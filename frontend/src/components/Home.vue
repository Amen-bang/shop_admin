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
}
.el-main {
  background-color: #eaedf1;
}
</style>
