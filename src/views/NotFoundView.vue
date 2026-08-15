<template>
  <main class="not-found">
    <p class="code">404</p>
    <h1>页面不存在</h1>
    <p>你访问的页面可能被移动或删除了。</p>
    <RouterLink class="back-home" to="/">返回首页</RouterLink>
  </main>
</template>

<style scoped>
.not-found {
  display: grid;
  place-items: center;
  text-align: center;
  padding: 70px 16px;
}

.code {
  margin: 0;
  font-family: 'Cormorant Garamond', serif;
  color: var(--accent-deep);
  font-size: 3rem;
}

h1 {
  margin: 8px 0;
  color: var(--text-main);
  font-family: 'Cormorant Garamond', serif;
}

p {
  margin: 0;
  color: var(--text-strong);
}

.back-home {
  margin-top: 20px;
  color: var(--text-main);
  text-decoration: none;
  border-bottom: 1px solid var(--accent);
}
</style>
