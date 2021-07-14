const GeneralMixin = {
  computed: {
    sources () {
      return [
        { text: 'اینستاگرام', value: 'instagram', placeholder: 'link' },
        { text: 'تلگرام', value: 'telegram', placeholder: 'channel' },
        { text: 'توییتر', value: 'twitter', placeholder: 'username' },
        { text: 'خبرفوری', value: 'khabar-foori', placeholder: 'link' }
      ]
    }
  },
  methods: {
    getSourceText (source) {
      return this.sources.find((s) => s.value === source).text
    },
    getSourcePlaceholder (source) {
      return this.sources.find((s) => s.value === source).placeholder
    }
  }
}

export default GeneralMixin
