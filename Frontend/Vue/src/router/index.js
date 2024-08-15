import { createRouter, createWebHistory } from 'vue-router';
import BaseLayout from '@/layouts/BaseLayout.vue';
import Dashboard from '@/views/Dashboard.vue';

import CreateWorkout from '@/views/WorkoutViews/CreateWorkout.vue';
import EditWorkout from '@/views/WorkoutViews/EditWorkout.vue';

import Activities from '@/views/ActivityViews/Activities.vue';
import LogActivity from '@/views/ActivityViews/LogActivity.vue';
import EditActivity from '@/views/ActivityViews/EditActivity.vue';
import CustomActivity from '@/views/ActivityViews/CustomActivity.vue';

import setFitnessGoal from '@/views/GoalViews/setFitnessGoal.vue';
import EditGoal from '@/views/GoalViews/EditGoal.vue';

import Login from '@/views/Auth/Login.vue';
import Register from '@/views/Auth/Register.vue';




const routes = [
  {
    path: '/',
    component: BaseLayout,
    meta: { requiresAuth: true },  // Protect the entire BaseLayout routes
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
        path: '/custom-activity/:activityName',
        name: 'CustomActivity',
        component: CustomActivity,
        props: true
      },
      {
        path: '/set-goal',
        name: 'setFitnessGoal',
        component: setFitnessGoal,
        props: true
      },
      {
        path: '/edit-activity',
        name: 'edit-activity',
        component: EditActivity,
      },
      {
        path: '/edit-workout',
        name: 'edit-workout',
        component: EditWorkout,
      },
      {
        path: '/edit-goal',
        name: 'edit-goal',
        component: EditGoal,
      }
    ]
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  const isAuthenticated = !!localStorage.getItem('authToken'); 

  if (requiresAuth && !isAuthenticated) {
    next('/login');
  } else {
    next();
  }
});

export default router;
