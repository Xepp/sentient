<template>
  <div
    class="twitter-form mx-auto my-4"
    style="direction: rtl; max-width: fit-content;"
  >
    <b-form
      class="justify-content-center"
      inline
    >
      <b-input-group
        class="ml-2"
        style="direction: ltr;"
        prepend="@"
      >
        <b-form-input
          v-model="username"
          style="min-width: 360px;"
          id="link-input"
          placeholder="username"
        ></b-form-input>
      </b-input-group>
      <b-button
        variant="primary"
        @click="onSubmit"
      > Submit </b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  name: 'TwitterForm',
  data: function () {
    return {
      username: ''
    }
  },
  methods: {
    onSubmit: function () {
      this.$emit('submit', this.username)
      this.username = ''
    }
  }
}
</script>
