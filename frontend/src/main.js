import Vue from 'vue'
import App from './App.vue'
import router from './router'
// 引入ElementUI
import ElementUI from 'element-ui'
// 导入axios
import axios from 'axios'
// 引入css
import 'element-ui/lib/theme-chalk/index.css'
// 导入全局样式表
import './assets/css/global.css'
// 导入字体图标
import './assets/fonts/iconfont.css'

// 使用ElementUI
Vue.use(ElementUI)

// 设置请求根路径
axios.defaults.baseURl = 'http://127.0.0.1:8080/api'
Vue.prototype.$http = axios

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
