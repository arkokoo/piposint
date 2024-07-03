<template>
    <div class="result-bento">
        <div class="bento-grid-person">
            <div class="bento-item bento-chart-country">
                <h3>Pays</h3>
                <Pie :data="getCountryChartData" :options="{ responsive: true}"/>
            </div>
            <div class="bento-item bento-chart-gender">
                <h3>Genre</h3>
                <Pie :data="getGenderChartData" :options="{ responsive: true}"/>
            </div>
            <div class="bento-item bento-person-dorks">
                <h3>Google Dorks</h3>
                <div class="bento-content">
                    <ul>
                        <li><a :href="`https://www.google.com/search?q=${ '&quot;' + responseData.args[0]} ${responseData.args[1] + '&quot;'}`" target="_blank">Nom complet</a></li>
                        <li><a :href="`https://www.google.com/search?q=${ '&quot;' + responseData.args[0] + ' ' + responseData.args[1] + '&quot; site:facebook.com'}`" target="_blank">Facebook</a></li>
                        <li><a :href="`https://www.google.com/search?q=${ '&quot;' + responseData.args[0] + ' ' + responseData.args[1] + '&quot; site:linkedin.com'}`" target="_blank">LinkedIn</a></li>
                        <li><a :href="`https://www.google.com/search?q=${ '&quot;' + responseData.args[0] + ' ' + responseData.args[1] + '&quot; site:twitter.com'}`" target="_blank">Twitter</a></li>
                        <li><a :href="`https://www.google.com/search?q=${ '&quot;' + responseData.args[0] + ' ' + responseData.args[1] + '&quot; site:instagram.com'}`" target="_blank">Instagram</a></li>
                    </ul>
                </div>
            </div>
         </div>
         <div class="bento-item bento-person-webmii">
            <h3>Webmii</h3>
            <div class="bento-content">
                <iframe :src="getWebMiiUrl()"></iframe>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { Pie} from 'vue-chartjs';
    import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';

    ChartJS.register(ArcElement, Tooltip, Legend)
</script>

<script>
    export default {
        props: {
            responseData: {
                type: Object,
                default: {
                    data: {}
                }
            }
        },
        methods: {
            generateCountryChartData() {
                return {
                    labels: this.responseData.data.country.map(item => item.name),
                    datasets: [
                        {
                            label: 'Probabilité (en %)',
                            backgroundColor: ['#f87979', '#79f8b4', '#79a4f8', '#f879f8', '#f8d679'],
                            data: this.responseData.data.country.map(item => item.probability * 100)
                        }
                    ]
                };
            },
            generateGenderChartData() {
                const genderValue = this.responseData.data.gender.value;
                const genderProbability = this.responseData.data.gender.probability;
                const maleProbability = genderValue === 'female' ? (1 - genderProbability) * 100 : genderProbability * 100;
                const femaleProbability = genderValue === 'female' ? genderProbability * 100 : (1 - genderProbability) * 100;

                return {
                    labels: ["Homme", "Femme"],
                    datasets: [
                        {
                            label: 'Probabilité (en %)',
                            backgroundColor: ['#79a4f8', '#f87979'],
                            data: [maleProbability, femaleProbability]
                        }
                    ]
                };
            },
            getWebMiiUrl() {
                const firstName = encodeURIComponent(this.responseData.args[0]);
                const lastName = encodeURIComponent(this.responseData.args[1]);
                return `https://webmii.com/people?n=%22${firstName}%20${lastName}%22#gsc.tab=0&gsc.q=%22${firstName}%20${lastName}%22&gsc.sort=date`;
            }
        },
        computed: {
            getCountryChartData() {
                return this.generateCountryChartData();
            },
            getGenderChartData() {
                return this.generateGenderChartData();
            }
        }
    }
</script>

<style lang="scss" scoped>
    @import url(../../views/styles/result.scss);
    @import url(./styles/person.scss);
</style>
