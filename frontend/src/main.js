import './assets/main.scss';

import { library } from '@fortawesome/fontawesome-svg-core'
import { faBars, faMoon } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

library.add(faBars)
library.add(faMoon)

createApp(App).component("font-awesome-icon", FontAwesomeIcon).use(router).mount("#app");