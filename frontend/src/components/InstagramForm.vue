<template>
  <div
    class="instagram-form mx-auto my-4"
    style="direction: rtl; max-width: fit-content;"
  >
    <b-form
      class="justify-content-center"
      inline
    >
      <b-form-input
        v-model="link"
        class="ml-2"
        style="min-width: 360px; direction: ltr;"
        id="link-input"
        placeholder="link"
      ></b-form-input>
      <b-button
        variant="primary"
        @click="onSubmit"
      > Submit </b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  name: 'InstagramForm',
  data: function () {
    return {
      link: ''
    }
  },
  methods: {
    onSubmit: function () {
      this.$emit('submit', this.link)
      this.link = ''
    }
  }
}
</script>
