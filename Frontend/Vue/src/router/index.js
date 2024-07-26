import { createRouter, createWebHistory } from 'vue-router';
import BaseLayout from '@/layouts/BaseLayout.vue';
import Dashboard from '@/views/Dashboard.vue';

const routes = [
  {
    path: '/',
    component: BaseLayout,
    children: [
      {
        path: '',
        component: Dashboard
      }
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
