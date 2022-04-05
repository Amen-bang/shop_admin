import Vue from 'vue'
import { Button, Form, FormItem, Input, Message } from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(Button).use(Form).use(FormItem).use(Input)
// 配置全局弹窗组件调用
Vue.prototype.$message = Message
