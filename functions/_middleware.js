// Cloudflare Pages Functions — site-wide password gate.
//
// Set the environment variable SITE_PASSWORD in the Pages dashboard
// (Settings → Environment variables → Production). While it is unset,
// the site stays open so a missing variable never locks you out.
//
// Flow: no cookie → login page (401) → POST /__login → cookie (30 days)
//       GET /__logout clears the cookie.

const COOKIE = 'ums_auth';
const MAX_AGE = 60 * 60 * 24 * 30; // 30 days
const OPEN_PATHS = new Set(['/ads.txt', '/robots.txt', '/favicon.ico']);

async function sha256(text) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
  return [...new Uint8Array(buf)].map(b => b.toString(16).padStart(2, '0')).join('');
}

function timingSafeEqual(a, b) {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

function getCookie(request, name) {
  const header = request.headers.get('Cookie') || '';
  for (const part of header.split(';')) {
    const [k, ...v] = part.trim().split('=');
    if (k === name) return v.join('=');
  }
  return null;
}

function escapeHtml(s) {
  return s.replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
}

function safeNext(raw) {
  if (!raw || !raw.startsWith('/') || raw.startsWith('//') || raw.startsWith('/__')) return '/';
  return raw;
}

function loginPage(next, error) {
  return `<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>대학수학생존 · 로그인</title>
<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<style>
:root{--g50:#EAF9F1;--g600:#0AA65B;--g700:#08894B;--grey50:#F9FAFB;--grey100:#F2F4F6;--grey200:#E5E8EB;--grey300:#D1D6DB;--grey500:#8B95A1;--grey700:#4E5968;--grey900:#191F28;--pink:#E0396B;--pink-bg:#FFECF0;color-scheme:light}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%}
body{font-family:'Pretendard Variable',Pretendard,-apple-system,BlinkMacSystemFont,system-ui,'Apple SD Gothic Neo','Noto Sans KR',sans-serif;background:var(--grey50);color:var(--grey900);letter-spacing:-.01em;-webkit-font-smoothing:antialiased;display:flex;align-items:center;justify-content:center;padding:24px}
.card{width:100%;max-width:380px;background:#fff;border-radius:24px;padding:40px 32px 32px;box-shadow:0 2px 8px rgba(25,31,40,.04),0 12px 32px rgba(25,31,40,.06)}
.logo{display:flex;align-items:center;gap:10px;margin-bottom:28px}
.logo-mark{width:36px;height:36px;border-radius:10px;background:var(--g600);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:20px}
.logo-name{font-weight:800;font-size:18px}
h1{font-size:22px;font-weight:800;line-height:1.35;margin-bottom:6px}
p.sub{font-size:14px;color:var(--grey500);margin-bottom:24px}
label{display:block;font-size:13px;font-weight:600;color:var(--grey700);margin-bottom:8px}
input{width:100%;height:52px;border:1.5px solid var(--grey200);border-radius:14px;padding:0 16px;font:inherit;font-size:16px;background:var(--grey50);color:var(--grey900);outline:none;transition:border-color .15s,background .15s}
input:focus{border-color:var(--g600);background:#fff}
input.err{border-color:var(--pink)}
.error{display:flex;align-items:center;gap:6px;color:var(--pink);font-size:13px;font-weight:600;margin-top:10px}
button{width:100%;height:52px;margin-top:20px;border:0;border-radius:14px;background:var(--g600);color:#fff;font:inherit;font-size:16px;font-weight:700;cursor:pointer;transition:background .15s}
button:hover{background:var(--g700)}
button:active{transform:scale(.99)}
.foot{margin-top:24px;text-align:center;font-size:12px;color:var(--grey500)}
</style>
</head>
<body>
<form class="card" method="POST" action="/__login" autocomplete="off">
  <div class="logo"><span class="logo-mark">√</span><span class="logo-name">대학수학생존</span></div>
  <h1>비밀번호를 입력해 주세요</h1>
  <p class="sub">이 사이트는 비공개 학습 노트예요.</p>
  <label for="pw">비밀번호</label>
  <input id="pw" name="password" type="password" class="${error ? 'err' : ''}" autofocus required>
  ${error ? '<div class="error">비밀번호가 맞지 않아요. 다시 확인해 주세요.</div>' : ''}
  <input type="hidden" name="next" value="${escapeHtml(next)}">
  <button type="submit">입장하기</button>
  <div class="foot">© univmathsurvive.com</div>
</form>
</body>
</html>`;
}

function html(body, status, extraHeaders = {}) {
  return new Response(body, {
    status,
    headers: { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store', ...extraHeaders },
  });
}

export async function onRequest(context) {
  const { request, env, next } = context;
  const password = env.SITE_PASSWORD;

  // No password configured → site stays open.
  if (!password) return next();

  const url = new URL(request.url);
  const path = url.pathname;
  const expected = await sha256(password);

  if (path === '/__logout') {
    return new Response(null, {
      status: 302,
      headers: {
        Location: '/',
        'Set-Cookie': `${COOKIE}=; Path=/; Max-Age=0; HttpOnly; Secure; SameSite=Lax`,
      },
    });
  }

  if (path === '/__login') {
    if (request.method !== 'POST') return Response.redirect(url.origin + '/', 302);
    const form = await request.formData();
    const given = String(form.get('password') || '');
    const target = safeNext(String(form.get('next') || '/'));
    const ok = timingSafeEqual(await sha256(given), expected);
    if (!ok) return html(loginPage(target, true), 401);
    return new Response(null, {
      status: 302,
      headers: {
        Location: target,
        'Set-Cookie': `${COOKIE}=${expected}; Path=/; Max-Age=${MAX_AGE}; HttpOnly; Secure; SameSite=Lax`,
      },
    });
  }

  if (OPEN_PATHS.has(path)) return next();

  const cookie = getCookie(request, COOKIE);
  if (cookie && timingSafeEqual(cookie, expected)) return next();

  const target = safeNext(path + url.search);
  return html(loginPage(target, false), 401);
}
