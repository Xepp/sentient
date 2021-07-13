<template>
  <pie-chart
    v-if="hasData"
    :chartData="chartData"
    :options="options"
  ></pie-chart>
</template>

<script>
import PieChart from '@/components/PieChart'

export default {
  name: 'AnalysisSentiment',
  components: {
    PieChart
  },
  props: {
    items: {
      type: Array,
      required: true
    }
  },
  computed: {
    hasData () {
      return this.items.length > 0
    },
    chartData () {
      const pos = this.items.reduce((acc, cur) => cur.sentiment === 'pos' ? ++acc : acc, 0)
      const neu = this.items.reduce((acc, cur) => cur.sentiment === 'neu' ? ++acc : acc, 0)
      const neg = this.items.reduce((acc, cur) => cur.sentiment === 'neg' ? ++acc : acc, 0)

      return {
        labels: ['Pos', 'Neu', 'Neg'],
        datasets: [
          {
            backgroundColor: ['#00A676', '#ADB5BD', '#FF1F35'],
            data: [pos, neu, neg]
          }
        ]
      }
    },
    options () {
      return {
        responsive: true,
        maintainAspectRatio: false,
        onClick: this.handleClick
      }
    }
  },
  methods: {
    handleClick (point, event) {
      const item = event[0]
      console.log(item)
    }
  }
}
</script>
