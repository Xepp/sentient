import { mapActions } from 'vuex'
import { uniqBy } from 'lodash'

const TwitterMixin = {
  data: function () {
    return {
      twitterItems: [],
      twitterHasMore: false,
      twitterMaxId: null,
      twitterCurrentUser: null
    }
  },
  methods: {
    ...mapActions({
      getTwitterStatuses: 'media/getTwitterStatuses'
    }),
    setTwitterPagination () {
      if (this.twitterItems.length !== 0) {
        this.twitterMaxId = this.twitterItems[this.twitterItems.length - 1].id
      }
      this.twitterHasMore = this.twitterMaxId !== null
    },
    onTwitterSubmit (username) {
      this.twitterMaxId = null
      this.twitterCurrentUser = username

      this.getTwitterStatuses({ username })
        .then(res => {
          this.twitterItems = [...res.data.tweets]
          this.setTwitterPagination()
        })
    },
    onTwitterLoadMore () {
      this.getTwitterStatuses({ username: this.twitterCurrentUser, maxId: this.twitterMaxId })
        .then(res => {
          this.twitterItems = uniqBy([...this.twitterItems, ...res.data.tweets], 'id')
          this.setTwitterPagination()
        })
    }
  }
}

export default TwitterMixin
