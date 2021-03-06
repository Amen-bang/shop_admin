import Vue from 'vue'
import {
  Button, Form, FormItem, Input, Message,
  Container, Header, Aside, Main,
  Menu, Submenu, MenuItem,
  Breadcrumb, BreadcrumbItem,
  Card, Row, Col, Table, TableColumn,
  Switch, Tooltip, Pagination,
  Dialog, MessageBox
} from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(Button).use(Form).use(FormItem).use(Input)
Vue.use(Container).use(Header).use(Aside).use(Main)
Vue.use(Menu).use(Submenu).use(MenuItem)
Vue.use(Breadcrumb).use(BreadcrumbItem)
Vue.use(Card).use(Row).use(Col).use(Table).use(TableColumn)
Vue.use(Switch).use(Tooltip).use(Pagination)
Vue.use(Dialog)
// 配置全局弹窗组件调用
Vue.prototype.$message = Message
// 配置删除弹窗
Vue.prototype.$confirm = MessageBox
