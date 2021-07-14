<template>
  <div
    class="position-sticky"
    style="top: 150px;"
  >
    <analysis-sentiment
      :items="items"
    ></analysis-sentiment>
  </div>
</template>

<script>
import AnalysisSentiment from '@/components/AnalysisSentiment'

export default {
  name: 'AnalysisSection',
  components: {
    AnalysisSentiment
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
