<template>
  <div class="telegram-view">
    <img
      src="@/assets/telegram-logo.svg"
      alt="telegram logo"
      width="100"
    />
    <telegram-form
      @submit="onSubmit"
    ></telegram-form>
    <analysis-sentiment-pie
      v-show="messages.length > 0"
      :items="messages"
    ></analysis-sentiment-pie>
    <telegram-channel-post
      v-for="post in messages"
      :key="post.id"
      class="shadow d-flex flex-column align-items-start m-4 p-3"
      :id="post.id"
      :date="post.date"
      :link="post.link"
      :sentiment="post.sentiment"
      :text="post.text"
      :views="post.views"
      :username="currentUser"
    ></telegram-channel-post>
    <b-button
      v-if="offsetId !== null && offsetId > 1"
      variant="secondary"
      @click="loadMore"
    > Load More </b-button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import TelegramChannelPost from '@/components/TelegramChannelPost'
import TelegramForm from '@/components/TelegramForm'
import AnalysisSentimentPie from '@/components/AnalysisSentimentPie'

export default {
  name: 'Telegram',
  components: {
    TelegramChannelPost,
    TelegramForm,
    AnalysisSentimentPie
  },
  data: function () {
    return {
      currentUser: null,
      offsetId: null,
      messages: []
    }
  },
  methods: {
    ...mapActions({
      getPosts: 'media/getTelegramPosts'
    }),
    setOffsetId () {
      if (this.messages.length !== 0) {
        this.offsetId = this.messages[this.messages.length - 1].id
      }
    },
    onSubmit (username) {
      this.offsetId = null
      this.currentUser = username

      this.getPosts({ username })
        .then(res => {
          this.messages = [...res.data.messages]
          this.setOffsetId()
        })
    },
    loadMore () {
      this.getPosts({ username: this.currentUser, offsetId: this.offsetId })
        .then(res => {
          this.messages = [...this.messages, ...res.data.messages]
          this.setOffsetId()
        })
    }
  }
}
</script>
