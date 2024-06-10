<template>
    <div class="history">
        <div class="history-buttons">
            <ul>
                <li>
                    <button id="history-refresh" @click="updateHistory" title="Rafraîchir"><RefreshCw alt="Rafraîchir"/></button>
                </li>
                <li>
                    <button id="history-filter" @click="switchFilter" title="Filtrer">{{ history_filters_name[filterId] }}</button>
                </li>
                <li>
                    <button title="Télécharger"><Download alt="Télécharger"/></button>
                    <button title="Importer"><Import alt="Importer"/></button>
                    <button title="Nettoyer"><Eraser alt="Nettoyer" @click="deleteHistory" /></button>
                </li>
            </ul>
        </div>
        <div class="history-message" v-if="error">{{ error }}</div>
        <div class="history-message" v-else-if="Object.keys(history).length === 0">Aucune donnée à afficher.</div>
        <div v-else class="history-yearbox" v-for="(year, yearIndex) in Object.keys(history).sort((a, b) => Number(b) - Number(a))" :key="yearIndex">
            <h1 v-if="yearIndex !== 0" class="year-separator">{{ year }}</h1>
            <div class="history-monthbox" v-for="(month, monthIndex) in Object.keys(history[year]).sort((a, b) => Number(b) - Number(a))" :key="monthIndex">
                <h2 class="month-separator">{{ months[Number(month)] }}</h2>
                <div class="history-daybox" v-for="(day, dayIndex) in Object.keys(history[year][month]).sort((a, b) => Number(b) - Number(a))" :key="dayIndex">
                    <span class="day-separator">{{ day }}</span>
                    <div class="item" v-for="(item, itemIndex) in history[year][month][day]" :key="itemIndex">
                        <div class="item-delete" @click="deleteItem(item.uuid)">
                            <X/>
                        </div>
                        <div class="item-box" @click="fetchItem(item.type, item.uuid)">
                            <div class="item-infos">
                                <ul class="item-args">
                                    <li v-for="(arg, index) in item.args" :key="index">{{ arg }}{{ index !== item.args.length - 1 ? ',' : '' }}</li>
                                </ul>
                                <span id="item-hours">{{ item.hours }}</span>
                            </div>
                            <div id="item-icon">
                                <User v-if="item.type === 'person'"/>
                                <AtSign v-if="item.type === 'email'"/>
                                <Drama v-if="item.type === 'username'"/>
                                <MapPin v-if="item.type === 'ip'"/>
                                <Phone v-if="item.type === 'phone'"/>
                                <Globe v-if="item.type === 'domain'"/>
                                <MapPinned v-if="item.type === 'overpass-turbo'"/>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script setup>
    import { Phone, Globe, MapPin, User, MapPinned, X, AtSign, Drama, RefreshCw, Download, Import, Eraser } from 'lucide-vue-next';
    import { fetchHistory } from '@/components/functions/fetchHistory';
</script>

<script>
    
    export default {
        data() {
            return {
                items: [],
                history: {},
                filterId: 0,
                error: null,
                history_filters_name: [
                    "Tous",
                    "Personne",
                    "Email",
                    "Pseudo",
                    "IP",
                    "Téléphone",
                    "Domaine",
                    "Overpass-turbo",
                ],

                months : {
                1: 'Janvier',
                2: 'Février',
                3: 'Mars',
                4: 'Avril',
                5: 'Mai',
                6: 'Juin',
                7: 'Juillet',
                8: 'Août',
                9: 'Septembre',
                10: 'Octobre',
                11: 'Novembre',
                12: 'Décembre',
                },
            };
        },
        created() {
            this.updateHistory();
        },
        methods: {
            async updateHistory() {
                this.history = await fetchHistory(this.history, this.filterId);
            },
            fetchItem(param_type, param_uuid) {
                if (param_type === 'overpass-turbo') {
                    this.fetchOverpassData(param_uuid);
                } else {
                    console.log("not implemented yet");
                }
            },
            fetchOverpassData(param_uuid) {
                fetch(`/api/history/${param_uuid}`)
                    .then((response) => response.json())
                    .then((data) => {
                        window.open(data.data.url, '_blank');
                    })
                    .catch((error) => {
                        console.error('Error:', error);
                    });
            },
            deleteItem(param_uuid) {
                fetch(`/api/history/${param_uuid}`, {
                    method: 'DELETE',
                })
                    .then((response) => response.json())
                    .then((data) => {
                        this.updateHistory();
                    })
                    .catch((error) => {
                        console.error('Error:', error);
                    });
            },
            deleteHistory(){
                // Js popup to confirm the deletion
                if (!confirm("Voulez-vous vraiment supprimer tout l'historique ?")) {
                    return;
                }

                fetch('/api/history', {
                    method: 'DELETE',
                })
                    .then((response) => response.json())
                    .then((data) => {
                        this.updateHistory();
                    })
                    .catch((error) => {
                        console.error('Error:', error);
                    });
            },
            switchFilter() {
                if (this.filterId < 7) {
                    this.filterId += 1;
                } else {
                    this.filterId = 0;
                }
                this.updateHistory();
            },
        },
    };
</script>

<style lang="scss" scoped>
@import url(./styles/history.scss);
</style>