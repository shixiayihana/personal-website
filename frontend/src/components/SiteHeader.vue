<template>
  <header class="topbar bg-soft">
    <RouterLink class="brand" to="/">Tang Studio</RouterLink>
    <nav aria-label="主导航">
      <RouterLink to="/">首页</RouterLink>
      <RouterLink to="/projects">作品</RouterLink>
      <RouterLink to="/about">关于</RouterLink>
      <!-- <RouterLink to="/test">测试</RouterLink> -->
    </nav>
  </header>
</template>

<style scoped>
.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 30px;
  padding: 12px 16px;
  /* background: rgba(17, 17, 17, 0.9); */
  border: 1px solid var(--line-muted);
  border-radius: 14px;
  backdrop-filter: blur(10px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
}

.brand {
  margin: 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.7rem;
  font-weight: 700;
  letter-spacing: 0.8px;
  color: #f8fafc;
  text-decoration: none;
}

nav {
  display: flex;
  gap: 18px;
}

nav a {
  color: #cbd5e1;
  text-decoration: none;
  border-bottom: 1px solid transparent;
  transition: color 200ms ease, border-color 200ms ease;
}

nav a:hover,
nav a.router-link-active {
  color: #f8fafc;
  border-color: var(--accent);
}

@media (max-width: 640px) {
  .topbar {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }

  nav {
    gap: 12px;
    flex-wrap: wrap;
  }
}
</style>
