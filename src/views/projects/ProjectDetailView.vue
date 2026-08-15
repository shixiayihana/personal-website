<script setup lang="ts">
import { useRoute } from 'vue-router'

const route = useRoute()
</script>

<template>
  <main class="detail-page">
    <p class="eyebrow">Project Detail</p>
    <h1>{{ route.params.slug }}</h1>
    <p>详情页内容待补充。</p>
  </main>
</template>

<style scoped>
.detail-page {
  min-height: 60vh;
  padding: 32px 0;
}

.eyebrow {
  margin: 0 0 10px;
  color: var(--text-muted);
  font-size: 0.8rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

h1 {
  margin: 0 0 12px;
  color: var(--text-strong);
}

p {
  color: var(--text-main);
  line-height: 1.7;
}
</style>
