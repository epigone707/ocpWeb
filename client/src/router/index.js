import Vue from 'vue';
import Router from 'vue-router';
import Books from '../components/Books.vue';
import Ping from '../components/Ping.vue';
import Home from '../components/Home.vue';
import Help from '../components/Help.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/books',
      name: 'Books',
      component: Books,
    },
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/help',
      name: 'Help-page',
      component: Help,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
