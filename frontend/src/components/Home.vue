<template>
  <el-container class="home-container">
    <!--头部区域-->
    <el-header>
      <div>
        <img class="logo_img" src="../assets/logo2.png" alt />
        <span>陈邦邦后台管理系统</span>
      </div>
      <el-button type="info" @click="loginOut">退出</el-button>
    </el-header>

    <!--页面主题区域-->
    <el-container>
      <!--侧边栏,动态切换宽度，保证缩小侧边栏能隐藏-->
      <el-aside :width="isCollapse ? '64px':'200px'">
        <!-- 折叠按钮 -->
        <div class="toggle-button" @click="toggleCollapse">|||</div>
        <!--侧边栏菜单区域-->
        <el-menu background-color="#333744" text-color="#fff" active-text-color="#409EFF"
          :unique-opened="true" :collapse="isCollapse" :collapse-transition="false" router :default-active="activePath">
          <!--1级菜单，index绑定一个唯一值，保证不会打开一个导航栏影响其他导航栏，使用item.id另其成为唯一同时要另其为字符串形式-->
          <el-submenu :index="item.id + ''" v-for="item in menuList" :key="item.id">
            <!--1级菜单模板区域-->
            <template slot="title">
              <!--图标，绑定特定的图标-->
              <i :class="iconsObj[item.id]"></i>
              <!--文本-->
              <span>{{item.authName}}</span>
            </template>
            <!--2级菜单-->
            <el-menu-item :index="item.id + ''" v-for="subItem in item.children" :key="subItem.id">
              <template slot="title">
                <!--图标-->
                <i class="el-icon-menu"></i>
                <!--文本-->
                <span>{{subItem.authName}}</span>
              </template>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main>
        <!--路由占位符-->
        <router-view></router-view>
      </el-main>
    </el-container>

  </el-container>
</template>

<script>
export default {
  data () {
    return {
      // 左侧菜单数据
      menuList: [],
      iconsObj: {
        '125': 'iconfont icon-user',
        '103': 'iconfont icon-tijikongjian',
        '101': 'iconfont icon-shangpin',
        '102': 'iconfont icon-danju',
        '145': 'iconfont icon-baobiao'
      },
      // 是否折叠
      isCollapse: false,
      // 被激活链接的路径
      activePath: ''
    }
  },
  // 页面加载的时候马上获取左侧菜单
  created () {
    this.getMenuList()
    this.activePath = window.sessionStorage.getItem('activePath')
  },
  methods: {
    // 退出功能
    loginOut: function () {
      // 清空token
      window.sessionStorage.clear()
      // 跳转到登录页
      this.$router.push('/login')
    },
    // 获取所有的菜单
    async getMenuList () {
      const { data: res } = await this.$http.get('menus')
      if (res.meta.status !== 200) return this.$message.error(res.meta.msg)
      // console.log(res)
      this.menuList = res.data
    },
    // 点击按钮切换菜单的折叠与展开
    toggleCollapse () {
      this.isCollapse = !this.isCollapse
    }
  }
}
</script>

<style lang="less" scoped>
.home-container {
  height: 100%;
}
.logo_img {
  height: 55px;
  width: 55px;
  border: 1px solid #eee;
  border-radius: 50%;
}
.el-header {
  background-color: #373d41;
  display: flex;
  justify-content: space-between;
  padding-left: 0;
  align-items: center;
  color: #fff;
  > div {
    display: flex;
    align-items: center;
    span {
      margin-left: 15px;
    }
  }
}
.el-aside {
  background-color: #333744;
  .el-menu {
    border-right: 0;
  }
}
.el-main {
  background-color: #eaedf1;
}
.iconfont {
  margin-right: 10px;
}
.toggle-button {
  background-color: #4a5064;
  font-size: 10px;
  line-height: 24px;
  color: #fff;
  text-align: center;
  letter-spacing: 0.2em;
  cursor: pointer;
}
</style>
