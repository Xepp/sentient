<template>
  <div
    class="instagram-post-comment rounded-lg"
    style="direction: rtl"
  >
    <div class="d-flex flex-row justify-content-between w-100">
      <p class="m-0"> <small> {{ username }} </small> </p>
      <b-icon
        :icon="sentiment === 'pos' ? 'emoji-smile' : sentiment === 'neg' ? 'emoji-frown' : sentiment === 'neu' ? 'emoji-neutral' : 'question-circle'"
        :variant="sentiment === 'pos' ? 'success' : sentiment === 'neg' ? 'danger' : sentiment === 'neu' ? 'secondary' : 'dark'"
        font-scale="3"
      ></b-icon>
    </div>
    <div
      class="d-flex flex-row justify-content-start jumbotron border p-0 my-2"
      :class="[sentiment === 'pos' ? 'border-success' : sentiment === 'neg' ? 'border-danger' : 'border-secondary']"
    >
      <p class="p-3 my-2"> {{ text }} </p>
    </div>
    <p class="m-0"> <small> {{ createdAt }} </small> </p>
  </div>
</template>

<script>
export default {
  name: 'InstagramPostComment',
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
  }
}
</script>
