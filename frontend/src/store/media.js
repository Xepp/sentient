import api from '@/service/api'

export default {
  namespaced: true,
  actions: {
    getKhabarFooriComments: (context, { url }) => {
      const payload = {
        params: {
          url
        }
      }
      return api.getKhabarFooriComments(payload)
    },
    getInstagramComments: (context, { shortcode, endCursor }) => {
      const payload = {
        params: {
          end_cursor: endCursor
        },
        shortcode
      }
      return api.getInstagramComments(payload)
    },
    getTwitterStatuses: (context, { username, maxId }) => {
      const payload = {
        params: {
          max_id: maxId
        },
        username
      }
      return api.getTwitterStatuses(payload)
    },
    getTelegramPosts: (context, { username, offsetId }) => {
      const payload = {
        params: {
          offset_id: offsetId
        },
        username
      }
      return api.getTelegramPosts(payload)
    }
  }
}
