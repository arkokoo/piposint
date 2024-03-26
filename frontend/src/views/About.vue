<template>
  <section class="container" style="padding-top: 13rem;">
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
          <img src="https://avatars.githubusercontent.com/u/107856433?v=4" alt="Prezident" width="150px" height="150px" style="align-self: center; margin: auto; border-radius: 50%;">
          <p>Prezident</p>
        </div>
        <div class="card">
          <img src="https://avatars.githubusercontent.com/u/90249274?v=4" alt="Ectolast" width="150px" height="150px" style="align-self: center; margin: auto; border-radius: 50%;">
          <p>Ectolast</p>
        </div>
        <div class="card">
          <img src="https://avatars.githubusercontent.com/u/54044114?v=4" alt="ArKoo" width="150px" height="150px" style="align-self: center; margin: auto; border-radius: 50%;">
          <p>ArKoo</p>
        </div>
        
      </div>
    </div>
  </section>
  <section class="container" style="padding-top: 5rem;">
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
  <section class="container" style="padding-top: 5rem;">
    <div class="title">Mentions Légales</div>
    <div class="sub-container" style="padding-right: 0.5rem;">
      <!-- <font-awesome-icon :icon="['fas', 'scale-balanced']" height="300px"/> marche pas bien :/ -->
    </div>
    <div class="sub-container" style="padding-left: 0.5rem;">
      <span class="subtitle">Conditions d'utilisation</span>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure 
        dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
        sunt in culpa qui officia deserunt mollit anim id est laborum.
      </p>
    </div>
  </section>
</template>  

<script>
  export default {};
</script>

<style lang="scss" scoped>
@import url(./styles/about.scss);
</style>