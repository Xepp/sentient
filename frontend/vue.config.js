module.exports = {
  lintOnSave: false,
  devServer: {
    proxy: {
      '^/api': {
        target: process.env.VUE_APP_API_SERVER
      }
    }
  }
}
