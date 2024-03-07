<template>
  <section class="container" style="padding-top: 13rem;">
    <div class="title">À propos de nous</div>
    <div class="sub-container">
      <span class="subtitle">Bonjour !</span>
      <p class="text">Bienvenue sur ce magnifique site ! 
        Nous sommes trois étudiants du Pôle Sup de La Salle à Rennes et ceci est notre projet annuel. <br><br>
        Nous sommes en Bachelor Sécurité Informatique (niveau BAC + 3) et avons donc eu l'idée de développer notre projet sur le thème de l'OSINT.
        </p>
    </div>
    <div class="sub-container">
      <div class="cards">
        <div class="card">
          <img src="./../assets/LE_NAIN.svg" alt="test" width="150px" height="150px" style="align-self: center; margin: auto;">
        </div>
        <div class="card">
          <img src="./../assets/LE_NAIN.svg" alt="test" width="150px" height="150px" style="align-self: center; margin: auto;">
        </div>
        <div class="card">
          <img src="./../assets/LE_NAIN.svg" alt="test" width="150px" height="150px" style="align-self: center; margin: auto;">
        </div>
        
      </div>
    </div>
  </section>
  <section class="container">
    <div class="title">En bref</div>
  </section>
  <section class="container">
    <div class="title">Mentions Légales</div>
  </section>
</template>  

<script>
export default {};
</script>

<style lang="scss" scoped>
@import url(./../assets/main.scss);

.container {
  display: flex;
  flex-wrap: wrap-reverse;
  flex-direction: row;
  justify-content: center;
  .title {
    order: 1;
    width: 50%;
    padding-bottom: 1.5rem;
    font-size: 3rem;
    align-self: center;
  }
  .subtitle {
    font-size: 2rem;
  }
  .sub-container {
    display: flex;
    width: 50%;
    flex-direction: column;
  }
  .cards {
    display: flex;
    justify-content: space-between;
    .card {
      display: flex;
      margin: 1rem;
      width: 190px;
      height: 254px;
      border-radius: 30px;
      background: #f7f9f4;
      box-shadow: 15px 15px 30px #bebebe,
                 -15px -15px 30px #ffffff;
    }
  
  }
}

</style>