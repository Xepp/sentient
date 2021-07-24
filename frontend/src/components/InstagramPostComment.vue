<template>
  <card
    :variant="variant"
  >
    <div
      class="d-flex flex-row align-items-center w-100"
      style="color: #5F5F5F;"
    >
      <p class="m-0 border-left"> <b-badge dir="ltr" variant="transparent"> {{ username }} </b-badge> </p>
      <p class="m-0" dir="ltr"> {{ jalaliDate }} </p>
    </div>
    <p class="p-3 my-2"> {{ text }} </p>
  </card>
</template>

<script>
import Card from '@/components/Card'

export default {
  name: 'InstagramPostComment',
  components: {
    Card
  },
  props: {
    createdAt: {
      type: Number,
      required: true
    },
    id: {
      type: String,
      required: true
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
    },
    username: {
      type: String,
      required: false,
      default: ''
    }
  },
  computed: {
    variant: function () {
      return this.sentiment === 'pos' ? 'success' : this.sentiment === 'neg' ? 'danger' : 'info'
    },
    jalaliDate: function () {
      return new Date(this.createdAt * 1000).toLocaleString('fa-IR')
    }
  }
}
</script>
