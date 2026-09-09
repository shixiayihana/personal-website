<template>
  <div class="site-shell">
    <a href="#main-content" class="skip-link">跳到主内容</a>
    <SiteHeader />
    <section id="main-content">
      <RouterView />
    </section>
    <footer class="site-footer">
      <p>© 2026 Tang Studio.</p>
    </footer>
  </div>
</template>

<script setup lang="ts">
import SiteHeader from './components/SiteHeader.vue'
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Noto+Serif+SC:wght@400;500;600&display=swap');

/* 参照Vue Bits的配色方案，使用深色背景和柔和的紫色作为主色调 */
/* :root {
  --bg-main: #000000;      
  --bg-soft: #0a0a0a;       
  --bg-paper: #121212;      
  --line-soft: rgba(148, 163, 184, 0.24);
  --line-muted: rgba(148, 163, 184, 0.32);
  --text-main: #e2e8f0;
  --text-strong: #f8fafc;
  --text-muted: #94a3b8;
  --accent: #8b5cf6;
  --accent-deep: #7c3aed;
} */

/* 参照naiveUI的配色方案，使用深色背景和柔和的绿色作为主色调 */
:root {
  /* 背景分层，页面底色严格 rgb(16,16,20) → #101014 */
  --bg-main: #101014;
  --bg-soft: #18181c;
  --bg-paper: #1e1e26;

  /* 分割线边框 */
  --line-soft: rgba(255, 255, 255, 0.08);
  --line-muted: rgba(255, 255, 255, 0.14);

  /* 文字三级 */
  --text-strong: #ffffff;
  --text-main: #d4d4e0;
  --text-muted: #888899;

  /* NaiveUI 原版绿色主色 */
  --accent: #18a058;
  --accent-hover: #36ad6a;
  --accent-deep: #0c7a43;

  /* 状态色，沿用NaiveUI */
  --success: #52c41a;
  --warning: #f0a020;
  --error: #ff4d4f;
}


* {
  box-sizing: border-box;
}

html,
body,
#app {
  margin: 0;
  min-height: 100%;
}

body {
  background:
    radial-gradient(circle at 10% 10%, rgba(24, 160, 88, 0.08), transparent 28%),
    radial-gradient(circle at 90% 5%, rgba(54, 173, 106, 0.06), transparent 24%),
    var(--bg-main);
  color: var(--text-strong);
  font-family: 'Noto Serif SC', serif;
}
</style>

<style scoped>
.site-shell {
  max-width: 980px;
  margin: 0 auto;
  padding: 24px 20px 56px;
}

.skip-link {
  position: absolute;
  left: -9999px;
  top: 0;
}

.skip-link:focus {
  left: 12px;
  top: 12px;
  background: var(--text-main);
  color: var(--bg-main);
  padding: 8px 12px;
  border-radius: 8px;
}

.site-footer {
  margin-top: 28px;
  padding-top: 16px;
  border-top: 1px dashed var(--line-muted);
}

.site-footer p {
  margin: 0;
  color: var(--text-main);
}

@media (max-width: 640px) {
  .site-shell {
    padding: 14px 14px 36px;
  }
}
</style>
