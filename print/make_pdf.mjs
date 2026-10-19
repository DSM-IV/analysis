#!/usr/bin/env node
// 과목별 인쇄용 PDF 생성기 (해석학2 · 선형대수1 · 선형대수2 · 집합론)
//
//   cd print && npm install            # puppeteer-core (설치된 Google Chrome 사용)
//   node print/make_pdf.mjs            # 4과목 전부
//   node print/make_pdf.mjs la2 la1    # 일부만
//
// 각 과목의 chNN.html(+부록)을 한 문서로 합쳐 한국어 패널만 남기고 증명·풀이를 펼친 뒤
// MathJax 조판이 끝나면 A4 PDF로 저장한다. 목차 쪽번호는 2패스(pdftotext로 단원 마커 탐지)로 채운다.
// 출력: print/out/<과목>.pdf, 중간 합본 HTML: print/out/build/<과목>.html
// 요구: Google Chrome(CHROME_PATH로 변경 가능), poppler의 pdftotext

import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { fileURLToPath, pathToFileURL } from 'node:url';
import puppeteer from 'puppeteer-core';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, '..');
const OUT_DIR = path.join(HERE, 'out');
const BUILD_DIR = path.join(OUT_DIR, 'build');
const CHROME = process.env.CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const SITE = 'https://univmathsurvive.com';
const PRETENDARD = 'https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css';

// A4 세로, 여백 상하 18mm · 좌우 15mm → 본문 180mm × 261mm
const MARGIN = { top: '18mm', bottom: '18mm', left: '15mm', right: '15mm' };
const PX_PER_MM = 96 / 25.4;
const CONTENT_W = Math.floor(180 * PX_PER_MM);
const CONTENT_H = Math.floor(261 * PX_PER_MM);
const KEEP_RATIO = 0.45;      // 본문 높이의 이 비율보다 짧은 카드는 쪽 경계에서 쪼개지 않는다
const KEEP_PROOF_RATIO = 0.3; // 짧은 증명 블록도 마찬가지

const SUBJECTS = {
  analysis2: { ko: '해석학2', en: 'Analysis II', out: '해석학2.pdf' },
  la1: { ko: '선형대수학 1', en: 'Linear Algebra I', out: '선형대수1.pdf',
         appendix: [{ file: 'quiz1.html', bilingual: true }, { file: 'midterm.html', bilingual: true }] },
  la2: { ko: '선형대수학 2', en: 'Linear Algebra II', out: '선형대수2.pdf',
         appendix: [{ file: 'midterm.html' }] },
  settheory: { ko: '집합론', en: 'Set Theory', out: '집합론.pdf' },
};

// ── 원본 페이지 읽기 ──────────────────────────────────────────────
function readUnit(subject, file, { appendix = false, bilingual = false } = {}) {
  const src = fs.readFileSync(path.join(ROOT, subject, file), 'utf8');
  const key = file.replace(/\.html$/, '');
  const header = src.match(/<header[^>]*>([\s\S]*?)<\/header>/)?.[1] ?? '';
  const h1 = header.match(/<h1>([\s\S]*?)<\/h1>/)?.[1] ?? key;
  const main = src.match(/<main[^>]*>([\s\S]*)<\/main>/)?.[1];
  if (main == null) throw new Error(`${subject}/${file}: <main> 없음`);
  const body = main
    .replace(/<!--[\s\S]*?-->/g, '')
    .replace(/<script\b[\s\S]*?<\/script>/g, '');
  return {
    key, file, appendix, bilingual, h1,
    subtitle: header.match(/<p class="subtitle">([\s\S]*?)<\/p>/)?.[1] ?? '',
    titleKo: h1.replace(/<span>[\s\S]*?<\/span>/, '').trim(),
    titleEn: h1.match(/<span>([\s\S]*?)<\/span>/)?.[1] ?? '',
    body,
    mjConfig: src.match(/<script>\s*(?:window\.)?MathJax\s*=[\s\S]*?<\/script>/)?.[0],
    mjSrc: src.match(/<script[^>]*src="([^"]*mathjax[^"]*)"/i)?.[1],
    cards: (body.match(/class="card[\s"]/g) || []).length,
    koProofs: (body.match(/class="proof-content"/g) || []).length,
  };
}

