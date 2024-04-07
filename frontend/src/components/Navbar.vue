<template>
  <header class="navbar">

    <link rel="stylesheet" 
        href="https://use.fontawesome.com/releases/v5.2.0/css/all.css" 
        integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ" 
        crossorigin="anonymous">

    <nav class="container">
      <a class="sides z-50 flex items-center gap-2 -ml-3 md:mr-12">
          <img src="./../assets/LE_NAIN.svg" alt="pipOSINT">
          <p>pipOSINT</p>
      </a>
      <ul v-show="!mobile" class="navigation">
        <li><router-link :to="{ name: 'Home' }" >Accueil</router-link></li>
        <li><router-link :to="{ name: 'About' }" >À propos</router-link></li>
        <li><a href="https://gitlab.com/bsi-dls/piposint" target="_blank">Gitlab</a></li>
        <li><router-link :to="{ name: 'Tutorials' }" >Tuto</router-link></li>
      </ul>
      <i v-show="!mobile" class="fas fa-moon"></i>
      <i v-show="mobile" @click="toggleMobileNavigation" class="fas fa-bars"></i>
      <transition name="mobile-nav">
        <ul v-show="mobileNav" class="mobile-navigation">
          <li><router-link :to="{ name: 'Home' }" >Accueil</router-link></li>
          <li><router-link :to="{ name: 'About' }" >À propos</router-link></li>
          <li><a href="https://gitlab.com/bsi-dls/piposint" target="_blank">Gitlab</a></li>
          <li><router-link :to="{ name: 'Tutorials' }" >Tuto</router-link></li>
          <li><i class="fas fa-moon" style="padding: 0;"></i></li>
        </ul>
      </transition>
    </nav>
  </header>
</template>

<script>

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

export default {
    name: 'Navbar',
    data() {
        return {
            scrollPosition: null,
            mobile: null,
            mobileNav: null,
            windowWidth: null,
        };
    },
    created () {
      window.addEventListener('resize', this.checkScreen);
      this.checkScreen();
    },
    methods: {
      toggleMobileNavigation() {
        this.mobileNav = !this.mobileNav;
      },
      checkScreen() {
        this.windowWidth = window.innerWidth;
        if (this.windowWidth <= 826) {
          this.mobile = true;
          return;
        } else {
          this.mobile = false;
          this.mobileNav = false;
          return;
        }
      },
    },
    components: { FontAwesomeIcon }
};
</script>

<style lang="scss" scoped>
@import url(./styles/navbar.scss);
</style>