import { createRouter, createWebHistory } from 'vue-router';
import BaseLayout from '@/layouts/BaseLayout.vue';
import Dashboard from '@/views/Dashboard.vue';
import CreateWorkout from '@/views/CreateWorkout.vue';
import Activities from '@/views/Activities.vue';
import LogActivity from '@/views/LogActivity.vue';
import setFitnessGoal from '@/views/setFitnessGoal.vue';


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
      },
      {
        path: '/activities',
        name: 'Activities',
        component: Activities
      },
      {
        path: '/log-activity/:activityName',
        name: 'LogActivity',
        component: LogActivity,
        props: true
      },
      {
        path: '/set-goal',
        name: 'setFitnessGoal',
        component: setFitnessGoal,
        props: true
      }
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
