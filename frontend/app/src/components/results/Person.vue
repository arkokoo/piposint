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
                </div>
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
