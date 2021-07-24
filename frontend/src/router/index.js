import Vue from 'vue'
import VueRouter from 'vue-router'
import BaseLayout from '@/layouts/Base'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home'),
    meta: {
      layout: BaseLayout
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
