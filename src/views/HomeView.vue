<script setup lang="ts">
import { projects, siteProfile } from '../data/site'
import CurvedLoop from "../components/CurvedLoop.vue";
import DecryptedText from '../components/DecryptedText.vue';
const featuredProjects = projects.slice(0, 3)
</script>

<template>
  <main>
    <div class="flex justify-center items-center bg-bg-main magin flex-col ">
      <!-- 内层容器：负责两个组件上下排列、组件之间留空隙，内部元素居中 -->
      <div class="flex flex-col gap-16 items-center">
        <DecryptedText text="Hi,I'm" :speed="50" :max-iterations="10" :sequential="false" reveal-direction="start"
          :use-original-chars-only="false" animate-on="hover" class-name="text-7xl justify-center text-blue-500"
          encrypted-class-name="text-7xl justify-center text-red-500" />

        <DecryptedText text="shixiayihana" :speed="50" :max-iterations="10" :sequential="false" reveal-direction="start"
          :use-original-chars-only="false" animate-on="hover" class-name="text-7xl text-blue-500"
          encrypted-class-name="text-7xl text-red-500" />

        <DecryptedText text="a Front‑end Developer" :speed="50" :max-iterations="10" :sequential="false"
          reveal-direction="start" :use-original-chars-only="false" animate-on="hover"
          class-name="text-7xl justify-center text-blue-500"
          encrypted-class-name="text-7xl justify-center text-red-500" />
      </div>
      <CurvedLoop marquee-text="Welcome ✦ to ✦ my ✦ personal ✦ website ✦" :speed="2" :curve-amount="200"
        direction="left" :interactive="true" />
    </div>


    <section class="hero" aria-labelledby="home-title">
      <p class="hero-kicker">{{ siteProfile.subtitle }}</p>
      <h1 id="home-title">{{ siteProfile.title }}</h1>
      <p>{{ siteProfile.intro }}</p>
      <div class="hero-actions">
        <RouterLink class="btn btn-primary" to="/projects">查看作品</RouterLink>
        <RouterLink class="btn btn-ghost" to="/about">了解我</RouterLink>
      </div>
    </section>

    <!-- <section class="panel panel-soft" aria-labelledby="featured-title">
      <h2 id="featured-title">精选作品</h2>
      <div class="work-grid">
        <article v-for="item in featuredProjects" :key="item.slug" class="project-card">
          <p class="tag">{{ item.tag }} · {{ item.year }}</p>
          <h3>{{ item.title }}</h3>
          <p>{{ item.description }}</p>
        </article>
      </div>
    </section> -->
  </main>
</template>

<style scoped>
.hero {
  background: linear-gradient(150deg, rgba(17, 17, 17, 0.98), rgba(12, 12, 12, 0.96));
  border: 1px solid var(--line-soft);
  border-radius: 18px;
  padding: 38px 28px;
  box-shadow: 0 20px 45px rgba(0, 0, 0, 0.28);
}

.hero-kicker {
  margin: 0 0 8px;
  color: var(--accent);
  letter-spacing: 1.6px;
  text-transform: uppercase;
  font-size: 0.78rem;
}

h1,
h2,
h3 {
  font-family: 'Cormorant Garamond', serif;
  margin-top: 0;
  color: #f8fafc;
}

h1 {
  margin-bottom: 14px;
  font-size: clamp(2rem, 3.8vw, 3.1rem);
  line-height: 1.08;
}

p {
  line-height: 1.72;
  color: #dbe3f0;
}

.hero-actions {
  display: flex;
  gap: 12px;
  margin-top: 24px;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 10px 16px;
  border-radius: 10px;
  text-decoration: none;
  font-weight: 600;
  transition: transform 200ms ease, background-color 200ms ease, color 200ms ease;
}

.btn:hover {
  transform: translateY(-1px);
}

.btn-primary {
  background: var(--accent);
  border: 1px solid var(--accent);
  color: #ffffff;
}

.btn-primary:hover {
  background: var(--accent-hover);
  border-color: var(--accent-hover);
}

.btn-ghost {
  background: transparent;
  border: 1px solid var(--line-soft);
  color: var(--text-main);
}

.btn-ghost:hover {
  border-color: var(--accent);
  color: var(--text-strong);
}

.panel {
  margin-top: 24px;
  border-radius: 16px;
  padding: 22px;
  border: 1px solid var(--line-soft);
}

.panel-soft {
  background: rgba(240, 234, 226, 0.78);
}

.work-grid {
  margin-top: 16px;
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

.project-card h3 {
  margin-bottom: 8px;
  font-size: 1.7rem;
}

@media (max-width: 860px) {
  .work-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 640px) {
  .hero {
    padding: 24px 18px;
  }

  .hero-actions {
    flex-direction: column;
  }

  .work-grid {
    grid-template-columns: 1fr;
  }
}
</style>
