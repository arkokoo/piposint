<template>
    <div class="result-bento">
        <div class="bento-grid-email">
            <div v-for="domain in responseData.data.associated_domains" :key="domain" class="bento-item bento-email-domain">
                <div class="bento-external-link">
                  <ArrowUpRight @click="openUrl('https://' + domain)" />
                </div>
                <h3>{{ domain.split('.')[0].charAt(0).toUpperCase() + domain.split('.')[0].slice(1) }}</h3>
                <div class="bento-content">
                  <img :src="getFaviconUrl(domain)" :alt="domain">
                </div>
            </div>
         </div>
    </div>
    <div class="bento-empty" v-if="responseData.data.associated_domains.length === 0">
      <p>Aucun domaine associé trouvé.</p>
    </div>
</template>

<script setup>
    import { ArrowUpRight } from 'lucide-vue-next';
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
                        associated_domains: []
                    }
                }
            }
        },
    }
</script>

<style lang="scss" scoped>
    @import url(./styles/email.scss);
    @import url(../../views/styles/result.scss);
</style>