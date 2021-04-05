<template>
  <div class="khabar-foori-view">
    <img
      src="@/assets/khabar-foori-logo.png"
      alt="khabar foori logo"
      width="100"
    />
    <khabar-foori-form
      @submit="onSubmit"
    ></khabar-foori-form>
    <analysis-sentiment-pie
      v-show="comments.length > 0"
      :items="comments"
    ></analysis-sentiment-pie>
    <khabar-foori-feed-comment
      v-for="(comment, index) in comments"
      :key="index"
      class="shadow d-flex flex-column align-items-start m-4 p-3"
      :author="comment.author"
      :date="comment.date"
      :like-count="comment.pos"
      :dislike-count="comment.neg"
      :sentiment="comment.sentiment"
      :text="comment.text"
    ></khabar-foori-feed-comment>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import KhabarFooriFeedComment from '@/components/KhabarFooriFeedComment'
import KhabarFooriForm from '@/components/KhabarFooriForm'
import AnalysisSentimentPie from '@/components/AnalysisSentimentPie'

export default {
  name: 'KhabarFoori',
  components: {
    KhabarFooriFeedComment,
    KhabarFooriForm,
    AnalysisSentimentPie
  },
  data: function () {
    return {
      comments: []
    }
  },
  methods: {
    ...mapActions({
      getComments: 'media/getKhabarFooriComments'
    }),
    onSubmit (url) {
      this.getComments({ url })
        .then(res => {
          this.comments = res.data.comments
        })
    }
  }
}
</script>
