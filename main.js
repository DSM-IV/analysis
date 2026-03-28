function getRandomNumbers() {
  const numbers = [];
  while (numbers.length < 6) {
    const n = Math.floor(Math.random() * 45) + 1;
    if (!numbers.includes(n)) numbers.push(n);
  }
  numbers.sort((a, b) => a - b);

  let bonus;
  do {
    bonus = Math.floor(Math.random() * 45) + 1;
  } while (numbers.includes(bonus));

  return { numbers, bonus };
}

function getBallClass(n) {
  if (n <= 10) return 'range-1';
  if (n <= 20) return 'range-10';
  if (n <= 30) return 'range-20';
  if (n <= 40) return 'range-30';
  return 'range-40';
}

function createBallHTML(n, delay, isBonus) {
  const cls = `ball ${getBallClass(n)}${isBonus ? ' bonus' : ''}`;
  return `<div class="${cls}" style="animation-delay:${delay}s">${n}</div>`;
}

function generate() {
  const count = parseInt(document.getElementById('setCount').value);
  const resultsEl = document.getElementById('results');
  resultsEl.innerHTML = '';

  const sets = [];
  for (let i = 0; i < count; i++) {
    const { numbers, bonus } = getRandomNumbers();
    sets.push({ numbers, bonus });

    const setDiv = document.createElement('div');
    setDiv.className = 'result-set';
    setDiv.style.animationDelay = `${i * 0.1}s`;

    let ballsHTML = '';
    numbers.forEach((n, j) => {
      ballsHTML += createBallHTML(n, j * 0.08, false);
    });
    ballsHTML += '<div class="plus">+</div>';
    ballsHTML += createBallHTML(bonus, 0.5, true);

    setDiv.innerHTML = `
      <div class="set-label">${String.fromCharCode(65 + i)}세트</div>
      <div class="balls">${ballsHTML}</div>
    `;
    resultsEl.appendChild(setDiv);
  }

  saveHistory(sets);
}

function saveHistory(sets) {
  const history = JSON.parse(localStorage.getItem('lottoHistory') || '[]');
  const now = new Date();
  const time = `${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}`;

  sets.forEach(set => {
    history.unshift({ numbers: set.numbers, bonus: set.bonus, time });
  });

  if (history.length > 50) history.length = 50;
  localStorage.setItem('lottoHistory', JSON.stringify(history));
  renderHistory();
}

function renderHistory() {
  const history = JSON.parse(localStorage.getItem('lottoHistory') || '[]');
  const section = document.getElementById('history');
  const list = document.getElementById('historyList');

  if (history.length === 0) {
    section.style.display = 'none';
    return;
  }

  section.style.display = 'block';
  list.innerHTML = '';

  history.forEach(item => {
    const div = document.createElement('div');
    div.className = 'history-item';

    let html = `<span class="timestamp">${item.time}</span>`;
    item.numbers.forEach(n => {
      html += `<div class="ball ${getBallClass(n)}">${n}</div>`;
    });
    html += '<div class="plus">+</div>';
    html += `<div class="ball ${getBallClass(item.bonus)} bonus">${item.bonus}</div>`;

    div.innerHTML = html;
    list.appendChild(div);
  });
}

function clearHistory() {
  localStorage.removeItem('lottoHistory');
  renderHistory();
}

renderHistory();
