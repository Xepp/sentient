import { mapActions } from 'vuex'

const TelegramMixin = {
  data: function () {
    return {
      telegramOffsetId: null,
      telegramCurrentUser: null
    }
  },
  methods: {
    ...mapActions({
      getTelegramPosts: 'media/getTelegramPosts'
    }),
    setTelegramPagination () {
      if (this.items.length !== 0) {
        this.telegramOffsetId = this.items[this.items.length - 1].id
      }
      this.hasMore = this.telegramOffsetId !== null && this.telegramOffsetId > 1
    },
    onTelegramSubmit (username) {
      this.telegramOffsetId = null
      this.telegramCurrentUser = username

      this.getTelegramPosts({ username })
        .then(res => {
          this.items = [...res.data.messages]
          this.setTelegramPagination()
        })
    },
    onTelegramLoadMore () {
      this.getTelegramPosts({ username: this.telegramCurrentUser, offsetId: this.telegramOffsetId })
        .then(res => {
          this.items = [...this.items, ...res.data.messages]
          this.setTelegramPagination()
        })
    }
  }
}

export default TelegramMixin
