const TIMER_SECONDS = 20;
const SCENARIO_URL = "scenarios/rcp/001_paro_calle.json";

const state = {
  scenario: null,
  currentStep: 0,
  life: 100,
  score: 0,
  streak: 0,
  bestStreak: 0,
  hits: 0,
  timerId: null,
  timeLeft: 0,
  answered: false,
  history: []
};

const el = {};
const IDS = [
  'start-screen','game-screen','end-screen','scenario-title','scenario-context',
  'scenario-difficulty','scenario-steps','start-btn','lifebar','life-value',
  'streak','score','timer','step-counter','progress-bar','situation-text',
  'options','feedback','next-btn','result-banner','final-verdict','final-score',
  'final-life','final-streak','final-hits','review-list','restart-btn'
];
IDS.forEach(id => {
  el[id.replace(/-(\w)/g, (_, c) => c.toUpperCase())] = document.getElementById(id);
});
el.timerWrap = document.querySelector('.hud-item.timer');

function showScreen(name) {
  ['start','game','end'].forEach(s => {
    document.getElementById(s + '-screen').classList.toggle('active', s === name);
  });
}

async function loadScenario() {
  try {
    const res = await fetch(SCENARIO_URL);
    if (!res.ok) throw new Error('HTTP ' + res.status);
    state.scenario = await res.json();
    el.scenarioTitle.textContent = state.scenario.titulo;
    el.scenarioContext.textContent = state.scenario.contexto;
    el.scenarioDifficulty.textContent = '📊 ' + state.scenario.dificultad;
    el.scenarioSteps.textContent = '🎯 ' + state.scenario.pasos.length + ' decisiones';
  } catch (err) {
    el.scenarioTitle.textContent = 'Error cargando escenario';
    el.scenarioContext.textContent = 'Verifica que el JSON esté en scenarios/rcp/. Sirviendo localmente con `python3 -m http.server` desde /game.';
    console.error(err);
  }
}

function startGame() {
  if (!state.scenario) return;
  Object.assign(state, {
    currentStep: 0, life: 100, score: 0,
    streak: 0, bestStreak: 0, hits: 0, history: []
  });
  showScreen('game');
  renderStep();
}

function renderStep() {
  const step = state.scenario.pasos[state.currentStep];
  state.answered = false;
  el.stepCounter.textContent = 'Paso ' + (state.currentStep + 1) + ' de ' + state.scenario.pasos.length;
  el.progressBar.style.width = (state.currentStep / state.scenario.pasos.length * 100) + '%';
  el.situationText.textContent = step.situacion;
  el.options.innerHTML = '';
  el.feedback.classList.add('hidden');
  el.nextBtn.classList.add('hidden');
  step.opciones.forEach((opt, i) => {
    const btn = document.createElement('button');
    btn.className = 'option';
    btn.innerHTML = '<span class="option-letter">' + String.fromCharCode(65 + i) + '</span>' + escapeHtml(opt.texto);
    btn.onclick = () => selectOption(i);
    el.options.appendChild(btn);
  });
  updateHUD();
  startTimer();
}

function escapeHtml(s) {
  return s.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}

function startTimer() {
  state.timeLeft = TIMER_SECONDS;
  el.timer.textContent = state.timeLeft;
  el.timerWrap.classList.remove('warning', 'critical');
  clearInterval(state.timerId);
  state.timerId = setInterval(() => {
    state.timeLeft--;
    el.timer.textContent = state.timeLeft;
    if (state.timeLeft <= 5) {
      el.timerWrap.classList.remove('warning');
      el.timerWrap.classList.add('critical');
    } else if (state.timeLeft <= 10) {
      el.timerWrap.classList.add('warning');
    }
    if (state.timeLeft <= 0) {
      clearInterval(state.timerId);
      timeOut();
    }
  }, 1000);
}

function timeOut() {
  if (state.answered) return;
  state.answered = true;
  state.life = Math.max(0, state.life - 10);
  state.streak = 0;
  state.history.push({
    step: state.currentStep, choice: null, correct: false,
    choiceText: null,
    feedback: '⏱ No respondiste a tiempo. En ECOE el silencio penaliza.'
  });
  el.feedback.className = 'feedback incorrect';
  el.feedback.innerHTML = '⏱ <strong>Tiempo agotado.</strong> En el ECOE quedarse callado cuesta. <small>-10 vida</small>';
  el.feedback.classList.remove('hidden');
  Array.from(el.options.children).forEach(c => c.disabled = true);
  updateHUD();
  if (state.life <= 0) {
    setTimeout(() => endGame(true), 1500);
  } else {
    el.nextBtn.classList.remove('hidden');
  }
}

