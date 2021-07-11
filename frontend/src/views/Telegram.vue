<template>
  <b-container class="telegram-view">
    <b-row>
      <b-col sm="3">
        <analysis-section
          class="mt-5"
          :items="messages"
        ></analysis-section>
      </b-col>
      <b-col sm="9">
        <telegram-form
          @submit="onSubmit"
        ></telegram-form>
        <telegram-channel-post
          v-for="post in messages"
          :key="post.id"
          class="shadow my-4 mx-auto"
          style="width: 560px; min-height: 260px;"
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
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { mapActions } from 'vuex'
import TelegramChannelPost from '@/components/TelegramChannelPost'
import TelegramForm from '@/components/TelegramForm'
import AnalysisSection from '@/components/AnalysisSection'

export default {
  name: 'Telegram',
  components: {
    TelegramChannelPost,
    TelegramForm,
    AnalysisSection
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
