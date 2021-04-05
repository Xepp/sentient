<template>
  <div
    class="twitter-feed-item rounded-lg"
    style="direction: rtl"
  >
    <div class="d-flex flex-row justify-content-between w-100">
      <p class="m-0"> <small> {{ user.name }} </small> <b-badge dir="ltr"> {{ `@${user.screen_name}` }} </b-badge> </p>
      <b-icon
        :icon="sentiment === 'pos' ? 'emoji-smile' : sentiment === 'neg' ? 'emoji-frown' : sentiment === 'neu' ? 'emoji-neutral' : 'question-circle'"
        :variant="sentiment === 'pos' ? 'success' : sentiment === 'neg' ? 'danger' : sentiment === 'neu' ? 'secondary' : 'dark'"
        font-scale="3"
      ></b-icon>
    </div>
    <div
      class="d-flex flex-row justify-content-start jumbotron border p-0 my-2"
      :class="[sentiment === 'pos' ? 'border-success' : sentiment === 'neg' ? 'border-danger' : 'border-secondary']"
    >
      <img
        :src="tweetTypeIcon"
        width="64"
      />
      <p class="p-3 my-2"> {{ text }} </p>
    </div>
    <p class="m-0"> <small> {{ createdAt }} </small> </p>
  </div>
</template>

<script>
import TwitterTweetIcon from '@/assets/icon/twitter-tweet.svg'
import TwitterRetweetIcon from '@/assets/icon/twitter-retweet.svg'
import TwitterQuoteIcon from '@/assets/icon/twitter-quote.svg'
import TwitterReplayIcon from '@/assets/icon/twitter-replay.svg'

export default {
  name: 'TwitterFeedItem',
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
    tweetTypeIcon () {
      if (this.tweetType === 'tweet') {
        return TwitterTweetIcon
      } else if (this.tweetType === 'retweet') {
        return TwitterRetweetIcon
      } else if (this.tweetType === 'quote') {
        return TwitterQuoteIcon
      } else if (this.tweetType === 'replay') {
        return TwitterReplayIcon
      }
      return TwitterTweetIcon
    }
  }
}
</script>
