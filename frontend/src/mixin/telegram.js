import { mapActions } from 'vuex'

const TelegramMixin = {
  data: function () {
    return {
      telegramItems: [],
      telegramHasMore: false,
      telegramOffsetId: null,
      telegramCurrentUser: null
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

      this.getTelegramPosts({ username })
        .then(res => {
          this.telegramItems = [...res.data.messages]
          this.setTelegramPagination()
        })
    },
    onTelegramLoadMore () {
      this.getTelegramPosts({ username: this.telegramCurrentUser, offsetId: this.telegramOffsetId })
        .then(res => {
          this.telegramItems = [...this.telegramItems, ...res.data.messages]
          this.setTelegramPagination()
        })
    }
  }
}

export default TelegramMixin
