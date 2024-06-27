<template>
    <div class="result-bento">
        <div class="bento-grid-username">
            <div @click="openUrl(site.url)" v-for="site in responseData.data.sites" :key="site" class="bento-item bento-username-site">
                <div class="bento-content">
                  <img id="site-picture" :src="getFaviconUrl(site.url)" :alt="site.app">
                  <h3>{{ site.app }}</h3>
                  <template v-for="metadata in site.metadata">
                    <img id="profile-picture" v-if="metadata.key === 'picture'" :src="metadata.value" :alt="site.app">
                  </template>
                </div>
            </div>
         </div>
    </div>
    <div class="bento-empty" v-if="responseData.data.sites.length === 0">
      <p>Aucun domaine associé trouvé.</p>
    </div>
</template>

<script setup>
    import { getFaviconUrl } from '@/components/functions/getFaviconUrl';
    import { openUrl } from '@/components/functions/openUrl';
</script>

<script>
    export default {
        props: {
            responseData: {
                type: Object,
                default: {
                    data: {
                        sites: []
                    }
                }
            }
        },
    }
</script>

<style lang="scss" scoped>
    @import url(../../views/styles/result.scss);
    @import url(./styles/username.scss);
</style>