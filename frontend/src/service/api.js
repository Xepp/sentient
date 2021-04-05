import { mapValues } from 'lodash'
import axios from 'axios'

const endpoints = {
  getKhabarFooriComments: {
    method: 'GET',
    url: '/api/web/khabar-foori'
  },
  getInstagramComments: {
    method: 'GET',
    url: '/api/instagram/<shortcode>'
  },
  getTwitterStatuses: {
    method: 'GET',
    url: '/api/twitter/<username>'
  },
  getTelegramPosts: {
    method: 'GET',
    url: '/api/telegram/<username>'
  }
}

const api = mapValues(endpoints, (value) => {
  return function ({ params, data, ...urlParams }) {
    const req = {
      params,
      data,
      ...value
    }
    Object.keys(urlParams).forEach(k => {
      req.url = req.url.replaceAll(`<${k}>`, urlParams[k])
    })

    return axios(req)
  }
})

export default api
