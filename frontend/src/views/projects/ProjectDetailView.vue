<script setup lang="ts">
import { onMounted, ref } from 'vue'

import {
  getLatestValuations,
  type Valuation,
} from '../../api/cn-index-percentile'

const valuations = ref<Valuation[]>([])
const isLoading = ref(true)
const errorMessage = ref('')

const percentage = (value: number) => `${(value * 100).toFixed(2)}%`

const statusClass = (value: number) => {
  const percent = value * 100
  if (percent <= 40) return 'status-low'
  if (percent < 80) return 'status-middle'
  return 'status-high'
}

const statusLabel = (value: number) => {
  const percent = value * 100
  if (percent <= 40) return '相对低位'
  if (percent < 80) return '中位区间'
  return '相对高位'
}

const loadValuations = async () => {
  isLoading.value = true
  errorMessage.value = ''

  try {
    valuations.value = await getLatestValuations()
  } catch {
    valuations.value = []
    errorMessage.value = '数据暂时无法获取，请稍后重试'
  } finally {
    isLoading.value = false
  }
}

onMounted(loadValuations)
</script>

<template>
  <main class="detail-page">
    <header class="page-heading">
      <div>
        <p class="eyebrow">CN INDEX PERCENTILE</p>
        <h1>A股分位观测站</h1>
        <p class="intro">主要宽基指数估值百分位的每日观察。</p>
      </div>
      <p v-if="valuations.length" class="updated-at">
        更新于 {{ valuations[0]?.data }}
      </p>
    </header>

    <section v-if="isLoading" class="message-panel" aria-live="polite">
      正在读取最新估值数据...
    </section>

    <section v-else-if="errorMessage" class="message-panel error-panel" role="alert">
      <p>{{ errorMessage }}</p>
      <button type="button" @click="loadValuations">重新加载</button>
    </section>

    <section v-else-if="valuations.length === 0" class="message-panel">
      暂无估值数据
    </section>

    <section v-else class="valuation-grid" aria-label="指数估值百分位">
      <article v-for="item in valuations" :key="item.index_code" class="valuation-card">
        <div class="card-heading">
          <div>
            <h2>{{ item.index_name }}</h2>
            <p>{{ item.index_code }}</p>
          </div>
          <span class="card-date">{{ item.data }}</span>
        </div>

        <div class="metric-list">
          <div v-for="metric in [
            { key: 'pe_percentile', label: 'PE 百分位' },
            { key: 'pb_percentile', label: 'PB 百分位' },
          ]" :key="metric.key" class="metric">
            <div class="metric-label">
              <span>{{ metric.label }}</span>
              <strong :class="statusClass(item[metric.key as 'pe_percentile' | 'pb_percentile'])">
                {{ percentage(item[metric.key as 'pe_percentile' | 'pb_percentile']) }}
              </strong>
            </div>
            <div class="bar-track" role="progressbar" aria-valuemin="0" aria-valuemax="100"
              :aria-valuenow="item[metric.key as 'pe_percentile' | 'pb_percentile'] * 100">
              <span class="bar-fill" :class="statusClass(item[metric.key as 'pe_percentile' | 'pb_percentile'])"
                :style="{ width: `${item[metric.key as 'pe_percentile' | 'pb_percentile'] * 100}%` }"></span>
            </div>
            <span class="metric-status" :class="statusClass(item[metric.key as 'pe_percentile' | 'pb_percentile'])">
              {{ statusLabel(item[metric.key as 'pe_percentile' | 'pb_percentile']) }}
            </span>
          </div>
        </div>
      </article>
    </section>

    <p class="page-note">百分位越高，代表当前估值在历史区间中的位置越高。</p>
  </main>
</template>

<style scoped>
.detail-page {
  min-height: 60vh;
  padding: 32px 0 20px;
}

.page-heading {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 24px;
  margin-bottom: 30px;
}

.eyebrow {
  margin: 0 0 10px;
  color: var(--accent-hover);
  font-size: 0.76rem;
  letter-spacing: 0.14em;
}

h1,
h2,
p {
  margin-top: 0;
}

h1 {
  margin-bottom: 10px;
  color: var(--text-strong);
  font-size: clamp(2rem, 5vw, 3.4rem);
}

.intro,
.updated-at,
.page-note {
  margin-bottom: 0;
  color: var(--text-muted);
  line-height: 1.7;
}

.updated-at {
  flex-shrink: 0;
  padding-bottom: 4px;
  font-size: 0.88rem;
}

.valuation-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
}

.valuation-card,
.message-panel {
  border: 1px solid var(--line-muted);
  border-radius: 14px;
  background: var(--bg-paper);
  box-shadow: 0 12px 28px rgba(0, 0, 0, 0.16);
}

.valuation-card {
  padding: 20px;
}

.card-heading {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  padding-bottom: 18px;
  border-bottom: 1px solid var(--line-soft);
}

.card-heading h2 {
  margin-bottom: 5px;
  color: var(--text-strong);
  font-size: 1.25rem;
}

.card-heading p,
.card-date {
  margin-bottom: 0;
  color: var(--text-muted);
  font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
  font-size: 0.76rem;
}

.card-date {
  white-space: nowrap;
}

.metric-list {
  display: grid;
  gap: 22px;
  padding-top: 22px;
}

.metric-label {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  margin-bottom: 9px;
  color: var(--text-main);
  font-size: 0.9rem;
}

.metric-label strong {
  font-size: 1.1rem;
}

.bar-track {
  height: 8px;
  overflow: hidden;
  border-radius: 999px;
  background: var(--bg-soft);
}

.bar-fill {
  display: block;
  height: 100%;
  border-radius: inherit;
  transition: width 500ms ease;
}

.metric-status {
  display: inline-block;
  margin-top: 8px;
  font-size: 0.76rem;
}

.status-low {
  color: var(--success);
}

.status-middle {
  color: var(--warning);
}

.status-high {
  color: var(--error);
}

.bar-fill.status-low {
  background: var(--success);
}

.bar-fill.status-middle {
  background: var(--warning);
}

.bar-fill.status-high {
  background: var(--error);
}

.page-note {
  margin-top: 20px;
  font-size: 0.86rem;
}

.message-panel {
  padding: 32px 24px;
  color: var(--text-main);
  text-align: center;
}

.message-panel p {
  margin-bottom: 16px;
}

button {
  border: 1px solid var(--line-muted);
  border-radius: 8px;
  padding: 8px 14px;
  background: transparent;
  color: var(--text-main);
  cursor: pointer;
  font: inherit;
}

button:hover {
  border-color: var(--accent-hover);
  color: var(--text-strong);
}

@media (max-width: 860px) {
  .valuation-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 640px) {
  .detail-page {
    padding-top: 20px;
  }

  .page-heading {
    display: block;
  }

  .updated-at {
    margin-top: 12px;
  }
}
</style>
