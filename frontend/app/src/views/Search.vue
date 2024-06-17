<template>
  <ErrorPopup :error="error" />
  <Loader :isLoading="isLoading" />
  <section class="container" style="padding-top: 8rem;">
    <div class="search-form">
      <div class="search-icon">
        <User v-if="query === 'person'" />
        <AtSign v-if="query === 'email'" />
        <Drama v-if="query === 'username'" />
        <MapPin v-if="query === 'ip'" />
        <Phone v-if="query === 'phone'" />
        <Globe v-if="query === 'domain'" />
      </div>
      <h1 class="search-title">{{ search_types[query] }}</h1>
      <input type="text" name="search-email" :placeholder="placeholders.email" @keyup.enter="sendSearch" placeholder v-if="query === 'email'" @input="checkEmail" :id="param_1.is_valid === false ? 'bad-input' : ''"/>
      <input type="text" name="search-ip" :placeholder="placeholders.ip" @keyup.enter="sendSearch" v-if="query === 'ip'" @input="checkIpAddress" :id="param_1.is_valid === false ? 'bad-input' : ''"/>
      <input type="text" name="search-phone" :placeholder="placeholders.phone" @keyup.enter="sendSearch" v-if="query === 'phone'" @input="checkPhone" :id="param_1.is_valid === false ? 'bad-input' : ''"/>
      <input type="text" name="search-username" :placeholder="placeholders.username" @keyup.enter="sendSearch" v-if="query === 'username'" @input="checkUsername" :id="param_1.is_valid === false ? 'bad-input' : ''"/>
      <input type="text" name="search-domain" :placeholder="placeholders.domain" @keyup.enter="sendSearch" v-if="query === 'domain'"/>
      <input type="text" name="search-firstname" :placeholder="placeholders.firstname" @keyup.enter="sendSearch" v-if="query === 'person'" @input="checkFirstname" :id="param_1.is_valid === false ? 'bad-input' : ''"/>
      <input type="text" name="search-lastname" :placeholder="placeholders.lastname" @keyup.enter="sendSearch" v-if="query === 'person'" @input="checkLastname" :id="param_2.is_valid === false ? 'bad-input' : ''"/>
      <button class="search-button" @click="sendSearch" :id="param_1.is_valid && (query !== 'person' || (query === 'person' && param_2.is_valid)) ? '' : 'bad-input'">
        Valider
      </button>
    </div>
  </section>
</template>

<script setup>
import { Phone, Globe, MapPin, User, X, AtSign, Drama } from 'lucide-vue-next';
import ErrorPopup from '@/components/ErrorPopup.vue';
import Loader from '@/components/Loader.vue';
</script>

<script>
export default {
  data() {
    return {
      isLoading: false,
      error: {
        code: null,
        message: ''
      },
      query: null,
      param_1: {
        value: '',
        is_valid: null,
      },
      param_2: {
        value: '',
        is_valid: null,
      },
      search_types: {
        person: 'Personne',
        email: 'Email',
        username: 'Pseudo',
        ip: 'Adresse IP',
        phone: 'Téléphone',
        domain: 'Domaine',
      },
      placeholders: {
        email: 'Email',
        ip: 'Adresse IP',
        phone: 'N° de téléphone',
        username: 'Pseudo',
        domain: 'Domaine',
        firstname: 'Prénom',
        lastname: 'Nom',
      },
    };
  },

  mounted() {
    this.query = this.$route.params.query;
  },
  methods: {
    sendSearch() {
        if (this.param_1.is_valid && (this.query !== 'person' || (this.query === 'person' && this.param_2.is_valid))) {
          switch (this.query) {
            case 'person':
              this.fetchHandler(`/api/person?firstname=${this.param_1.value}&lastname=${this.param_2.value}`);
              break;
            case 'ip':
              this.fetchHandler(`/api/ip?value=${this.param_1.value}`);
              break;
            case 'phone':
              this.fetchHandler(`/api/phone?value=${this.param_1.value}`);
              break;
            case 'username':
              this.fetchHandler(`/api/username?value=${this.param_1.value}`);
              break;
            case 'email':
              this.fetchHandler(`/api/email?value=${this.param_1.value}`);
              break;
            case 'domain':
              this.fetchHandler(`/api/domain?value=${this.param_1.value}`);
              break;
          }
        }
      },
      fetchHandler(url) {
        this.isLoading = true;
        this.error.code = null;
        this.error.message = '';
        fetch(url, {
        })
          .then(response => {
            this.isLoading = false;
            if (response.ok) {
              return response.json();
            } else {
              this.error.code = response.status;
              this.error.message = response.statusText;
            }
          })
          .then(data => {
            if (data) {
              console.log(data);
            }
          })
          .catch(err => {
            this.isLoading = false;
            this.error.code = 500;
            this.error.message = 'Internal server error';
          });
      },
      checkFirstname(event) {
        const firstname = event.target.value;
        const firstnameRegex = /^[a-zA-Z\s-]+$/;

        this.param_1.value = firstname;
        this.param_1.is_valid = firstnameRegex.test(firstname);
      },
      checkLastname(event) {
        const lastname = event.target.value;
        const lastnameRegex = /^[a-zA-Z\s-]+$/;

        this.param_2.value = lastname;
        this.param_2.is_valid = lastnameRegex.test(lastname);
      },
      checkIpAddress(event) {
        const ipAddress = event.target.value;
        const ipv4Regex = /^([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?<!172\.(16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31))(?<!127)(?<!^10)(?<!^0)\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(?<!192\.168)(?<!172\.(16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31))\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$/;
        //TODO: voir pour retirer ipv6Regex
        const ipv6Regex = /(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))/;
        const domainRegex = /[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/;
        
        
        this.param_1.value = ipAddress;
        this.param_1.is_valid = ipv4Regex.test(ipAddress) || ipv6Regex.test(ipAddress) || domainRegex.test(ipAddress);
      },
      checkPhone(event) {
        const phone = event.target.value;
        const phoneRegex = /^\+?[0-9]{9,14}$/;

        this.param_1.value = phone;
        this.param_1.is_valid = phoneRegex.test(phone);
      },
      checkUsername(event) {
        const username = event.target.value;
        const usernameRegex = /^[^()'"`]{1,30}$/;

        this.param_1.value = username;
        this.param_1.is_valid = usernameRegex.test(username);
      },
      checkEmail(event) {
        const email = event.target.value;
        const emailRegex = /^[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]{1,253}\.[a-zA-Z]{2,}$/;
        this.param_1.value = email;
        this.param_1.is_valid = emailRegex.test(email);
      },
  },
};
</script>

<style lang="scss" scoped>
@import url(./styles/search.scss);
</style>
