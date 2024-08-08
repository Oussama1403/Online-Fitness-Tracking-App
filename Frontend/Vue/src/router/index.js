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
      /*
      {
        path: '/edit-workout',
        name: 'edit-workout',
        component: EditWorkout, // Your component for editing workouts
        props: (route) => ({ item: JSON.parse(route.params.item) })
      },
      {
        path: '/edit-goal',
        name: 'edit-goal',
        component: EditGoal, // Your component for editing goals
      }*/
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
