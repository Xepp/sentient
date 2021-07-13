<template>
  <card
    :variant="variant"
  >
    <div
      class="d-flex flex-row align-items-center w-100"
      style="color: #5F5F5F;"
    >
      <p class="m-0 border-left"> <b-badge dir="ltr" variant="transparent"> {{ user.name }} </b-badge> </p>
      <p class="m-0" dir="ltr"> {{ jalaliDate }} </p>
      <p class="m-0 mr-auto"> <b-badge dir="ltr" variant="transparent"> {{ `@${user.screen_name}` }} </b-badge> </p>
    </div>
    <div class="d-flex flex-row justify-content-start align-items-start">
      <img
        :src="tweetTypeIcon"
        width="64"
      />
      <p class="p-3 my-2"> {{ text }} </p>
    </div>
  </card>
</template>

<script>
import Card from '@/components/Card'
import TwitterTweetIcon from '@/assets/icon/twitter-tweet.svg'
import TwitterRetweetIcon from '@/assets/icon/twitter-retweet.svg'
import TwitterQuoteIcon from '@/assets/icon/twitter-quote.svg'
import TwitterReplayIcon from '@/assets/icon/twitter-replay.svg'

export default {
  name: 'TwitterFeedItem',
  components: {
    Card
  },
  props: {
    user: {
      type: Object,
      default: function () {
        return {
          avatar: null,
          description: '',
          followers_count: '',
          followings_count: '',
          id: null,
          name: '',
          screen_name: '',
          statuses_count: ''
        }
      }
    },
    createdAt: {
      type: String,
      required: true
    },
    favoriteCount: {
      type: Number,
      required: false,
      default: 0
    },
    id: {
      type: String,
      required: true
    },
    retweetCount: {
      type: Number,
      required: false,
      default: 0
    },
    sentiment: {
      type: String,
      required: false,
      default: 'unk'
    },
    text: {
      type: String,
      required: false,
      default: ''
    },
    tweetType: {
      type: String,
      required: false,
      default: 'tweet'
    }
  },
  computed: {
    variant: function () {
      return this.sentiment === 'pos' ? 'success' : this.sentiment === 'neg' ? 'danger' : 'info'
    },
    tweetTypeIcon: function () {
      return this.tweetType === 'retweet'
        ? TwitterRetweetIcon : this.tweetType === 'quote'
          ? TwitterQuoteIcon : this.tweetType === 'reply'
            ? TwitterReplayIcon : TwitterTweetIcon
    },
    jalaliDate: function () {
      return new Date(this.createdAt).toLocaleString('fa-IR')
    }
  }
}
</script>
