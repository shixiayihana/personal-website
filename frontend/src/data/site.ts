export type Project = {
  slug: string
  title: string
  description: string
  tag: string
  year: string
  month: string
  // href: string
}

export const siteProfile = {
  brand: 'Tang Studio',
  title: '一个简单有趣的个人网站',
  subtitle: 'Interesting Personal Website',
  intro: '基于Vue3，Ts，TailwindCSS构建',
  email: '2638645379@qq.com',
  bilibili: 'https://space.bilibili.com/476404207',
  github: 'https://github.com/shixiayihana',
}

export const projects: Project[] = [
  {
    slug: 'cn-index-percentile',
    title: 'A股分位观测站',
    description: '每日自动爬取A股主要宽基指数的估值数据。',
    tag: 'Tool',
    year: '2026',
    month: '08',
  },
  // {
  //   slug: 'notes-website',
  //   title: '个人随笔站',
  //   description: '沉淀技术与生活笔记，强调阅读舒适性与留白节奏。',
  //   tag: 'Writing',
  //   year: '2025',
  //   month: '05',
  // },
  // {
  //   slug: 'brand-landing',
  //   title: '品牌落地页',
  //   description: '为小型工作室设计复古风宣传页，突出质感与细节。',
  //   tag: 'Design',
  //   year: '2024',
  //   month: '11',
  // },
]
