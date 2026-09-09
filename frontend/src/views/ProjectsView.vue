<script setup lang="ts">
import { projects } from '../data/site'
</script>

<template>
  <main class="min-h-[70vh]">
    <h1 class="text-3xl font-bold mb-4">作品列表</h1>
    <p class="text-muted">这里是为了偷懒而开发的一些小玩意@_@</p>

    <section class="work-grid bg-paper" aria-label="项目卡片列表">
      <RouterLink v-for="item in projects" :key="item.slug" :to="`/projects/${item.slug}`"
        class="project-card">
        <p class="tag">{{ item.tag }} · {{ item.year }} · {{ item.month }}</p>
        <h2>{{ item.title }}</h2>
        <p>{{ item.description }}</p>
      </RouterLink>
    </section>
  </main>
</template>

<style scoped>
p {
  line-height: 1.72;
  color: var(--text-strong);
}

.panel {
  margin-top: 24px;
  border-radius: 16px;
  padding: 22px;
  border: 1px solid var(--line-soft);
}


.work-grid {
  margin-top: 24px;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
}

.project-card {
  background: var(--bg-paper);
  border: 1px solid var(--line-muted);
  border-radius: 14px;
  padding: 18px;
  box-shadow: 0 8px 20px rgba(71, 52, 32, 0.08);
}

.tag {
  margin: 0 0 8px;
  color: var(--text-muted);
  font-size: 0.82rem;
  text-transform: uppercase;
  letter-spacing: 1.1px;
}

@media (max-width: 860px) {
  .work-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 640px) {
  .work-grid {
    grid-template-columns: 1fr;
  }
}
</style>
