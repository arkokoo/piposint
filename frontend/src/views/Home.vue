<template>
  <section class="container">

    <div class="sub-container">
      <span class="title">Bienvenue sur pipOSINT
        <p class="subtitle">Votre boîte à outils d'OSINT.</p>
      </span>
      <button class="button">Let's go !
        <svg fill="currentColor" viewBox="0 0 24 24" class="icon">
          <path clip-rule="evenodd" d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25zm4.28 10.28a.75.75 0 000-1.06l-3-3a.75.75 0 10-1.06 1.06l1.72 1.72H8.25a.75.75 0 000 1.5h5.69l-1.72 1.72a.75.75 0 101.06 1.06l3-3z" fill-rule="evenodd"></path>
        </svg>
      </button>
    </div>

    <div class="sub-container2">
      <span class="text">En bref :</span>
      <p>Le but de pipOSINT est de rassembler un maximum 
        d'outils d'OSINT afin de tout avoir en un endroit et ainsi éviter une perte de temps considérable.<br><br>
        Il est aussi possible de porter cette version web dans un docker afin de self-host</p>
    </div>
  </section>
</template>  

<script>
export default {};
</script>

<style lang="scss" scoped>
.title {
  max-width: fit-content;
  padding-bottom: 1rem;
  font-size: 5rem;
  font-weight: 600;
  font-family: 'Space Mono', monospace;
  .subtitle{
    font-size: 1.5rem;
    font-weight: 400;
    font-family: 'Space Mono', monospace;
  }
}
.text {
  font-size: 2rem;
  font-weight: 400;
  font-family: 'Space Mono', monospace;
}
.container {
  display: flex;
  justify-content: space-between;
  .sub-container {
    max-width: 600px;
    display: flex;
    flex-direction: column;
    padding: 1em;
  }
  .sub-container2 {
    max-height: 350px;
    align-self: center;
    display: flex;
    flex-direction: column;
    padding-left: 4rem;
    padding-top: 4rem;
  }
}
section {
  padding-top: 13rem; // obligatoire pour le moment
  padding-bottom: 6rem;
  border-bottom: solid 1px rgba($color: #000000, $alpha: 0.1);
}
// le bouton let's go
.button {
  position: relative;
  width: 15rem;
  transition: all 0.3s ease-in-out;
  box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2);
  padding-block: 0.5rem;
  padding-inline: 1.25rem;
  background-color: rgb(13 121 37);
  border-radius: 9999px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ffff;
  gap: 10px;
  font-weight: bold;
  font-family: 'Space Mono', monospace;
  border: 3px solid #ffffff4d;
  outline: none;
  overflow: hidden;
  font-size: 15px;
  cursor: pointer;
}
.icon {
  width: 24px;
  height: 24px;
  transition: all 0.3s ease-in-out;
}
.button:hover {
  transform: scale(1.05);
  border-color: #fff9;
}
.button:hover .icon {
  transform: translate(4px);
}
.button:hover::before {
  animation: shine .5s ease-out;
}
.button::before {
  content: "";
  position: absolute;
  width: 100px;
  height: 100%;
  background-image: linear-gradient(
    120deg,
    rgba(255, 255, 255, 0) 30%,
    rgba(255, 255, 255, 0.8),
    rgba(255, 255, 255, 0) 70%
  );
  top: 0;
  left: -100px;
  opacity: 0.6;
}
@keyframes shine {
  0% {
    left: -100px;
  }
  60% {
    left: 100%;
  }
  to {
    left: 100%;
  }
}

</style>