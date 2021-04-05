<template>
  <div class="panel-layout">
    <Sidebar></Sidebar>
    <slot></slot>
  </div>
</template>

<script>
import Sidebar from '@/components/Sidebar'

export default {
  name: 'PanelLayout',
  components: {
    Sidebar
  }
}
</script>
