<template>
  <section v-show="!mobile" class="container" style="padding-top: 13rem;">
    <div class="title">À propos de nous</div>
    <div class="sub-container" style="padding-right: 0.5rem;">
      <span class="subtitle">Bonjour !</span>
      <p class="text">Bienvenue sur ce magnifique site ! 
        Nous sommes trois étudiants du Pôle Sup de La Salle à Rennes et ceci est notre projet annuel. <br><br>
        Nous sommes en Bachelor Sécurité Informatique (niveau BAC + 3) et avons donc eu l'idée de développer notre projet sur le thème de l'OSINT.
        </p>
    </div>
    <div class="sub-container" style="padding-left: 0.5rem;">
      <div class="cards">
        <div class="card">
          <img src="https://avatars.githubusercontent.com/u/107856433?v=4" alt="Prezident" width="120px" height="120px" style="align-self: center; margin: auto; border-radius: 50%;">
          <p>Prezident</p>
        </div>
        <div class="card">
          <img src="https://avatars.githubusercontent.com/u/90249274?v=4" alt="Ectolast" width="120px" height="120px" style="align-self: center; margin: auto; border-radius: 50%;">
          <p>Ectolast</p>
        </div>
        <div class="card">
          <img src="https://avatars.githubusercontent.com/u/54044114?v=4" alt="ArKoo" width="120px" height="120px" style="align-self: center; margin: auto; border-radius: 50%;">
          <p>ArKoo</p>
        </div>
      </div>
    </div>
  </section>

  <!-- faire ça pour chaque section je sais pas si c'est opti :/ -->
  <transition name="mobile-nav">
    <section v-show="mobile" class="mobile-container">
    <div class="title" style="padding-bottom: 2rem;">À propos de nous</div>
    <div class="mobile-sub-container">
    <span class="subtitle">Bonjour !</span>
      <p class="text">Bienvenue sur ce magnifique site ! 
      Nous sommes trois étudiants du Pôle Sup de La Salle à Rennes et ceci est notre projet annuel. <br><br>
      Nous sommes en Bachelor Sécurité Informatique (niveau BAC + 3) et avons donc eu l'idée de développer notre projet sur le thème de l'OSINT.
      </p>
    </div>
    <div class="mobile-sub-container">
      <div class="cards">
        <div class="card">
          <img src="https://avatars.githubusercontent.com/u/107856433?v=4" alt="Prezident" width="90px" height="90px" style="align-self: center; margin: auto; border-radius: 50%;">
          <p>Prezident</p>
        </div>
        <div class="card">
          <img src="https://avatars.githubusercontent.com/u/90249274?v=4" alt="Ectolast" width="90px" height="90px" style="align-self: center; margin: auto; border-radius: 50%;">
          <p>Ectolast</p>
        </div>
        <div class="card">
          <img src="https://avatars.githubusercontent.com/u/54044114?v=4" alt="ArKoo" width="90px" height="90px" style="align-self: center; margin: auto; border-radius: 50%;">
          <p>ArKoo</p>
        </div>
      </div>
    </div>
    </section>
  </transition>
  
  <section v-show="!mobile" class="container" style="padding-top: 5rem;">
    <div class="title">En bref</div>
    <div class="sub-container" style="padding-right: 0.5rem;">
      <span class="subtitle">pipOSINT, c'est quoi ?</span>
      <p>Dans l'ensemble c'est assez simple, c'est une boîte à outils. <br><br>
        On voulait faire un peu comme Aperi'Solve, un endroit avec pleins d'outils qui sont automatisés.
        Une donnée en entrée et une multitude de sorties, en revanche ce n'est pas facile en OSINT. <br><br>
        Donc on a opté pour plus simple, un endroit où on peut choisir son outil et l'utiliser sans trop de complications.</p>
    </div>
    <div class="sub-container" style="padding-left: 0.5rem;">
      <span class="subtitle">Pourquoi pipOSINT ?</span>
      <p>Le nom pipOSINT vient du jeu de mot avec "pip", l'outil pour installer des modules python et de l'acronyme OSINT.<br><br>
        On rassemble l'idée de l'outil qui installe des modules et une boîte à outils qui rassemble ... bah des outils.
        Le joueur de flûte de Hamelin, d'où le logo, nous a aussi inspiré, "pipo" l'instrument de musique, "pip" de python et enfin OSINT. <br><br>
       pipOSINT est né.
      </p>
    </div>
  </section>

  <transition name="mobile-nav">
    <section v-show="mobile" class="mobile-container" style="padding-top: 2rem;">
    <div class="title" style="padding-bottom: 2rem;">En bref</div>
    <div class="mobile-sub-container">
      <span class="subtitle">pipOSINT, c'est quoi ?</span>
      <p>Dans l'ensemble c'est assez simple, c'est une boîte à outils. <br><br>
        On voulait faire un peu comme Aperi'Solve, un endroit avec pleins d'outils qui sont automatisés.
        Une donnée en entrée et une multitude de sorties, en revanche ce n'est pas facile en OSINT. <br><br>
        Donc on a opté pour plus simple, un endroit où on peut choisir son outil et l'utiliser sans trop de complications.</p>
    </div>
    <div class="mobile-sub-container">
      <span class="subtitle">Pourquoi pipOSINT ?</span>
      <p>Le nom pipOSINT vient du jeu de mot avec "pip", l'outil pour installer des modules python et de l'acronyme OSINT.<br><br>
        On rassemble l'idée de l'outil qui installe des modules et une boîte à outils qui rassemble ... bah des outils.
        Le joueur de flûte de Hamelin, d'où le logo, nous a aussi inspiré, "pipo" l'instrument de musique, "pip" de python et enfin OSINT. <br><br>
       pipOSINT est né.
      </p>
    </div>
    </section>
  </transition>
  
  <section v-show="!mobile" class="container" style="padding-top: 5rem;">
    <div class="title">Mentions Légales</div>
    <div class="sub-container" style="padding-right: 0.5rem; justify-content: center;">
      <img src="../assets/gavel.png" alt="mentions-legales" style="width: 60%; align-self: center;">
    </div>
    <div class="sub-container" style="padding-left: 0.5rem;">
      <span class="subtitle">Conditions d'utilisation</span>
      <p>pipOSINT receuille et répertorie des outils d'Open Source Intelligence (OSINT) provenant de différentes sources disponibles publiquement. <br><br>
        Les informations fournies sur ce site sont fournies à titre informatif uniquement. 
        Nous ne garantissons ni ne cautionnons l'exactitude, l'exhaustivité ou la fiabilité des informations récupérées, et déclinons toute responsabilité quant à leur utilisation. <br><br> 
        Les utilisateurs sont responsables de l'utilisation des outils répertoriés et doivent se conformer aux lois et réglementations applicables. 
        Les utilisateurs sont encouragés à consulter les conditions d'utilisation et les politiques de confidentialité de chaque outil individuel avant de les utiliser. <br><br>
        En utilisant ce site, vous acceptez ces conditions d'utilisation.
      </p>
    </div>
  </section>

  <transition>
    <section v-show="mobile" class="mobile-container" style="padding-top: 5rem;">
    <div class="title" style="padding-bottom: 2rem;">Mentions Légales</div>
    <div class="mobile-sub-container" style="padding-right: 0.5rem; justify-content: center;">
      <img src="../assets/gavel.png" alt="mentions-legales" style="width: 35%; align-self: center;">
    </div>
    <div class="mobile-sub-container">
      <span class="subtitle">Conditions d'utilisation</span>
      <p>pipOSINT receuille et répertorie des outils d'Open Source Intelligence (OSINT) provenant de différentes sources disponibles publiquement. <br><br>
        Les informations fournies sur ce site sont fournies à titre informatif uniquement. 
        Nous ne garantissons ni ne cautionnons l'exactitude, l'exhaustivité ou la fiabilité des informations récupérées, et déclinons toute responsabilité quant à leur utilisation. <br><br> 
        Les utilisateurs sont responsables de l'utilisation des outils répertoriés et doivent se conformer aux lois et réglementations applicables. 
        Les utilisateurs sont encouragés à consulter les conditions d'utilisation et les politiques de confidentialité de chaque outil individuel avant de les utiliser. <br><br>
        En utilisant ce site, vous acceptez ces conditions d'utilisation.
      </p>
    </div>
    </section>
  </transition>

</template>  

<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

export default {
    name: 'About',
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
        if (this.windowWidth <= 1000) {
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
@import url(./styles/about.scss);
</style>