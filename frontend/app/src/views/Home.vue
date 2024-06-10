<template>

  <section v-show="!mobile" class="container homescreen">
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
  </section>

  <transition name="mobile-nav">
    <section v-show="mobile" class="mobile-container homescreen" >
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
    </section>
  </transition>
  <TheMenu />
</template>  

<script>
import TheMenu from '@/components/Menu.vue';
import checkScreen from '@/components/mixins/checkScreen';

export default {
    name: 'Home',
    mixins: [checkScreen],
    methods: {
      goToMenu() {
        const element = document.getElementById('honeycomb_menu');
        if (element) {
          element.scrollIntoView({ behavior: 'smooth' });
        }
      },
    },
    components: { TheMenu }
};
</script>

<style lang="scss" scoped>
@import url("./styles/home.scss");
</style>