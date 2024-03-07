import { createRouter, createWebHistory } from 'vue-router';
import Home from './../views/Home.vue';
import About from './../views/About.vue';
import Tutorials from './../views/Tutorials.vue';

const routes = [
    { path: '/', name: 'Home', component: Home },
    { path: '/about', name: 'About', component: About },
    { path: '/tutorials', name: 'Tutorials', component: Tutorials },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;