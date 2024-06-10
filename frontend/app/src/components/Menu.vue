<template>
  <section class="container" id="honeycomb_menu" style="padding-top: 13rem;">
    <ul class="honeycomb">
        <li class="honeycomb-cell">
          <div class="honeycomb-cell-overlay"/>
          <div class="honeycomb-cell-inner">
            <span class="honeycomb-cell-inner_title">Personne</span>
        </div>
      </li>
        <li class="honeycomb-cell">
          <div class="honeycomb-cell-overlay"/>
          <div class="honeycomb-cell-inner">
            <span class="honeycomb-cell-inner_title">Email</span>
        </div>
      </li>
        <li class="honeycomb-cell">
          <div class="honeycomb-cell-overlay"/>
          <div class="honeycomb-cell-inner">
            <span class="honeycomb-cell-inner_title">Pseudo</span>
        </div>
      </li>
        <li class="honeycomb-cell">
          <div class="honeycomb-cell-overlay"/>
          <div class="honeycomb-cell-inner">
            <span class="honeycomb-cell-inner_title">IP</span>
        </div>
      </li>
        <li class="honeycomb-cell">
          <div class="honeycomb-cell-overlay"/>
          <div class="honeycomb-cell-inner">
            <span class="honeycomb-cell-inner_title">Téléphone</span>
        </div>
      </li>
        <li class="honeycomb-cell">
          <div class="honeycomb-cell-overlay"/>
          <div class="honeycomb-cell-inner">
            <span class="honeycomb-cell-inner_title">Domaine</span>
        </div>
      </li>
        <li class="honeycomb-cell">
          <div class="honeycomb-cell-overlay"/>
          <div class="honeycomb-cell-inner">
            <span class="honeycomb-cell-inner_title">Overpass Turbo</span>
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
