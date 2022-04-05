import Vue from 'vue'
import {
  Button, Form, FormItem, Input, Message,
  Container, Header, Aside, Main
} from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(Button).use(Form).use(FormItem).use(Input)
Vue.use(Container).use(Header).use(Aside).use(Main)
// 配置全局弹窗组件调用
Vue.prototype.$message = Message
