<template>
    <div class="result-bento">
        <div class="bento-item bento-phonenumbers">
            <h3>Phonenumbers</h3>
            <div class="bento-content">
                <span>Numéro possible: {{ bool_types[responseData.data.is_possible_number] }}</span>
                <span>Numéro valide: {{ bool_types[responseData.data.is_valid_number] }}</span>
                <span>Pays: {{ responseData.data.country }}</span>
                <span>Opérateur: {{ responseData.data.operator }}</span>
                <span>Type: {{ responseData.data.line_type }}</span>
            </div>
        </div>
        <div class="bento-grid-phone">
            <div class="bento-item bento-tellows">
                <div class="bento-external-link">
                    <ArrowUpRight @click="openUrl(responseData.data.reputation.tellows.url)" />
                </div>
                <h3>Tellows</h3>
                <div class="bento-content">
                    <span>Score: {{ responseData.data.reputation.tellows.score }}</span>
                    <span v-for="note in responseData.data.reputation.tellows.notes" :key="note">{{ note }}</span>
                </div>
            </div>
            <div class="bento-item bento-spamcalls">
                <div class="bento-external-link">
                    <ArrowUpRight @click="openUrl(responseData.data.reputation.spamcalls.url)" />
                </div>
                <h3>Spamcalls</h3>
                <div class="bento-content">
                    <span>Spam: {{ bool_types[responseData.data.reputation.spamcalls.is_spam] }}</span>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { ArrowUpRight } from 'lucide-vue-next';
    import { openUrl } from '@/components/functions/openUrl';
</script>

<script>
    export default {
        data () {
            return {
                bool_types: {
                    'true': '✅',
                    'false': '❌',
                },
            }
        },
        props: {
            responseData: {
                type: Object,
                default: {
                    data: {
                        is_possible_number: false,
                        is_valid_number: false,
                        country: '',
                        operator: '',
                        line_type: '',
                        reputation: {
                            tellows: {
                                url: '',
                                score: 0,
                                notes: []
                            },
                            spamcalls: {
                                url: '',
                                is_spam: false
                            }
                        }
                    }
                }
            }
        }
    }
</script>



<style lang="scss" scoped>
    @import url(./styles/phone.scss);
    @import url(../../views/styles/result.scss);
</style>