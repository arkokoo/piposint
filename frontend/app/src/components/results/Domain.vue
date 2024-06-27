<template>
    <div class="result-bento">
        <div class="bento-item bento-domain-infos" v-if = "responseData.data.data.organization">
            <h3>{{  responseData.data.data.organization }}</h3>
            <p>{{ responseData.data.data.country ? responseData.data.data.country : '' }}{{ responseData.data.data.street ? ' ' + responseData.data.data.street + ',' : '' }}{{ responseData.data.data.postal_code ? ' ' + responseData.data.data.postal_code : '' }}{{ responseData.data.data.city ? ' ' + responseData.data.data.city : '' }}</p>
            <p>{{ responseData.data.data && responseData.data.data.company_type ? responseData.data.data.company_type.charAt(0).toUpperCase() +  responseData.data.data.company_type.slice(1) : '' }}</p>
            <p>{{  responseData.data.data.industry }}</p>
            <p>{{ responseData.data.data.description }}</p>
        </div>
        <div class="bento-item bento-domain-stack" v-if="responseData.data.data.technologies.length > 0">
            <h3>Stack détectée</h3>
            <div class="bento-content">
                <ul>
                    <li v-for="tech in responseData.data.data.technologies" :key="tech">
                        {{ tech.charAt(0).toUpperCase() + tech.slice(1) }}
                    </li>
                </ul>
            </div>
        </div>
        <div class="bento-grid-domain">
            <div v-for="email in responseData.data.data.emails" :key="email" class="bento-item bento-domain-email">
                <h3>{{ email.value }}</h3>
                <div class="bento-content">
                    <div class="bento-content-infos">
                        <span> Confiance : {{ email.confidence }}/100</span>
                        <span> {{ email.position && email.department ? email.department.charAt(0).toUpperCase() + email.department.slice(1) + ' - ' + email.position : email.position ? email.position : email.department ? email.department.charAt(0).toUpperCase() + email.department.slice(1) : String.fromCharCode(8203) }}</span>
                    </div>
                    <span id="bento-email-name">{{ email.first_name && email.last_name ? email.first_name + " " + email.last_name : String.fromCharCode(8203) }}</span>
                </div>
            </div>
         </div>
    </div>
    <div class="bento-empty" v-if="responseData.data.data.emails.length === 0">
      <p>Aucun email trouvé.</p>
    </div>
</template>

<script>
    export default {
        props: {
            responseData: {
                type: Object,
                default: {
                    data: {
                        emails:  []
                    }
                }
            }
        },
    }
</script>

<style lang="scss" scoped>
    @import url(./styles/domain.scss);
    @import url(../../views/styles/result.scss);
</style>