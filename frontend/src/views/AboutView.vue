<script setup lang="ts">
import { siteProfile } from '../data/site'
</script>

<template>
  <main class="min-h-[70vh]">
    <!-- <section class="panel bg-soft" aria-labelledby="about-title"> -->
      <h1 class="text-3xl font-bold mb-4">关于我</h1>
      <p>
        你好，我是一名前端开发者，关注前端体验设计与工程实现，擅长把设计稿转成高质量、可维护的页面。
      </p>
      <!-- <p>
        我坚持移动端优先与渐进增强，重视性能、可访问性和长期维护成本。
      </p> -->
    <!-- </section> -->

    <!-- <section class="panel panel-contrast" aria-labelledby="contact-title"> -->
      <h1 class="text-3xl font-bold mt-16 mb-4">联系我</h1>
      <!-- <p>QQ邮箱：{{ siteProfile.email }}</p> -->
      <!-- <p>哔哩哔哩：<a :href="siteProfile.bilibili" target="_blank" rel="noopener noreferrer">{{ siteProfile.bilibili }}</a></p> -->
      <p>GitHub：<a :href="siteProfile.github" target="_blank" rel="noopener noreferrer">{{ siteProfile.github }}</a></p>
    <!-- </section> -->
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


.panel-contrast {
  background: var(--text-main);
  border-color: var(--accent);
}

.panel-contrast h2,
.panel-contrast p {
  color: var(--bg-main);
}
</style>
