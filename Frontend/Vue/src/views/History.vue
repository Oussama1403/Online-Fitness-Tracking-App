<template>
    <div class="dashboard">
      <div class="container-fluid px-4">
        <h2 class="mb-4 mt-4 text-center dash-title fade-in">History</h2>
        <h5 class="mb-4 mt-4 text-center intro-text fade-in">
          Track your completed <span class="intro-important"> goals </span> and <span class="intro-important"> workouts </span>
        </h5>
          
          <h2 class="mt-4 workout-title fade-in">Completed Workouts</h2>
          <hr style="border: 3px solid #ff8640" />
          <div v-if="workouts.length != 0">
            <WorkoutsSection :workouts="workouts" />
          </div>
          <div v-else>
            <h5 class="mb-4 mt-4 text-center workout-title fade-in">
                There are no completed workouts yet.
            </h5>          
          </div>
          
          <h2 class="mt-4 goals-title fade-in">Completed Goals</h2>
          <hr style="border: 3px solid #ff3434" />
          <div v-if="goals.length != 0">
            <GoalsSection :goals="goals" />  
          </div>
          <div v-else>
            <h5 class="mb-4 mt-4 text-center goals-title fade-in">
                There are no completed goals yet.
            </h5>          
          </div>
  
        </div>
      </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  import WorkoutsSection from '@/components/DashboardSections/WorkoutsSection.vue';
  import GoalsSection from '@/components/DashboardSections/GoalsSection.vue';
  
  export default {
    name: 'Dashboard',
  
    components: {
      WorkoutsSection,
      GoalsSection,
    },
  
    data() {
      return {
        workouts: [],
        goals: [],
      }
    },
    created() {
      this.loadData()
    },
    methods: {
      loadData() {

        axios
        .get('http://127.0.0.1:5000/get_workouts')
        .then((response) => {
          this.workouts = response.data.filter(workout => workout.is_done === true)
          console.log('completed workouts :', this.workouts)

        })
        .catch((error) => {
          console.error('There was an error fetching completed workouts!', error)
        })
  
        axios
          .get('http://127.0.0.1:5000/get_goals')
          .then((response) => {
            this.goals = response.data.filter(goal => goal.is_done === true)
            console.log('completed goals :', response.data)
          })
          .catch((error) => {
            console.error('There was an error fetching completed goals!', error)
          })
      },
      
      goToEdit(item, routeName) {
        const clonedItem = JSON.stringify(item)
        console.log('clonedItem :', clonedItem)
        this.$router.push({
          name: routeName,
          query: { item: clonedItem }
        })
      }
    }
  }
  </script>
  
  <style scoped>
  @import "@/assets/SharedCardStyles.css";
  
  .dashboard {
    margin-top: 20px;
    font-family: 'Montserrat', sans-serif;
  }
  
  .dash-title {
    font-size: 36px;
    font-weight: bold;
    color: #57b846;
  }

  .workout-title {
    background: linear-gradient(to bottom right, #fbc848, #fe8b27);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
  }
  
  .goals-title {
    background: linear-gradient(to bottom right, #fb7091, #f73158);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
  }
  
  .intro-text {
  color: #333333;
  padding-bottom: 1rem;
  font-family: 'Montserrat', sans-serif;
  }
  
  .intro-important {
  color: #57b846;
  }
  </style>
  