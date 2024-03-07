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
        <li><router-link :to="{ name: 'Home' }" ><button>Accueil</button></router-link></li>
        <li><router-link :to="{ name: 'About' }" ><button>À propos</button></router-link></li>
        <li><a href="https://gitlab.com/bsi-dls/piposint" target="_blank"><button>Gitlab</button></a></li>
        <li><router-link :to="{ name: 'Tutorials' }" ><button>Tuto</button></router-link></li>
      </ul>
      <i v-show="!mobile" class="fas fa-moon"></i>
      <i v-show="mobile" @click="toggleMobileNavigation" class="fas fa-bars"></i>
      <transition name="mobile-nav">
        <ul v-show="mobileNav" class="mobile-navigation">
          <li><router-link :to="{ name: 'Home' }" ><button>Accueil</button></router-link></li>
          <li><router-link :to="{ name: 'About' }" ><button>À propos</button></router-link></li>
          <li><a href="https://gitlab.com/bsi-dls/piposint" target="_blank"><button>Gitlab</button></a></li>
          <li><router-link :to="{ name: 'Tutorials' }" ><button>Tuto</button></router-link></li>
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
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 50;
  background-color: #f7f9f4;
  transition: .5s ease all;
  color: #000000;
  .container {
    position: relative;
    display: flex;
    align-items: stretch;
    justify-content: space-between;
    padding-top: 0.75rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    padding-left: 12px;
    padding-right: 12px;

    // mobile version
    .mobile-navigation {
      display: flex;
      align-items: center;
      flex-direction: column;
      position: fixed;
      background-color: #f7f9f4;
      width: 100%;
      max-width: 250px;
      height: 100%;
      margin-top: 0;
      top: 0;
      left: 0;
      border-right: solid 1px rgba($color: #000000, $alpha: 0.1);
    } 
  }
  li{
  padding: 0.5em;
  }
  i{
    padding-left: 100px;
    padding-right: 25px;
    font-size: 25px;
    align-self: center;
    cursor: pointer;
  }
  gap-2 {
    gap: 0.5rem;
  }
  p{
    font-size: 1.25rem;
    font-weight: 600;
    font-family: 'Space Mono', monospace;
  }
  img {
    width: 4rem;
    height: 4rem;
    align-self: center;
  }
}
.sides {
  min-width: 150px;
  max-width: 150px;
  display: flex;
  align-self: center;
}
ul {
  display: flex;
  padding-left: 0;
  list-style-type: none;
}

// Les boutons des liens de navigation
button {
 appearance: none;
 background-color: transparent;
 border: 0.125em solid #1A1A1A;
 border-radius: 0.9375em;
 box-sizing: border-box;
 color: #000000;
 cursor: pointer;
 display: inline-block;
 font-family: 'Space Mono', monospace;
 font-size: 12px;
 font-weight: 600;
 line-height: normal;
 margin: 0;
 min-height: 3.75em;
 min-width: 10em;
 outline: none;
 padding: 1em 2.3em;
 text-align: center;
 text-decoration: none;
 transition: all 300ms cubic-bezier(.23, 1, 0.32, 1);
 user-select: none;
 -webkit-user-select: none;
 touch-action: manipulation;
 will-change: transform;
}
button:disabled {
 pointer-events: none;
}
button:hover {
 color: #fff;
 background-color: #1A1A1A;
 box-shadow: rgba(0, 0, 0, 0.25) 0 8px 15px;
 transform: translateY(-2px);
}
button:active {
 box-shadow: none;
 transform: translateY(0);
}
</style>