function selectOption(idx) {
  if (state.answered) return;
  state.answered = true;
  clearInterval(state.timerId);
  const step = state.scenario.pasos[state.currentStep];
  const opt = step.opciones[idx];
  const buttons = Array.from(el.options.children);
  step.opciones.forEach((o, i) => {
    if (o.correcta) buttons[i].classList.add('correct');
    else if (i === idx) buttons[i].classList.add('incorrect');
    buttons[i].disabled = true;
  });
  let lifeDelta = 0;
  let bonusText = '';
  if (opt.correcta) {
    state.hits++;
    state.streak++;
    state.bestStreak = Math.max(state.bestStreak, state.streak);
    const streakBonus = Math.min(state.streak - 1, 5) * 2;
    state.score += opt.puntos + streakBonus;
    lifeDelta = 2;
    if (streakBonus > 0) bonusText = ' · 🔥 +' + streakBonus + ' streak';
    el.feedback.className = 'feedback correct';
    el.feedback.innerHTML = opt.feedback + '<br><small>+' + opt.puntos + ' pts' + bonusText + '</small>';
  } else {
    state.streak = 0;
    state.score = Math.max(0, state.score + opt.puntos);
    lifeDelta = opt.puntos;
    el.feedback.className = opt.puntos <= -10 ? 'feedback incorrect' : 'feedback warning';
    el.feedback.innerHTML = opt.feedback + '<br><small>' + opt.puntos + ' pts</small>';
  }
  state.life = Math.max(0, Math.min(100, state.life + lifeDelta));
  state.history.push({
    step: state.currentStep, choice: idx, correct: opt.correcta,
    choiceText: opt.texto, feedback: opt.feedback
  });
  el.feedback.classList.remove('hidden');
  updateHUD();
  if (state.life <= 0) {
    setTimeout(() => endGame(true), 1800);
  } else {
    el.nextBtn.classList.remove('hidden');
  }
}

function updateHUD() {
  el.lifebar.style.width = state.life + '%';
  el.lifebar.classList.remove('warn', 'crit');
  if (state.life <= 30) el.lifebar.classList.add('crit');
  else if (state.life <= 60) el.lifebar.classList.add('warn');
  el.lifeValue.textContent = state.life + '%';
  el.streak.textContent = '🔥 ' + state.streak;
  el.score.textContent = state.score;
}

function nextStep() {
  state.currentStep++;
  if (state.currentStep >= state.scenario.pasos.length) {
    endGame(false);
  } else {
    renderStep();
  }
}

function endGame(patientDied) {
  clearInterval(state.timerId);
  showScreen('end');
  const total = state.scenario.pasos.length;
  let verdict, banner;
  if (patientDied) {
    banner = '💀';
    verdict = 'El paciente no sobrevivió. Revisa tus decisiones y reintenta.';
  } else {
    const pct = state.hits / total;
    if (pct >= 0.85) { banner = '🏆'; verdict = '¡Excelente! Listo para sala de simulación ECOE.'; }
    else if (pct >= 0.7) { banner = '✅'; verdict = 'Aprobado. Pule los puntos donde fallaste.'; }
    else if (pct >= 0.5) { banner = '⚠️'; verdict = 'En el límite. Vuelve a repasar las capas de RCP y reintenta.'; }
    else { banner = '❌'; verdict = 'Necesitas repaso profundo. Empieza por Capa 1 del flujo macro.'; }
  }
  el.resultBanner.textContent = banner;
  el.finalVerdict.textContent = verdict;
  el.finalScore.textContent = state.score;
  el.finalLife.textContent = state.life + '%';
  el.finalStreak.textContent = '🔥 ' + state.bestStreak;
  el.finalHits.textContent = state.hits + '/' + total;
  el.reviewList.innerHTML = '';
  state.history.forEach((h, i) => {
    const div = document.createElement('div');
    div.className = 'review-item';
    const icon = h.correct ? '✅' : (h.choice === null ? '⏱' : '❌');
    let inner = '<strong>' + icon + ' Paso ' + (i + 1) + '</strong>';
    if (h.choiceText) inner += '<em>"' + escapeHtml(h.choiceText) + '"</em>';
    inner += '<small>' + h.feedback + '</small>';
    div.innerHTML = inner;
    el.reviewList.appendChild(div);
  });
}

el.startBtn.onclick = startGame;
el.nextBtn.onclick = nextStep;
el.restartBtn.onclick = startGame;

loadScenario();
