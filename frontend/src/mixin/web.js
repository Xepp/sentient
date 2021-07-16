import { mapActions } from 'vuex'

const KhabarFooriMixin = {
  data: function () {
    return {
      khabarFooriItems: [],
      khabarFooriZeroState: true
    }
  },
  methods: {
    ...mapActions({
      getKhabarFooriComments: 'media/getKhabarFooriComments'
    }),
    onKhabarFooriSubmit (url) {
      this.loadingState = true
      this.getKhabarFooriComments({ url })
        .then(res => {
          this.khabarFooriItems = [...res.data.comments]
          if (this.khabarFooriZeroState) this.khabarFooriZeroState = false
        })
        .finally(() => {
          this.loadingState = false
        })
    }
  }
}

export default KhabarFooriMixin
