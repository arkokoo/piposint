<template>
  <section class="container" id="honeycomb_menu" style="padding-top: 13rem;">
    <ul class="honeycomb">
        <li class="honeycomb-cell">
          <div class="honeycomb-cell-overlay"/>
          <div class="honeycomb-cell-inner">
            <router-link :to="'/search/person'" class="honeycomb-cell-inner_title">Personne</router-link>
        </div>
      </li>
        <li class="honeycomb-cell">
          <div class="honeycomb-cell-overlay"/>
          <div class="honeycomb-cell-inner">
            <router-link :to="'/search/email'" class="honeycomb-cell-inner_title">Email</router-link>
        </div>
      </li>
        <li class="honeycomb-cell">
          <div class="honeycomb-cell-overlay"/>
          <div class="honeycomb-cell-inner">
            <router-link :to="'/search/username'" class="honeycomb-cell-inner_title">Pseudo</router-link>
        </div>
      </li>
        <li class="honeycomb-cell">
          <div class="honeycomb-cell-overlay"/>
          <div class="honeycomb-cell-inner">
            <router-link :to="'/search/ip'" class="honeycomb-cell-inner_title">Adresse IP</router-link>
        </div>
      </li>
        <li class="honeycomb-cell">
          <div class="honeycomb-cell-overlay"/>
          <div class="honeycomb-cell-inner">
            <router-link :to="'/search/phone'" class="honeycomb-cell-inner_title">Téléphone</router-link>
        </div>
      </li>
        <li class="honeycomb-cell">
          <div class="honeycomb-cell-overlay"/>
          <div class="honeycomb-cell-inner">
            <router-link :to="'/search/domain'" class="honeycomb-cell-inner_title">Domaine</router-link>
        </div>
      </li>
        <li class="honeycomb-cell">
          <div class="honeycomb-cell-overlay"/>
          <div class="honeycomb-cell-inner">
            <a href="/services/overpass-turbo/" target="_blank" class="honeycomb-cell-inner_title">Overpass-Turbo</a>
        </div>
      </li>
    </ul>
  </section>
</template>  
  
<script>
  export default {
    name: 'Menu',
    mounted() {
      const tags = document.querySelectorAll('.honeycomb-cell');

      tags.forEach(tag => {
        tag.addEventListener('mouseenter', () => {
          tags.forEach(tag => {
            tag.classList.add('comb_not_hovered');
          });
          document.body.classList.remove('comb_not_hovered');
        });

        tag.addEventListener('mouseleave', () => {
          tags.forEach(tag => {
            tag.classList.remove('comb_not_hovered');
          });
        });
      });
    }
  };
</script>

<style lang="scss" scoped>
  @import url(./styles/menu.scss);
</style>
