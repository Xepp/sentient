<template>
  <vue-chartist
    :data="data"
    :options="options"
    type="Pie"
  ></vue-chartist>
</template>

<script>
import VueChartist from 'v-chartist'

export default {
  name: 'AnalysisSentimentPie',
  components: {
    VueChartist
  },
  props: {
    items: {
      type: Array,
      required: true
    }
  },
  computed: {
    data () {
      const pos = this.items.reduce((acc, cur) => cur.sentiment === 'pos' ? ++acc : acc, 0)
      const neu = this.items.reduce((acc, cur) => cur.sentiment === 'neu' ? ++acc : acc, 0)
      const neg = this.items.reduce((acc, cur) => cur.sentiment === 'neg' ? ++acc : acc, 0)

      const res = {
        series: [pos, neu, neg],
        labels: ['Pos', 'Neu', 'Neg']
      }

      return res
    },
    options () {
      return {
        donut: true,
        width: '270px',
        height: '270px',
        donutWidth: 50,
        startAngle: 270,
        donutSolid: true,
        showLabel: false
      }
    }
  }
}
</script>
