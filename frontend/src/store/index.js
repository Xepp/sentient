import Vue from 'vue'
import Vuex from 'vuex'
import media from '@/store/media'

Vue.use(Vuex)

export default new Vuex.Store({
  strict: true,
  modules: {
    media
  }
})
