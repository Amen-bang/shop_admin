<template>
  <el-container class="home-container">
    <!--头部区域-->
    <el-header>
      <el-button type="info" @click="loginOut">退出</el-button>
    </el-header>
    <!--页面主题区域-->
    <el-container>
      <!--侧边栏-->
      <el-aside></el-aside>
      <el-main></el-main>
    </el-container>
  </el-container>
</template>

<script>
export default {
  methods: {
    loginOut: function () {
      // 清空token
      window.sessionStorage.clear()
      // 跳转到登录页
      this.$router.push('/login')
    }
  }
}
</script>

<style lang="less" scoped>
.home-container {
  height: 100%;
}
.el-header {
  background-color: #373d41;
}
.el-aside {
  background-color: #333744;
}
.el-main {
  background-color: #eaedf1;
}
</style>
