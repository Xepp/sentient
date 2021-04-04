<template>
  <div class="twitter-view">
    <img
      src="@/assets/twitter-logo.svg"
      alt="twitter logo"
      width="100"
    />
    <twitter-form
      @submit="onSubmit"
    ></twitter-form>
    <twitter-feed-item
      v-for="item in statuses"
      :key="item.id"
      class="shadow d-flex flex-column align-items-start m-4 p-3"
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
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import { uniqBy } from 'lodash'
import TwitterFeedItem from '@/components/TwitterFeedItem'
import TwitterForm from '@/components/TwitterForm'

export default {
  name: 'Twitter',
  components: {
    TwitterFeedItem,
    TwitterForm
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
