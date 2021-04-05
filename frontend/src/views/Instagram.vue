<template>
  <div class="instagram-view">
    <img
      src="@/assets/instagram-logo.svg"
      alt="instagram logo"
      width="100"
    />
    <instagram-form
      @submit="onSubmit"
    ></instagram-form>
    <analysis-sentiment-pie
      v-show="comments.length > 0"
      :items="comments"
    ></analysis-sentiment-pie>
    <instagram-post-comment
      v-for="comment in comments"
      :key="comment.id"
      class="shadow d-flex flex-column align-items-start m-4 p-3"
      :id="comment.id"
      :sentiment="comment.sentiment"
      :text="comment.text"
      :username="comment.username"
      :created-at="comment.created_at"
    ></instagram-post-comment>
    <b-button
      v-if="hasNextPage"
      variant="secondary"
      @click="loadMore"
    > Load More </b-button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import InstagramPostComment from '@/components/InstagramPostComment'
import InstagramForm from '@/components/InstagramForm'
import AnalysisSentimentPie from '@/components/AnalysisSentimentPie'

export default {
  name: 'Instagram',
  components: {
    InstagramPostComment,
    InstagramForm,
    AnalysisSentimentPie
  },
  data: function () {
    return {
      shortcode: null,
      endCursor: null,
      hasNextPage: false,
      comments: []
    }
  },
  methods: {
    ...mapActions({
      getComments: 'media/getInstagramComments'
    }),
    getShortcode (url) {
      const match = /^(?:.*\/p\/)([\d\w\-_]+)/.exec(url)
      if (match === null) return null
      return match[1]
    },
    onSubmit (url) {
      this.endCursor = null
      this.hasNextPage = false
      this.shortcode = this.getShortcode(url)

      this.getComments({ shortcode: this.shortcode })
        .then(res => {
          this.comments = [...res.data.comments]
          this.endCursor = res.data.new_end_cursor
          this.hasNextPage = res.data.has_next_page
        })
    },
    loadMore () {
      this.getComments({ shortcode: this.shortcode, endCursor: this.endCursor })
        .then(res => {
          this.comments = [...this.comments, ...res.data.comments]
          this.endCursor = res.data.new_end_cursor
          this.hasNextPage = res.data.has_next_page
        })
    }
  }
}
</script>
