<template>

  <section v-show="!mobile" class="container" style="z-index: 10;">
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
  </section>

  <transition name="mobile-nav">
    <section v-show="mobile" class="mobile-container" style="z-index: 10;">
      <div class="sub-mobile-container"> 
        <span class="title">Bienvenue sur pipOSINT
          <p class="subtitle">Votre boîte à outils d'OSINT.</p>
        </span>
        <button class="button">Let's go !
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
</template>  

<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

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
@import url(./../assets/main.scss);

.container {
  padding-top: 25rem;
  align-items: center;
  padding-bottom: 20rem;
  .sub-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    .button {
      width: 20rem;
      font-size: 20px;
    }
  }
}
// mobile version
.mobile-container {
  padding-top : 20rem;
  padding-bottom: 15rem;
  .sub-mobile-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    .title {
      font-size: 4rem;
      padding-bottom: 0;
    }
    .button {
      align-self: center;
    }
  }
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