<template>
  <card
    :variant="variant"
  >
    <div
      class="d-flex flex-row align-items-center w-100"
      style="color: #5F5F5F;"
    >
      <p class="m-0 border-left"> <b-badge dir="rtl" variant="transparent"> {{ channelTitle }} </b-badge> </p>
      <p class="m-0" dir="ltr"> {{ jalaliDate }} </p>
      <p class="m-0 mr-auto"> <b-badge dir="ltr" variant="transparent"> {{ `@${channelUsername}` }} </b-badge> </p>
    </div>
    <p class="p-3 my-2"> {{ text }} </p>
  </card>
</template>

<script>
import Card from '@/components/Card'

export default {
  name: 'TelegramChannelPost',
  components: {
    Card
  },
  props: {
    date: {
      type: Number,
      required: true
    },
    id: {
      type: Number,
      required: true
    },
    link: {
      type: String,
      required: false
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
    views: {
      type: Number,
      required: false,
      default: 1
    },
    channelUsername: {
      type: String,
      required: false,
      default: ''
    },
    channelTitle: {
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
      return new Date(this.date * 1000).toLocaleString('fa-IR')
    }
  }
}
</script>
