<template>
  <b-container class="khabar-foori-view">
    <b-row>
      <b-col sm="3">
        <analysis-section
          class="mt-5"
          :items="comments"
        ></analysis-section>
      </b-col>
      <b-col sm="9">
        <khabar-foori-form
          @submit="onSubmit"
        ></khabar-foori-form>
        <khabar-foori-feed-comment
          v-for="(comment, index) in comments"
          :key="index"
          class="shadow my-4 mx-auto"
          style="width: 560px; min-height: 260px;"
          :author="comment.author"
          :date="comment.date"
          :like-count="comment.pos"
          :dislike-count="comment.neg"
          :sentiment="comment.sentiment"
          :text="comment.text"
        ></khabar-foori-feed-comment>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { mapActions } from 'vuex'
import KhabarFooriFeedComment from '@/components/KhabarFooriFeedComment'
import KhabarFooriForm from '@/components/KhabarFooriForm'
import AnalysisSection from '@/components/AnalysisSection'

export default {
  name: 'KhabarFoori',
  components: {
    KhabarFooriFeedComment,
    KhabarFooriForm,
    AnalysisSection
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
