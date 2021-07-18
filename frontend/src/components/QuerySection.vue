<template>
  <div
    class="query-section mx-auto position-sticky bg-white"
    style="direction: rtl; max-width: fit-content; top: 0px; height: 150px; z-index: 999;"
  >
    <b-form
      class="justify-content-center py-5"
      inline
    >
      <b-input-group
        class="ml-2"
        style="direction: ltr;"
      >
        <template #prepend>
          <b-input-group-text>
            <b-icon :icon="prependIcon"></b-icon>
          </b-input-group-text>
        </template>
        <template #append>
          <b-dropdown
            style="width: 140px;"
            :text="getSourceText(source)"
            :variant="source"
            split
            block
          >
            <b-dropdown-item
              v-for="item in sources"
              :key="item.value"
              @click="change(item.value)"
            > {{ item.text }} </b-dropdown-item>
          </b-dropdown>
        </template>
        <b-form-input
          v-model="input"
          style="min-width: 360px;"
          id="link-input"
          :placeholder="getSourcePlaceholder(source)"
        ></b-form-input>
      </b-input-group>
      <b-button
        style="width: 150px;"
        variant="primary"
        @click="submit"
      > جست و جو </b-button>
    </b-form>
  </div>
</template>

<script>
import { QueryMixin } from '@/mixin'

export default {
  name: 'QuerySection',
  mixins: [QueryMixin],
  props: {
    source: {
      type: String,
      required: true
    }
  },
  data: function () {
    return {
      input: ''
    }
  },
  computed: {
    prependIcon () {
      return ['telegram', 'twitter'].includes(this.source) ? 'person' : 'link45deg'
    }
  },
  methods: {
    change (s) {
      if (s !== this.source) {
        this.$emit('change', s)
        this.input = ''
      }
    },
    submit () {
      this.$emit('submit', this.source, this.input)
    }
  }

}
</script>
