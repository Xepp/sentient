import { mapActions } from 'vuex'

const KhabarFooriMixin = {
  data: function () {
    return {
      khabarFooriItems: []
    }
  },
  methods: {
    ...mapActions({
      getKhabarFooriComments: 'media/getKhabarFooriComments'
    }),
    onKhabarFooriSubmit (url) {
      this.getKhabarFooriComments({ url })
        .then(res => {
          this.khabarFooriItems = [...res.data.comments]
        })
    }
  }
}

export default KhabarFooriMixin
