function toggleLang() {
  const showKo = document.getElementById('toggle-ko').checked;
  const showEn = document.getElementById('toggle-en').checked;
  document.body.classList.toggle('hide-ko', !showKo);
  document.body.classList.toggle('hide-en', !showEn);
}

function toggleProof(btn) {
  btn.classList.toggle('open');
  const arrow = btn.querySelector('.arrow');
  const content = btn.nextElementSibling;
  content.classList.toggle('visible');
  const isVisible = content.classList.contains('visible');
  const isEn = btn.closest('.en-panel') !== null;
  const show = btn.dataset.show || (isEn ? 'Proof' : '증명 보기');
  const hide = btn.dataset.hide || (isEn ? 'Hide Proof' : '증명 접기');
  btn.innerHTML = '';
  btn.appendChild(arrow);
  btn.append(' ' + (isVisible ? hide : show));
}

window.addEventListener('scroll', function() {
  const btn = document.getElementById('scrollTop');
  if (btn) btn.classList.toggle('visible', window.scrollY > 400);
});
