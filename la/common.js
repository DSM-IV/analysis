function toggleLang() {
  const showKo = document.getElementById('toggle-ko').checked;
  const showEn = document.getElementById('toggle-en').checked;
  document.body.classList.toggle('hide-ko', !showKo);
  document.body.classList.toggle('hide-en', !showEn);
}

function toggleProof(btn) {
  btn.classList.toggle('open');
  const arrow = btn.querySelector('.arrow');
  const isEn = btn.closest('.en-panel') !== null;
  let content = btn.nextElementSibling;
  content.classList.toggle('visible');
  const isVisible = content.classList.contains('visible');

  btn.innerHTML = '';
  btn.appendChild(arrow);
  if (isEn) {
    btn.append(' ' + (isVisible ? 'Hide Proof' : 'Proof'));
  } else {
    btn.append(' ' + (isVisible ? '증명 접기' : '증명 보기'));
  }
}

window.addEventListener('scroll', function() {
  const btn = document.getElementById('scrollTop');
  if (btn) btn.classList.toggle('visible', window.scrollY > 400);
});
