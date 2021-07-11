<template>
  <div
    class="position-sticky"
    style="top: 0;"
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
