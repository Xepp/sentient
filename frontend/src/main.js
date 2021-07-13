import Vue from 'vue'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './scss/main.scss'

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)

Vue.config.productionTip = false

Vue.mixin({
  created () {
    console.log('[created] ' + this.$options.name)
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
