import './assets/main.scss';

import { library } from '@fortawesome/fontawesome-svg-core'
import { faBars, faMoon, faScaleBalanced} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Je mets ça mais ça n'a pas l'air de fonctionner comem je veux, pas sûr de pourquoi
library.add(faBars)
library.add(faMoon)
library.add(faScaleBalanced)

createApp(App).component("font-awesome-icon", FontAwesomeIcon).use(router).mount("#app");