<template>
  <b-container class="twitter-view">
    <b-row>
      <b-col sm="3">
        <analysis-section
          class="mt-5"
          :items="statuses"
        ></analysis-section>
      </b-col>
      <b-col sm="9">
        <twitter-form
          @submit="onSubmit"
        ></twitter-form>
        <twitter-feed-item
          v-for="item in statuses"
          :key="item.id"
          class="shadow my-4 mx-auto"
          style="width: 560px; min-height: 260px;"
          :user="item.user"
          :created-at="item.created_at"
          :id="item.id"
          :favorite-count="item.favorite_count"
          :retweet-count="item.retweet_count"
          :sentiment="item.sentiment"
          :text="item.text"
          :tweet-type="item.type"
        ></twitter-feed-item>
        <b-button
          v-if="maxId !== null"
          variant="secondary"
          @click="loadMore"
        > Load More </b-button>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { mapActions } from 'vuex'
import { uniqBy } from 'lodash'
import TwitterFeedItem from '@/components/TwitterFeedItem'
import TwitterForm from '@/components/TwitterForm'
import AnalysisSection from '@/components/AnalysisSection'

export default {
  name: 'Twitter',
  components: {
    TwitterFeedItem,
    TwitterForm,
    AnalysisSection
  },
  data: function () {
    return {
      currentUser: null,
      maxId: null,
      statuses: []
    }
  },
  methods: {
    ...mapActions({
      getStatuses: 'media/getTwitterStatuses'
    }),
    setMaxId () {
      if (this.statuses.length !== 0) {
        this.maxId = this.statuses[this.statuses.length - 1].id
      }
    },
    onSubmit (username) {
      this.maxId = null
      this.currentUser = username

      this.getStatuses({ username })
        .then(res => {
          this.statuses = [...res.data.tweets]
          this.setMaxId()
        })
    },
    loadMore () {
      this.getStatuses({ username: this.currentUser, maxId: this.maxId })
        .then(res => {
          this.statuses = uniqBy([...this.statuses, ...res.data.tweets], 'id')
          this.setMaxId()
        })
    }
  }
}
</script>
