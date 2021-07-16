import { mapActions } from 'vuex'

const TelegramMixin = {
  data: function () {
    return {
      telegramItems: [],
      telegramHasMore: false,
      telegramOffsetId: null,
      telegramCurrentUser: null,
      telegramZeroState: true
    }
  },
  methods: {
    ...mapActions({
      getTelegramPosts: 'media/getTelegramPosts'
    }),
    setTelegramPagination () {
      if (this.telegramItems.length !== 0) {
        this.telegramOffsetId = this.telegramItems[this.telegramItems.length - 1].id
      }
      this.telegramHasMore = this.telegramOffsetId !== null && this.telegramOffsetId > 1
    },
    onTelegramSubmit (username) {
      this.telegramOffsetId = null
      this.telegramCurrentUser = username
      this.loadingState = true

      this.getTelegramPosts({ username })
        .then(res => {
          this.telegramItems = [...res.data.messages]
          this.setTelegramPagination()
          if (this.telegramZeroState) this.telegramZeroState = false
        })
        .finally(() => {
          this.loadingState = false
        })
    },
    onTelegramLoadMore () {
      this.loadingState = true
      this.getTelegramPosts({ username: this.telegramCurrentUser, offsetId: this.telegramOffsetId })
        .then(res => {
          this.telegramItems = [...this.telegramItems, ...res.data.messages]
          this.setTelegramPagination()
        })
        .finally(() => {
          this.loadingState = false
        })
    }
  }
}

export default TelegramMixin
