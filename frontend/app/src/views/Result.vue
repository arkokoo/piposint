<template>
    <section class="container" style="padding-top: 8rem;">
        <div class="result-header">
          <div class="result-icon">
            <User v-if="responseData.type === 'person'" />
            <AtSign v-if="responseData.type === 'email'" />
            <Drama v-if="responseData.type === 'username'" />
            <MapPin v-if="responseData.type === 'ip'" />
            <Phone v-if="responseData.type === 'phone'" />
            <Globe v-if="responseData.type === 'domain'" />
          </div>
          <h1 class="result-title">{{ result_types[responseData.type] }}</h1>
          <h2 class="result-args">{{ responseData.args.join(', ') }}</h2>
          <p class="result-description" v-if="responseData.datetime" >{{ formatDatetime(responseData.datetime) }}</p>
        </div>
        <BentoPerson v-if="responseData.type === 'person'" :responseData="responseData" />
        <BentoEmail v-if="responseData.type === 'email'" :responseData="responseData" />
        <BentoUsername v-if="responseData.type === 'username'" :responseData="responseData" />
        <BentoIp v-if="responseData.type === 'ip'" :responseData="responseData" />
        <BentoPhone v-if="responseData.type === 'phone'" :responseData="responseData" />
        <BentoDomain v-if="responseData.type === 'domain'" :responseData="responseData" />
    </section>
</template>

<script setup>
  import { Phone, Globe, MapPin, User, AtSign, Drama } from 'lucide-vue-next';
  import BentoPerson from '@/components/results/Person.vue';
  import BentoEmail from '@/components/results/Email.vue';
  import BentoUsername from '@/components/results/Username.vue';
  import BentoIp from '@/components/results/Ip.vue';
  import BentoPhone from '@/components/results/Phone.vue';
  import BentoDomain from '@/components/results/Domain.vue';
</script>

<script>
export default {
  watch: {
    '$route.params.data': {
      immediate: true,
      handler(newData) {
       this.responseData = JSON.parse(newData);
      },
    },
  },
  data() {
    return {
      responseData: null,
      result_types: {
        person: 'Personne',
        email: 'Email',
        username: 'Pseudo',
        ip: 'Adresse IP',
        phone: 'Téléphone',
        domain: 'Domaine',
      },
    };
  },
  created() {
    this.responseData = JSON.parse(this.$route.params.data);
  },
  methods: {
    formatDatetime(datetime) {
      return new Date(datetime).toLocaleString(undefined, { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' });
    },
  },
}
</script>

<style lang="scss" scoped>
@import url(./styles/result.scss);
</style>
