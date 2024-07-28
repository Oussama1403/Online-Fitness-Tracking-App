import { createRouter, createWebHistory } from 'vue-router';
import BaseLayout from '@/layouts/BaseLayout.vue';
import Dashboard from '@/views/Dashboard.vue';
import CreateWorkout from '@/views/CreateWorkout.vue';

const routes = [
  {
    path: '/',
    component: BaseLayout,
    children: [
      {
        path: '',
        component: Dashboard
      }, 
      {
        path: 'create-workout',
        component: CreateWorkout
      }
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
