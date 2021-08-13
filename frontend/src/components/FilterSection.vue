<template>
  <div
    class="position-sticky"
    style="top: 200px;"
  >
    <b-input-group
      size="sm"
    >
      <template #append>
        <b-input-group-text>
          <b-icon icon="search"></b-icon>
        </b-input-group-text>
      </template>
      <b-form-input
        :value="keyword"
        type="text"
        size="sm"
        dir="rtl"
        @input="(v) => $emit('filter-keyword', v)"
      ></b-form-input>
    </b-input-group>
    <b-form-group
      class="my-5"
      v-slot="{ ariaDescribedby }"
    >
      <b-form-checkbox-group
        :checked="selectedSentiment"
        :aria-describedby="ariaDescribedby"
        buttons
        size="lg"
        name="buttons-2"
        @input="(v) => $emit('filter-sentiment', v)"
      >
        <b-form-checkbox
          v-for="option in sentimentOptions"
          :key="option.key"
          :class="option.class"
          :value="option.key"
          :button-variant="`outline-${option.variant}`"
        >
          <b-icon
            :variant="option.active ? 'light' : 'dark'"
            :icon="option.icon"
          ></b-icon>
        </b-form-checkbox>
      </b-form-checkbox-group>
    </b-form-group>
  </div>
</template>

<script>
export default {
  name: 'FilterSection',
  props: {
    keyword: {
      type: String,
      required: true
    },
    selectedSentiment: {
      type: Array,
      required: true
    }
  },
  computed: {
    sentimentOptions () {
      return [
        {
          key: 'neg',
          icon: 'emoji-frown',
          variant: 'danger',
          class: ['rounded-left'],
          active: this.selectedSentiment.includes('neg')
        },
        {
          key: 'neu',
          icon: 'emoji-neutral',
          variant: 'info',
          class: [],
          active: this.selectedSentiment.includes('neu')
        },
        {
          key: 'pos',
          icon: 'emoji-smile',
          variant: 'success',
          class: ['rounded-right'],
          active: this.selectedSentiment.includes('pos')
        }
      ]
    }
  }
}
</script>
