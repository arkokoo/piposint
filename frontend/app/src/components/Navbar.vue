<template>
  <header class="navbar">

    <link rel="stylesheet" 
        href="https://use.fontawesome.com/releases/v5.2.0/css/all.css" 
        integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ" 
        crossorigin="anonymous">

    <nav class="container">
      <router-link :to="{ name: 'Home' }" @click="mobileNav = false" class="piposint-logo">
        <img src="./../assets/images/piposint.svg" alt="pipOSINT">
        <p>pipOSINT</p>
      </router-link>
      <ul v-show="!mobile" class="navigation">
        <li><router-link :to="{ name: 'Home' }" >Accueil</router-link></li>
        <li><router-link :to="{ name: 'About' }" >À propos</router-link></li>
        <li><a href="https://gitlab.com/bsi-dls/piposint" target="_blank">Gitlab</a></li>
        <li><router-link :to="{ name: 'Tutorials' }" >Tuto</router-link></li>
      </ul>
      <ul v-show="!mobile" class="navbar-items">
          <li><i class="fas fa-sync" id="history-button"></i></li>
          <li><i id="toggle-dark-mode" :class="{'fas fa-moon': colorTheme === 'light_theme', 'fas fa-sun': colorTheme === 'dark_theme'}" @click="toggleDarkMode"></i></li>
      </ul>
      <ul v-show="mobileNav" class="mobile-navigation">
        <i id="toggle-dark-mode" :class="{'fas fa-moon': colorTheme === 'light_theme', 'fas fa-sun': colorTheme === 'dark_theme'}" @click="toggleDarkMode"></i>
        <li><router-link :to="{ name: 'Home' }" @click="mobileNav = false">Accueil</router-link></li>
        <li><router-link :to="{ name: 'About' }" @click="mobileNav = false">À propos</router-link></li>
        <li><a href="https://gitlab.com/bsi-dls/piposint" target="_blank" @click="mobileNav = false">Gitlab</a></li>
        <li><router-link :to="{ name: 'Tutorials' }" @click="mobileNav = false">Tuto</router-link></li>
      </ul>
      <ul v-show="mobile" class="navbar-items">
        <li><i class="fas fa-sync" id="history-button"></i></li>
        <li><i class="fas fa-bars" @click="toggleMobileNavigation"></i></li>
      </ul>
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
          colorTheme: "light_theme",
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
    toggleDarkMode() {
      if (this.colorTheme === 'dark_theme') {
        this.colorTheme = 'light_theme';
        document.documentElement.classList.remove('dark_theme');
      } else {
        this.colorTheme = 'dark_theme';
        document.documentElement.classList.remove('light_theme');
      }
      document.documentElement.classList.add(this.colorTheme);
      localStorage.setItem('piposintTheme', this.colorTheme);
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
  mounted() {
    if (localStorage.getItem('piposintTheme')) {
      // Load the theme from local storage variable
      this.colorTheme = localStorage.getItem('piposintTheme')
    }
    else {
      localStorage.setItem('piposintTheme', this.colorTheme);
    }
    document.documentElement.classList.add(this.colorTheme);
  },
  components: { FontAwesomeIcon }
};
</script>

<style lang="scss" scoped>
@import url(./styles/navbar.scss);
</style>