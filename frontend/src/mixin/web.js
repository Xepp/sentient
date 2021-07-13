import { mapActions } from 'vuex'

const KhabarFooriMixin = {
  methods: {
    ...mapActions({
      getKhabarFooriComments: 'media/getKhabarFooriComments'
    }),
    onKhabarFooriSubmit (url) {
      this.getKhabarFooriComments({ url })
        .then(res => {
          this.items = [...res.data.comments]
        })
    }
  }
}

export default KhabarFooriMixin
