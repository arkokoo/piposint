import './assets/main.scss';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App).component("font-awesome-icon", FontAwesomeIcon).use(router).mount("#app");