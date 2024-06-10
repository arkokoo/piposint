<script setup>
import TheNavbar from './components/Navbar.vue'
import TheHome from './views/Home.vue'
import TheAbout from './views/About.vue'
import { RouterView } from 'vue-router';
</script>

<template>
  <TheNavbar />
  <RouterView />
</template>

<script>

export default {
  name: 'App',
  components: {
    TheNavbar,
    TheHome,
    TheAbout,
  },
};

</script>

<style lang="scss" scoped>

</style>