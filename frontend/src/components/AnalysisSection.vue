<template>
  <div
    class="position-sticky"
    style="top: 200px;"
  >
    <analysis-sentiment
      :items="items"
    ></analysis-sentiment>
    <analysis-statistics
      :items="items"
    ></analysis-statistics>
  </div>
</template>

<script>
import AnalysisSentiment from '@/components/AnalysisSentiment'
import AnalysisStatistics from '@/components/AnalysisStatistics'

export default {
  name: 'AnalysisSection',
  components: {
    AnalysisSentiment,
    AnalysisStatistics
  },
  props: {
    items: {
      type: Array,
      required: false,
      default: () => []
    }
  }
}
</script>
