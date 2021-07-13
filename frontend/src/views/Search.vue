<template>
  <b-container class="search-view">
    <query-section
      class="mt-5"
      :source="source"
      @change="changeSource"
      @submit="submit"
    ></query-section>
    <b-row>
      <b-col sm="3">
        <analysis-section
          class="mt-5"
          :items="items"
          :source="source"
        ></analysis-section>
      </b-col>
      <b-col sm="9">
        <result-section
          class="my-5"
          :source="source"
          :items="items"
          :has-more="hasMore"
          @load-more="loadMore"
        ></result-section>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { TelegramMixin, TwitterMixin, KhabarFooriMixin } from '@/mixin'
import AnalysisSection from '@/components/AnalysisSection'
import QuerySection from '@/components/QuerySection'
import ResultSection from '@/components/ResultSection'

export default {
  name: 'Search',
  components: {
    AnalysisSection,
    QuerySection,
    ResultSection
  },
  mixins: [TelegramMixin, TwitterMixin, KhabarFooriMixin],
  data: function () {
    return {
      source: 'telegram',
      items: [],
      hasMore: false
    }
  },
  methods: {
    submit (source, input) {
      if (source === 'telegram') {
        this.onTelegramSubmit(input)
      } else if (source === 'twitter') {
        this.onTwitterSubmit(input)
      } else if (source === 'khabar-foori') {
        this.onKhabarFooriSubmit(input)
      }
    },
    changeSource (source) {
      this.source = source
      this.items = []
      this.hasMore = false
    },
    loadMore () {
      if (this.source === 'telegram') {
        this.onTelegramLoadMore()
      } else if (this.source === 'twitter') {
        this.onTwitterLoadMore()
      }
    }
  }
}

</script>
