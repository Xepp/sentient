import { mapActions } from 'vuex'
import { uniqBy } from 'lodash'

const TwitterMixin = {
  data: function () {
    return {
      twitterMaxId: null,
      twitterCurrentUser: null
    }
  },
  methods: {
    ...mapActions({
      getTwitterStatuses: 'media/getTwitterStatuses'
    }),
    setTwitterPagination () {
      if (this.items.length !== 0) {
        this.twitterMaxId = this.items[this.items.length - 1].id
      }
      this.hasMore = this.twitterMaxId !== null
    },
    onTwitterSubmit (username) {
      this.twitterMaxId = null
      this.twitterCurrentUser = username

      this.getTwitterStatuses({ username })
        .then(res => {
          this.items = [...res.data.tweets]
          this.setTwitterPagination()
        })
    },
    onTwitterLoadMore () {
      this.getTwitterStatuses({ username: this.twitterCurrentUser, maxId: this.twitterMaxId })
        .then(res => {
          this.items = uniqBy([...this.items, ...res.data.tweets], 'id')
          this.setTwitterPagination()
        })
    }
  }
}

export default TwitterMixin
