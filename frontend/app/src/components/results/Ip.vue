<template>
    <div class="result-bento">
        <div class="bento-grid-ip">
            <div class="bento-item bento-ip-infos">
                <h3>Informations</h3>
                <div class="bento-content">
                    <p>{{ responseData.data.country_flag ? responseData.data.country_flag + ' ' : '' }}{{ responseData.data.country ? responseData.data.country : '' }}</p>
                    <p>{{ responseData.data.regionName ? responseData.data.regionName + ',' : '' }}{{ responseData.data.zip ? ' ' + responseData.data.zip : '' }}{{ responseData.data.city ? ' ' + responseData.data.city : '' }}</p>
                    <p>{{ responseData.data.isp ? "FAI : " + responseData.data.isp : '' }}</p>
                    <p>{{ responseData.data.as ? responseData.data.as : '' }}</p>
                    <p>{{ responseData.data.timezone ? "Timezone : " + responseData.data.timezone : '' }}</p>
                </div>
            </div>
            <div class="bento-item bento-ip-map">
                <h3>Carte</h3>
                <div class="bento-content">
                    <iframe :src="`https://maps.google.com/maps?q=${responseData.data.lat},${responseData.data.lon}&z=15&output=embed`"></iframe>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            responseData: {
                type: Object,
                default: {
                    data: {
                        "as": null,
                        "city": null,
                        "country": null,
                        "country_flag": null,
                        "isp": null,
                        "lat": null,
                        "lon": null,
                        "org": null,
                        "regionName": null,
                        "status": null,
                        "timezone": null,
                        "zip": null
                    }
                }
            }
        },
    }
</script>

<style lang="scss" scoped>
    @import url(./styles/ip.scss);
    @import url(../../views/styles/result.scss);
</style>