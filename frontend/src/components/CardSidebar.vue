<template>
  <div
    class="card-sidebar rounded-lg"
    :class="[bg]"
    style="width: 16px; border-top-left-radius: 0 !important; border-bottom-left-radius: 0 !important;"
  ></div>
</template>

<script>
export default {
  name: 'CardSidebar',
  props: {
    bg: {
      type: String,
      required: true
    }
  }
}
</script>
