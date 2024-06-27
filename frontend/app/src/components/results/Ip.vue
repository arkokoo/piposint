<template>
    <div class="result-bento">
        <div class="bento-item bento-ip-infos">
            <h3>Informations</h3>
        </div>
    </div>
    <pre>{{ responseData.data }}</pre>
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