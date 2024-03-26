<template>

  <section v-show="!mobile" class="container" style="z-index: 10;">
    <div class="sub-container">
      <span class="title">Bienvenue sur pipOSINT
        <p class="subtitle">Votre boîte à outils d'OSINT.</p>
      </span>
      <button class="button" @click="goToMenu">Let's go !
        <svg fill="currentColor" viewBox="0 0 24 24" class="icon">
          <path clip-rule="evenodd" d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25zm4.28 10.28a.75.75 0 000-1.06l-3-3a.75.75 0 10-1.06 1.06l1.72 1.72H8.25a.75.75 0 000 1.5h5.69l-1.72 1.72a.75.75 0 101.06 1.06l3-3z" fill-rule="evenodd"></path>
        </svg>
      </button>
    </div>
  </section>

  <transition name="mobile-nav">
    <section v-show="mobile" class="mobile-container" style="z-index: 10;">
      <div class="sub-mobile-container"> 
        <span class="title">Bienvenue sur pipOSINT
          <p class="subtitle">Votre boîte à outils d'OSINT.</p>
        </span>
        <button class="button" @click="goToMenu">Let's go !
          <svg fill="currentColor" viewBox="0 0 24 24" class="icon">
            <path clip-rule="evenodd" d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25zm4.28 10.28a.75.75 0 000-1.06l-3-3a.75.75 0 10-1.06 1.06l1.72 1.72H8.25a.75.75 0 000 1.5h5.69l-1.72 1.72a.75.75 0 101.06 1.06l3-3z" fill-rule="evenodd"></path>
          </svg>
        </button>
      </div>
    </section>
  </transition>
  <div class="animated-background">
      <ul>
        <li>&#x2B22;</li>
        <li>&#x2B22;</li>
        <li>&#x2B22;</li>
        <li>&#x2B22;</li>
        <li>&#x2B22;</li>
        <li>&#x2B22;</li>
        <li>&#x2B22;</li>
        <li>&#x2B22;</li>
      </ul>
    </div>
  <TheMenu />
</template>  

<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import TheMenu from '@/components/Menu.vue';

export default {
    name: 'Home',
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
      goToMenu() {
        const element = document.getElementById('honeycomb_menu');
        if (element) {
          element.scrollIntoView({ behavior: 'smooth' });
        }
      },
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
    components: { FontAwesomeIcon, TheMenu }
};
</script>

<style lang="scss" scoped>
@import url("./styles/home.scss");
</style>