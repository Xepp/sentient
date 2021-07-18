const FilterMixin = {
  data: function () {
    return {
      filterKeyword: '',
      filterSentiment: ['neg', 'neu', 'pos']
    }
  },
  computed: {
    filteredItems () {
      return this.items.filter(item => {
        const keywordCondition = item.text && item.text.includes(this.filterKeyword)
        const sentimentCondition = this.filterSentiment.includes(item.sentiment)

        return keywordCondition && sentimentCondition
      })
    }
  }
}

export default FilterMixin
