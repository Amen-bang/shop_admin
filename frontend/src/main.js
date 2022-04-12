import Vue from 'vue'
import App from './App.vue'
import router from './router'
// 按需引入ElementUI
import './plugins/element.js'
// 导入axios
import axios from 'axios'
// 导入全局样式表
import './assets/css/global.css'
// 导入字体图标
import './assets/fonts/iconfont.css'

// 配置请求根路径
axios.defaults.baseURL = 'http://192.168.91.131:1123/'
// 配置axios请求拦截器添加token，保证拥有获取数据的权限
axios.interceptors.request.use(config => {
  // 为请求头对象，添加 Token 验证的 Authorization 字段
  config.headers.Authorization = window.sessionStorage.getItem('token')
  // 在最后必须return config
  return config
})
Vue.prototype.$http = axios

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
