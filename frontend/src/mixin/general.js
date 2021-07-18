const GeneralMixin = {
  data: function () {
    return {
      loadingState: false
    }
  },
  computed: {
    zeroState () {
      if (this.source === 'telegram') return this.telegramZeroState
      else if (this.source === 'twitter') return this.twitterZeroState
      else if (this.source === 'khabar-foori') return this.khabarFooriZeroState

      return true
    }
  }
}

export default GeneralMixin
