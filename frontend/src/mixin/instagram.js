import { mapActions } from 'vuex'

const InstagramMixin = {
  data: function () {
    return {
      instagramItems: [],
      instagramHasMore: false,
      instagramEndCursor: null,
      instagramCurrentShortcode: null,
      instagramZeroState: true
    }
  },
  methods: {
    ...mapActions({
      getInstagramComments: 'media/getInstagramComments'
    }),
    getInstagramShortcodeFromUrl (url) {
      const match = /^(?:.*\/p\/)([\d\w\-_]+)/.exec(url)
      if (match === null) return null
      return match[1]
    },
    onInstagramSubmit (url) {
      this.instagramCurrentShortcode = this.getInstagramShortcodeFromUrl(url)
      if (this.instagramCurrentShortcode === null) {
        console.error('Invalid Instagram Post URL!!')
        return
      }
      this.instagramEndCursor = null
      this.instagramHasMore = false
      this.loadingState = true

      this.getInstagramComments({ shortcode: this.instagramCurrentShortcode })
        .then(res => {
          this.instagramItems = [...res.data.comments]
          this.instagramEndCursor = res.data.new_end_cursor
          this.instagramHasMore = res.data.has_next_page
          if (this.instagramZeroState) this.instagramZeroState = false
        })
        .finally(() => {
          this.loadingState = false
        })
    },
    onInstagramLoadMore () {
      this.loadingState = true
      this.getInstagramComments({ shortcode: this.instagramCurrentShortcode, endCursor: this.instagramEndCursor })
        .then(res => {
          this.instagramItems = [...this.instagramItems, ...res.data.comments]
          this.instagramEndCursor = res.data.new_end_cursor
          this.instagramHasMore = res.data.has_next_page
        })
        .finally(() => {
          this.loadingState = false
        })
    }
  }
}

export default InstagramMixin
