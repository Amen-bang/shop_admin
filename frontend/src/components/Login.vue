<template>
  <div class="login_container">
    <div class="login_box"></div>
  </div>
</template>

<script>
export default {}
</script>

<style lang="less" scoped>
.login_container {
  background: #2b4b6b;
  height: 100%;
}

.login_box {
  width: 450px;
  height: 350px;
  background-color: #fff;
  // 圆角边框
  border-radius: 3px;
  // 绝对定位,页面位移
  position: absolute;
  // 左和顶部各偏移50%，横和竖各偏移50%
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}
</style>
