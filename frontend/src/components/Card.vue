<template>
  <div class="d-flex flex-row align-items stretch rounded-lg bg-light">
    <div
      class="d-flex flex-column align-items-start p-3"
      style="direction: rtl; width: 504px;"
    >
      <slot></slot>
    </div>
    <card-sidebar
      :bg="`bg-${variant}`"
    ></card-sidebar>
  </div>
</template>

<script>
import CardSidebar from '@/components/CardSidebar'

export default {
  name: 'Card',
  components: {
    CardSidebar
  },
  props: {
    variant: {
      type: String,
      required: false,
      default: 'info'
    }
  }
}
</script>