function loadSubject(subject) {
  const conf = SUBJECTS[subject];
  const chapters = fs.readdirSync(path.join(ROOT, subject))
    .filter(f => /^ch\d\d\.html$/.test(f)).sort()
    .map(f => readUnit(subject, f));
  const appendix = (conf.appendix || []).map(a => readUnit(subject, a.file, { appendix: true, bilingual: !!a.bilingual }));
  const units = [...chapters, ...appendix];
  const warnings = [];
  const first = units[0];
  for (const u of units) {
    if (u.mjConfig !== first.mjConfig || u.mjSrc !== first.mjSrc) warnings.push(`${u.file}: MathJax 설정이 ${first.file}와 다름 (${first.file} 기준으로 조판)`);
  }
  if (!first.mjConfig || !first.mjSrc) throw new Error(`${subject}/${first.file}: MathJax 설정을 찾지 못함`);
  return { conf, units, warnings };
}

function gitInfo(subject) {
  try {
    const hash = execFileSync('git', ['-C', ROOT, 'rev-parse', '--short', 'HEAD'], { encoding: 'utf8' }).trim();
    const dirty = execFileSync('git', ['-C', ROOT, 'status', '--porcelain', '--', subject], { encoding: 'utf8' }).trim();
    return dirty ? `${hash}+수정` : hash;
  } catch { return 'unknown'; }
}

function today() {
  const d = new Date();
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
}

// ── 합본 HTML ─────────────────────────────────────────────────────
function buildHtml(subject, { conf, units }) {
  const first = units[0];
  const nChapters = units.filter(u => !u.appendix).length;
  const appendixNames = units.filter(u => u.appendix).map(u => u.titleKo);

  let firstAppendix = true;
  const tocItems = units.map((u, i) => {
    const cls = u.appendix && firstAppendix ? ' class="t-appendix-start"' : '';
    if (u.appendix) firstAppendix = false;
    const num = u.appendix ? '부록' : String(i + 1).padStart(2, '0');
    return `<li${cls}><a href="#${u.key}"><span class="t-num">${num}</span>`
      + `<span class="t-title">${u.titleKo}<small>${u.titleEn}</small></span>`
      + `<span class="t-page" data-ch="${u.key}"></span></a></li>`;
  }).join('\n');

  const sections = units.map(u => {
    const cls = ['print-chapter', u.appendix && 'print-appendix', u.bilingual && 'print-bilingual'].filter(Boolean).join(' ');
    return `<section class="${cls}" id="${u.key}">
<span class="pdf-mark">zzpdfmark${u.key}zz</span>
<div class="print-ch-head"><p class="subtitle">${u.subtitle}</p><h1>${u.h1}</h1></div>
${u.body}
</section>`;
  }).join('\n');

  const desc = [`강의 단원 ${nChapters}개`, ...appendixNames.map(n => `부록 · ${n}`)].join('<br>');
  const bilingualNote = units.some(u => u.bilingual)
    ? `<p class="print-toc-note">한국어 번역만 싣고 증명·풀이는 모두 펼쳐 두었습니다. 단, ${units.filter(u => u.bilingual).map(u => u.titleKo).join(', ')}은 영어 답안 문장이 학습 대상이라 원래대로 영어를 함께 실었습니다.</p>`
    : `<p class="print-toc-note">한국어 번역만 싣고 증명·풀이는 모두 펼쳐 두었습니다.</p>`;

  return `<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>${conf.ko} — 인쇄본</title>
${first.mjConfig}
<script>
  // 인쇄본: 자동 조판을 끄고(정리 후 직접 조판) 화면 밖 수식을 건너뛰는 ui/lazy를 뺀다.
  MathJax.startup = Object.assign({}, MathJax.startup, { typeset: false });
  if (MathJax.loader && Array.isArray(MathJax.loader.load)) MathJax.loader.load = MathJax.loader.load.filter(x => x !== 'ui/lazy');
</script>
<script id="MathJax-script" async src="${first.mjSrc}"></script>
<link rel="stylesheet" href="${PRETENDARD}">
<link rel="stylesheet" href="${pathToFileURL(path.join(ROOT, subject, 'style.css')).href}">
<link rel="stylesheet" href="${pathToFileURL(path.join(HERE, 'print.css')).href}">
</head>
<body>
<main class="print-main">
<div class="print-cover">
  <p class="cover-kicker">학습 가이드 인쇄본</p>
  <div class="cover-title">${conf.ko}</div>
  <div class="cover-en">${conf.en}</div>
  <div class="cover-rule"></div>
  <p class="cover-desc">${desc}</p>
  <p class="cover-meta">${today()} 생성 · ${gitInfo(subject)}</p>
</div>
<div class="print-toc-page">
  <h1>목차</h1>
  <ol class="print-toc">
${tocItems}
  </ol>
  ${bilingualNote}
</div>
${sections}
</main>
</body>
</html>
`;
}

