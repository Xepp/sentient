<template>
  <card
    :variant="variant"
  >
    <div
      class="d-flex flex-row align-items-center w-100"
      style="color: #5F5F5F;"
    >
      <p class="m-0 border-left"> <b-badge dir="ltr" variant="transparent"> {{ author }} </b-badge> </p>
      <p class="m-0" dir="ltr"> {{ date }} </p>
    </div>
    <p class="p-3 my-2"> {{ text }} </p>
  </card>
</template>

<script>
import Card from '@/components/Card'

export default {
  name: 'KhabarFooriFeedComment',
  components: {
    Card
  },
  props: {
    author: {
      type: String,
      required: false,
      default: ''
    },
    date: {
      type: String,
      required: false,
      default: ''
    },
    likeCount: {
      type: String,
      required: false,
      default: '0'
    },
    dislikeCount: {
      type: String,
      required: false,
      default: '0'
    },
    sentiment: {
      type: String,
      required: false,
      default: 'unk'
    },
    text: {
      type: String,
      required: false,
      default: ''
    }
  },
  computed: {
    variant: function () {
      return this.sentiment === 'pos' ? 'success' : this.sentiment === 'neg' ? 'danger' : 'info'
    }
  }
}
</script>
