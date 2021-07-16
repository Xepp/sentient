<template>
  <div
    class="d-flex flex-column rounded-lg border border-secondary justify-content-center p-3"
    style="height: 160px;"
  >
    <h5 class="text-primary"> تعداد نتایج </h5>
    <h1 class="my-2"> {{ count.total }} </h1>
    <div class="d-flex flex-row justify-content-around mx-5">
      <h5 class="text-success"> {{ count.pos }} </h5>
      <h5 class="text-info"> {{ count.neu }} </h5>
      <h5 class="text-danger"> {{ count.neg }} </h5>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AnalysisStatistics',
  props: {
    items: {
      type: Array,
      required: true
    }
  },
  computed: {
    count () {
      const pos = this.items.reduce((acc, cur) => cur.sentiment === 'pos' ? ++acc : acc, 0)
      const neu = this.items.reduce((acc, cur) => cur.sentiment === 'neu' ? ++acc : acc, 0)
      const neg = this.items.reduce((acc, cur) => cur.sentiment === 'neg' ? ++acc : acc, 0)
      const total = this.items.length

      return {
        total,
        pos,
        neg,
        neu
      }
    }
  }
}
</script>
