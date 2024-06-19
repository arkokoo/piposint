import { createRouter, createWebHistory } from 'vue-router';
import Home from './../views/Home.vue';
import About from './../views/About.vue';
import Tutorials from './../views/Tutorials.vue';
import Search from './../views/Search.vue';
import Result from './../views/Result.vue';

const routes = [
    { path: '/', name: 'Home', component: Home },
    { path: '/about', name: 'About', component: About },
    { path: '/tutorials', name: 'Tutorials', component: Tutorials },
    { path: '/search/:query', name: 'Search', component: Search },
    { path: '/result/:data', name: 'Result', component: Result },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
    scrollBehavior() {
        return { top: 0 };
    },
});

export default router;