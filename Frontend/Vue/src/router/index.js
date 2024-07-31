import { createRouter, createWebHistory } from 'vue-router';
import BaseLayout from '@/layouts/BaseLayout.vue';
import Dashboard from '@/views/Dashboard.vue';
import CreateWorkout from '@/views/CreateWorkout.vue';
import Activities from '@/views/Activities.vue';
import LogActivity from '@/views/LogActivity.vue';
import setFitnessGoal from '@/views/setFitnessGoal.vue';
import EditActivity from '@/views/EditActivity.vue';
import EditWorkout from '@/views/EditWorkout.vue';
import EditGoal from '@/views/EditGoal.vue';



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