// ── 브라우저 안에서 실행: 화면용 요소 정리 (조판 전) ────────────────────
function prepDom({ site, subject }) {
  const stats = { ads: 0, enPanels: 0, toggles: 0, details: 0, brokenLinks: [] };
  const sections = [...document.querySelectorAll('section.print-chapter')];
  const keys = new Set(sections.map(s => s.id));

  for (const sec of sections) {
    const ch = sec.id;
    sec.querySelectorAll('ins.adsbygoogle').forEach(ins => {
      const wrap = ins.parentElement;
      (wrap !== sec && wrap.children.length === 1 ? wrap : ins).remove();
      stats.ads++;
    });
    sec.querySelectorAll('nav.toc').forEach(n => n.remove());
    if (!sec.classList.contains('print-bilingual')) {
      sec.querySelectorAll('.en-panel').forEach(n => { n.remove(); stats.enPanels++; });
      sec.querySelectorAll('.panel-label').forEach(n => n.remove());
    }
    sec.querySelectorAll('button.proof-toggle').forEach(btn => {
      const label = document.createElement('div');
      label.className = 'print-proof-label';
      const text = (btn.dataset.show || btn.textContent).replace(/[▶▸►]/g, '').trim();
      label.textContent = text.replace(/\s*보기$/, '') || '증명';
      btn.replaceWith(label);
      stats.toggles++;
    });
    sec.querySelectorAll('.proof-content, .en-proof-content').forEach(n => n.classList.add('visible'));
    sec.querySelectorAll('details').forEach(d => { d.open = true; stats.details++; });
    // 단원끼리 id가 겹치지 않도록 접두사 (SVG 내부 정의 id는 이미 유일하고 url(#…)로 참조되므로 제외)
    sec.querySelectorAll('[id]').forEach(el => { if (!el.closest('svg')) el.id = `${ch}--${el.id}`; });
  }

  for (const sec of sections) {
    const ch = sec.id;
    sec.querySelectorAll('a[href]').forEach(a => {
      const href = a.getAttribute('href');
      if (href === '#') return;
      let target = null, m;
      if (href.startsWith('#')) target = `${ch}--${decodeURIComponent(href.slice(1))}`;
      else if ((m = href.match(/^([\w-]+)\.html(?:#(.*))?$/)) && keys.has(m[1])) target = m[2] ? `${m[1]}--${decodeURIComponent(m[2])}` : m[1];
      if (target !== null) {
        if (!document.getElementById(target)) stats.brokenLinks.push(`${ch}: ${href}`);
        a.setAttribute('href', '#' + target);
      } else if (!/^[a-z][\w+.-]*:/i.test(href)) {
        a.setAttribute('href', new URL(href, `${site}/${subject}/`).href);
      }
    });
  }
  return stats;
}

// ── 브라우저 안에서 실행: 조판 후 검사·넘침 축소·쪽 나눔 보정 ─────────────
function fitAndCheck({ contentH, keepRatio, keepProofRatio }) {
  const out = { merror: [], rawTex: [], scaledDisplay: 0, scaledInline: 0, stillWide: [], keep: 0, cards: 0, koProofs: 0 };
  const where = el => {
    const c = el.closest('.card, .qs-block');
    const sec = el.closest('section.print-chapter');
    return (c && c.id) || (sec ? sec.id : '?');
  };
  const main = document.querySelector('main');

  main.querySelectorAll('mjx-merror').forEach(e => out.merror.push(`${where(e)}: ${e.textContent.slice(0, 80)}`));

  const walker = document.createTreeWalker(main, NodeFilter.SHOW_TEXT, {
    acceptNode: n => n.parentElement.closest('mjx-container, script, style, .pdf-mark') ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT,
  });
  for (let n; (n = walker.nextNode());) {
    if (/\$|\\\(|\\\[|\\[a-zA-Z]+[{_^]/.test(n.data)) out.rawTex.push(`${where(n.parentElement)}: ${n.data.trim().slice(0, 80)}`);
  }

  // 본문폭을 넘는 수식은 글자 크기를 줄여 맞춘다 (v3 CHTML은 자동 줄바꿈이 없다).
  // \tag가 붙은 수식은 컨테이너에 min-width가 걸려 부모보다 넓어지므로, 부모의 내용 상자를 기준으로
  // 실제로 그려진 자손(mjx-math 아래, 숨은 mjx-assistive-mml 제외)의 오른쪽 끝을 잰다.
  const contentRight = mc => {
    let r = -Infinity;
    for (const e of mc.querySelectorAll('mjx-math, mjx-math *')) { const b = e.getBoundingClientRect(); if (b.width) r = Math.max(r, b.right); }
    return r;
  };
  const contentBox = el => {
    const b = el.getBoundingClientRect(), cs = getComputedStyle(el);
    return { left: b.left + parseFloat(cs.paddingLeft), right: b.right - parseFloat(cs.paddingRight) };
  };
  main.querySelectorAll('mjx-container[display="true"]').forEach(mc => {
    const { left, right } = contentBox(mc.parentElement);
    let pct = 100, scaled = false;
    for (let i = 0; i < 8 && pct > 55; i++) {
      const r = contentRight(mc);
      if (r <= right + 1) break;
      pct = Math.max(55, Math.floor((pct * (right - left)) / (r - left)) - 1);
      mc.style.fontSize = `${pct}%`;
      scaled = true;
    }
    if (scaled) out.scaledDisplay++;
  });
  main.querySelectorAll('mjx-container:not([display="true"])').forEach(mc => {
    const block = mc.parentElement.closest('p, li, td, th, div');
    if (!block) return;
    const cs = getComputedStyle(block);
    const avail = block.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
    if (mc.getBoundingClientRect().width > avail + 1) {
      mc.style.fontSize = `${Math.max(55, Math.floor((100 * avail) / mc.getBoundingClientRect().width))}%`;
      out.scaledInline++;
    }
  });
  main.querySelectorAll('mjx-container').forEach(mc => {
    const box = mc.parentElement.closest('.card, .qs-block, section');
    if (box && contentRight(mc) > box.getBoundingClientRect().right + 1) out.stillWide.push(where(mc));
  });

  main.querySelectorAll('.card, .qs-block').forEach(c => {
    if (c.getBoundingClientRect().height < contentH * keepRatio) { c.classList.add('keep'); out.keep++; }
  });
  main.querySelectorAll('.proof-content, .en-proof-content').forEach(p => {
    if (p.getBoundingClientRect().height < contentH * keepProofRatio) p.style.breakInside = 'avoid';
  });

  out.cards = main.querySelectorAll('.card').length;
  out.koProofs = main.querySelectorAll('.proof-content').length;
  return out;
}

// ── PDF ───────────────────────────────────────────────────────────
function pdfOptions(conf) {
  const font = "font-family:'Apple SD Gothic Neo','Noto Sans KR',sans-serif;";
  return {
    format: 'A4',
    margin: MARGIN,
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: `<div style="width:100%;padding:0 15mm;font-size:7.5px;color:#8B95A1;${font}">${conf.ko} · ${conf.en}</div>`,
    footerTemplate: `<div style="width:100%;text-align:center;font-size:8px;color:#6B7684;${font}"><span class="pageNumber"></span> / <span class="totalPages"></span></div>`,
    outline: true,
    tagged: true,
    timeout: 0,
  };
}

// 1차 PDF에서 단원 마커가 처음 나오는 쪽을 찾는다
function findChapterPages(pdfBuf, keys) {
  const tmp = path.join(fs.mkdtempSync(path.join(os.tmpdir(), 'printpdf-')), 'pass1.pdf');
  fs.writeFileSync(tmp, pdfBuf);
  const text = execFileSync('pdftotext', ['-enc', 'UTF-8', tmp, '-'], { encoding: 'utf8', maxBuffer: 256 * 1024 * 1024 });
  fs.rmSync(path.dirname(tmp), { recursive: true, force: true });
  const pages = text.split('\f').map(p => p.replace(/\s+/g, ''));
  const found = {};
  for (const k of keys) {
    const i = pages.findIndex(p => p.includes(`zzpdfmark${k}zz`));
    if (i >= 0) found[k] = i + 1;
  }
  return { found, pageCount: pages.length - (pages.at(-1) === '' ? 1 : 0) };
}

async function makeSubject(browser, subject) {
  const t0 = Date.now();
  const data = loadSubject(subject);
  const { conf, units, warnings } = data;
  fs.mkdirSync(BUILD_DIR, { recursive: true });
  const htmlPath = path.join(BUILD_DIR, `${subject}.html`);
  fs.writeFileSync(htmlPath, buildHtml(subject, data));

  const page = await browser.newPage();
  page.on('pageerror', e => warnings.push(`pageerror: ${e.message}`));
  page.on('requestfailed', r => warnings.push(`요청 실패: ${r.url()} (${r.failure()?.errorText})`));
  await page.setViewport({ width: CONTENT_W, height: 1200 });
  await page.emulateMediaType('print');
  await page.goto(pathToFileURL(htmlPath).href, { waitUntil: 'load', timeout: 180000 });
  // 조건식이 Promise를 돌려주면 puppeteer가 그 값을 기다리므로 boolean으로 바꿔 둔다
  await page.waitForFunction(() => !!(window.MathJax && MathJax.startup && MathJax.startup.promise), { timeout: 120000 });

  const prep = await page.evaluate(prepDom, { site: SITE, subject });
  await page.evaluate(async () => { await MathJax.startup.promise; await MathJax.typesetPromise(); });
  await page.waitForNetworkIdle({ idleTime: 1000, timeout: 120000 }).catch(() => warnings.push('네트워크 유휴 대기 시간 초과'));
  await page.evaluate(() => document.fonts.ready);
  const check = await page.evaluate(fitAndCheck, { contentH: CONTENT_H, keepRatio: KEEP_RATIO, keepProofRatio: KEEP_PROOF_RATIO });

  // 1차: 단원 시작 쪽 찾기 → 목차 채우고 마커 제거 → 2차
  const keys = units.map(u => u.key);
  const pass1 = await page.pdf(pdfOptions(conf));
  const { found, pageCount: pages1 } = findChapterPages(pass1, keys);
  const missing = keys.filter(k => !found[k]);
  if (missing.length) warnings.push(`쪽번호를 못 찾은 단원: ${missing.join(', ')}`);
  await page.evaluate(found => {
    document.querySelectorAll('.t-page').forEach(el => { el.textContent = found[el.dataset.ch] ?? ''; });
    document.querySelectorAll('.pdf-mark').forEach(el => el.remove());
  }, found);
  const pdf = await page.pdf(pdfOptions(conf));
  await page.close();

  fs.mkdirSync(OUT_DIR, { recursive: true });
  const outPath = path.join(OUT_DIR, conf.out);
  fs.writeFileSync(outPath, pdf);
  const pages2 = Number(execFileSync('pdfinfo', [outPath], { encoding: 'utf8' }).match(/Pages:\s+(\d+)/)?.[1]);
  if (pages2 !== pages1) warnings.push(`1차(${pages1}쪽)와 2차(${pages2}쪽) 쪽수가 다름 — 목차 쪽번호 재확인 필요`);
  const hasOutline = Buffer.from(pdf).includes('/Outlines');

  const srcCards = units.reduce((s, u) => s + u.cards, 0);
  const srcProofs = units.reduce((s, u) => s + u.koProofs, 0);
  if (check.cards !== srcCards) warnings.push(`카드 수 불일치: 원본 ${srcCards} / 인쇄 ${check.cards}`);
  if (check.koProofs !== srcProofs) warnings.push(`증명 블록 수 불일치: 원본 ${srcProofs} / 인쇄 ${check.koProofs}`);

  console.log(`\n■ ${conf.ko} → ${path.relative(ROOT, outPath)}  (${pages2}쪽, ${((Date.now() - t0) / 1000).toFixed(0)}초)`);
  console.log(`  단원 시작 쪽: ${keys.map(k => `${k}=${found[k] ?? '?'}`).join(' ')}`);
  console.log(`  카드 ${check.cards}/${srcCards} · 증명/풀이 ${check.koProofs}/${srcProofs} · 토글 ${prep.toggles} · 영어 패널 제거 ${prep.enPanels} · details ${prep.details} · 광고 ${prep.ads}`);
  console.log(`  수식 오류 ${check.merror.length} · 미조판 TeX ${check.rawTex.length} · 축소(display ${check.scaledDisplay}, inline ${check.scaledInline}) · 여전히 넘침 ${check.stillWide.length} · keep ${check.keep} · 책갈피 ${hasOutline ? '있음' : '없음'}`);
  const list = (label, arr) => { if (arr.length) console.log(`  ${label}:\n    ${arr.slice(0, 15).join('\n    ')}${arr.length > 15 ? `\n    … 외 ${arr.length - 15}건` : ''}`); };
  list('수식 오류', check.merror);
  list('미조판 TeX', check.rawTex);
  list('넘치는 수식', [...new Set(check.stillWide)]);
  list('깨진 내부 링크', prep.brokenLinks);
  list('경고', warnings);
  return { subject, outPath, pages: pages2, problems: check.merror.length + check.rawTex.length };
}

const targets = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(SUBJECTS);
for (const t of targets) if (!SUBJECTS[t]) { console.error(`알 수 없는 과목: ${t} (가능: ${Object.keys(SUBJECTS).join(', ')})`); process.exit(2); }

const browser = await puppeteer.launch({ executablePath: CHROME, headless: true, args: ['--allow-file-access-from-files'] });
const results = [];
try {
  for (const t of targets) results.push(await makeSubject(browser, t));
} finally {
  await browser.close();
}
console.log('\n완료:');
for (const r of results) console.log(`  ${r.outPath}  ${r.pages}쪽${r.problems ? `  ⚠ 수식 문제 ${r.problems}건` : ''}`);
