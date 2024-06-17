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
        <li>
            <History @click="openHistory" class="history-button" alt="Historique" title="Historique"/>
        </li>
        <li>
          <Moon v-if="colorTheme === 'light_theme'" @click="toggleDarkMode" />
          <Sun v-if="colorTheme === 'dark_theme'" @click="toggleDarkMode" />
        </li>
      </ul>
      <ul v-show="mobileNav" class="mobile-navigation">
        <div>
          <Moon v-if="colorTheme === 'light_theme'" id="toggle-dark-mode" @click="toggleDarkMode" />
          <Sun v-if="colorTheme === 'dark_theme'" id="toggle-dark-mode" @click="toggleDarkMode" />
        </div>
        <li><router-link :to="{ name: 'Home' }" @click="mobileNav = false">Accueil</router-link></li>
        <li><router-link :to="{ name: 'About' }" @click="mobileNav = false">À propos</router-link></li>
        <li><a href="https://gitlab.com/bsi-dls/piposint" target="_blank" @click="mobileNav = false">Gitlab</a></li>
        <li><router-link :to="{ name: 'Tutorials' }" @click="mobileNav = false">Tuto</router-link></li>
      </ul>
      <ul v-show="mobile" class="navbar-items">
        <li class="history-button">
          <History @click="openHistory" alt="Historique" title="Historique"/>
        </li>
        <li>
          <Menu @click="toggleMobileNavigation"/>
        </li>
      </ul>
    </nav>
    <TheHistory v-if="isHistoryOpen" v-click-outside="openHistory"/>
  </header>
</template>


<script setup>
  import { History, Menu, Moon, Sun } from 'lucide-vue-next';
</script>

<script>
  import TheHistory from '@/components/History.vue';
  import checkScreen from '@/components/mixins/checkScreen';
  import clickOutsideHistory from './mixins/clickOutsideHistory';

  export default {
    name: 'Navbar',
    mixins: [checkScreen],
    data() {
        return {
            scrollPosition: null,
            isHistoryOpen: false,
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
          document.documentElement.style.backgroundColor = '';
        } else {
          this.colorTheme = 'dark_theme';
          document.documentElement.classList.remove('light_theme');
          document.documentElement.style.backgroundColor = '#10031d';
        }
        document.documentElement.classList.add(this.colorTheme);
        localStorage.setItem('piposintTheme', this.colorTheme);
      },
      openHistory() {
        this.isHistoryOpen = !this.isHistoryOpen;
      },
    },
    mounted() {
      if (localStorage.getItem('piposintTheme')) {
        // Load the theme from local storage variable
        this.colorTheme = localStorage.getItem('piposintTheme');
        if (this.colorTheme === 'dark_theme') {
          document.documentElement.style.backgroundColor = '#10031d';
        }

      } else {
        localStorage.setItem('piposintTheme', this.colorTheme);
      }
      document.documentElement.classList.add(this.colorTheme);
    },
    components: { TheHistory },
    directives: {
      clickOutside: clickOutsideHistory,
      },
  };
</script>

<style lang="scss" scoped>
  @import url(./styles/navbar.scss);
</style>