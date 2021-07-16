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
          :items="filteredItems"
          :source="source"
        ></analysis-section>
      </b-col>
      <b-col sm="6">
        <result-section
          class="my-5"
          :source="source"
          :items="filteredItems"
          :has-more="hasMore"
          @load-more="loadMore"
        ></result-section>
      </b-col>
      <b-col sm="3">
        <filter-section
          class="mt-5"
          :keyword="filterKeyword"
          :selected-sentiment="filterSentiment"
          @filter-keyword="onFilterKeyword"
          @filter-sentiment="onFilterSentiment"
        ></filter-section>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { FilterMixin, TelegramMixin, TwitterMixin, KhabarFooriMixin } from '@/mixin'
import AnalysisSection from '@/components/AnalysisSection'
import QuerySection from '@/components/QuerySection'
import ResultSection from '@/components/ResultSection'
import FilterSection from '@/components/FilterSection'

export default {
  name: 'Search',
  components: {
    AnalysisSection,
    QuerySection,
    ResultSection,
    FilterSection
  },
  mixins: [FilterMixin, TelegramMixin, TwitterMixin, KhabarFooriMixin],
  data: function () {
    return {
      source: 'telegram'
    }
  },
  computed: {
    items () {
      if (this.source === 'telegram') return this.telegramItems
      else if (this.source === 'twitter') return this.twitterItems
      else if (this.source === 'khabar-foori') return this.khabarFooriItems
      return []
    },
    hasMore () {
      if (this.source === 'telegram') return this.telegramHasMore
      else if (this.source === 'twitter') return this.twitterHasMore
      return false
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
    },
    loadMore () {
      if (this.source === 'telegram') {
        this.onTelegramLoadMore()
      } else if (this.source === 'twitter') {
        this.onTwitterLoadMore()
      }
    },
    onFilterKeyword (keyword) {
      this.filterKeyword = keyword
    },
    onFilterSentiment (selectedSentiment) {
      this.filterSentiment = [...selectedSentiment]
    }
  }
}

</script>
