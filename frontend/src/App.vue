<script setup>
import TheHome from './views/Home.vue'
import TheAbout from './views/About.vue'
import TheNavbar from './components/Navbar.vue'
import { RouterView } from 'vue-router';
</script>

<template>
  <div class="body">
    <RouterView />
    <TheNavbar />
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
    TheNavbar,
    TheHome,
    TheAbout,
  },
  data() {
    return {
      scrollPosition: null,
      mobile: null,
      mobileNav: null,
      windowWidth: null,
    };
  },
};

</script>

<style lang="scss" scoped>

</style>