import Vue from 'vue'
import VueRouter from 'vue-router'
import BaseLayout from '@/layouts/Base'
import PanelLayout from '@/layouts/Panel'
import Home from '@/views/Home'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      layout: BaseLayout
    }
  },
  {
    path: '/khabar-foori',
    name: 'KhabarFoori',
    component: () => import('@/views/KhabarFoori'),
    meta: {
      layout: PanelLayout
    }
  },
  {
    path: '/instagram',
    name: 'Instagram',
    component: () => import('@/views/Instagram'),
    meta: {
      layout: PanelLayout
    }
  },
  {
    path: '/twitter',
    name: 'Twitter',
    component: () => import('@/views/Twitter'),
    meta: {
      layout: PanelLayout
    }
  },
  {
    path: '/telegram',
    name: 'Telegram',
    component: () => import('@/views/Telegram'),
    meta: {
      layout: PanelLayout
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
