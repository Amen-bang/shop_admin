module.exports = {
  devServer: {
    /* 自动打开浏览器 */
    open: false,
    port: 8080,
    https: false,
    hotOnly: false
    // /* 使用代理 */
    // proxy: {
    //   '/api': {
    //     // 服务器协议、ip和端口号
    //     target: 'http://127.0.0.1:1123',
    //     // 如果是https接口，需要配置这个参数
    //     secure: false,
    //     // 是否代理websockets
    //     ws: true,
    //     // 是否跨域
    //     changeOrigin: true,
    //     // url中的/api替换为空
    //     pathRewrite: {
    //       '^/api': ''
    //     }
    //   }
    // }
  }
}
