<template>
  <b-container class="search-view">
    <query-section
      class="mt-5"
      :source="source"
      @change="changeSource"
      @submit="submit"
    ></query-section>
    <b-overlay
      :show="loadingState"
      variant="white"
      opacity="0.8"
      blur="5px"
    >
      <template #overlay>
        <div class="d-flex align-items-center">
          <b-spinner small type="grow" variant="dark"></b-spinner>
          <b-spinner type="grow" variant="dark"></b-spinner>
          <b-spinner small type="grow" variant="dark"></b-spinner>
          <!-- We add an SR only text for screen readers -->
          <span class="sr-only">Please wait...</span>
        </div>
      </template>
      <b-alert
        v-if="zeroState"
        class="mx-auto rounded"
        style="max-width: 640px;"
        show
        variant="secondary"
      >
        <p> برای شروع لطفا فضای مورد نظر را انتخاب کرده و پرسمان خود را جستجو کنید </p>
        <hr>
        <h4> {{ alertBox.title }} </h4>
        <p> {{ alertBox.info }} </p>
      </b-alert>
      <b-row v-else>
        <b-col sm="3">
          <analysis-section
            class="mt-5"
            :items="filteredItems"
            :source="source"
          ></analysis-section>
        </b-col>
        <b-col sm="6">
          <result-section
            class="my-5"
            :source="source"
            :items="filteredItems"
            :has-more="hasMore"
            @load-more="loadMore"
          ></result-section>
        </b-col>
        <b-col sm="3">
          <filter-section
            class="mt-5"
            :keyword="filterKeyword"
            :selected-sentiment="filterSentiment"
            @filter-keyword="onFilterKeyword"
            @filter-sentiment="onFilterSentiment"
          ></filter-section>
        </b-col>
      </b-row>
    </b-overlay>
  </b-container>
</template>

<script>
import { GeneralMixin, FilterMixin, TelegramMixin, TwitterMixin, KhabarFooriMixin } from '@/mixin'
import AnalysisSection from '@/components/AnalysisSection'
import QuerySection from '@/components/QuerySection'
import ResultSection from '@/components/ResultSection'
import FilterSection from '@/components/FilterSection'

export default {
  name: 'Search',
  components: {
    AnalysisSection,
    QuerySection,
    ResultSection,
    FilterSection
  },
  mixins: [GeneralMixin, FilterMixin, TelegramMixin, TwitterMixin, KhabarFooriMixin],
  data: function () {
    return {
      source: 'telegram'
    }
  },
  computed: {
    items () {
      if (this.source === 'telegram') return this.telegramItems
      else if (this.source === 'twitter') return this.twitterItems
      else if (this.source === 'khabar-foori') return this.khabarFooriItems
      return []
    },
    hasMore () {
      if (this.source === 'telegram') return this.telegramHasMore
      else if (this.source === 'twitter') return this.twitterHasMore
      return false
    },
    alertBox () {
      const content = {
        telegram: {
          title: 'فضای پیامرسان تلگرام',
          info: 'شما می توانید با وارد کردن آیدی یک کانال عمومی تلگرام پیام های آن را رصد کنید'
        },
        twitter: {
          title: 'فضای شبکه اجتماعی توییتر',
          info: 'شما می توانید با وارد کردن آیدی یک اکانت عمومی در توییتر توییت های آن را رصد و بررسی کنید'
        },
        'khabar-foori': {
          title: 'وبسایت خبر فوری',
          info: 'شما می توانید با وارد کردن لینک جزییات یک پست در وبسایت خبر فوری نظرات ارسالی را بررسی کنید'
        },
        instagram: {
          title: 'فضای شبکه مجازی اینستاگرام',
          info: 'شما می توانید با وارد کردن لینک آدرس یک پست اینستاگرام نظرات آن پست را تحلیل و بررسی کنید'
        }
      }

      return content[this.source]
    }
  },
  methods: {
    submit (source, input) {
      if (source === 'telegram') {
        this.onTelegramSubmit(input)
      } else if (source === 'twitter') {
        this.onTwitterSubmit(input)
      } else if (source === 'khabar-foori') {
        this.onKhabarFooriSubmit(input)
      }
    },
    changeSource (source) {
      this.source = source
    },
    loadMore () {
      if (this.source === 'telegram') {
        this.onTelegramLoadMore()
      } else if (this.source === 'twitter') {
        this.onTwitterLoadMore()
      }
    },
    onFilterKeyword (keyword) {
      this.filterKeyword = keyword
    },
    onFilterSentiment (selectedSentiment) {
      this.filterSentiment = [...selectedSentiment]
    }
  }
}

</script>
