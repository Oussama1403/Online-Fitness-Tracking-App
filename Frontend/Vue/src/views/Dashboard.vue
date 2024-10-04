<template>
  <div class="dashboard">
    <div class="container-fluid px-4">
      <h2 class="mb-4 pb-4 mt-4 text-center dash-title fade-in">Dashboard</h2>
      <div class="row">
        <div class="col-xl-3 col-md-6 mb-4 fade-in" v-for="(card, index) in dashboardCards" :key="index">
          <div :class="`card ${card.bgColor} text-white h-100`">
            <div class="card-body">
              <div class="card-body-icon">
                <i :class="card.icon"></i>
              </div>
              <h6 class="mr-5">
                <strong style="font-size: 1.4em">{{ card.number }}</strong> {{ card.text }}
              </h6>
            </div>
          </div>
        </div>
        
        <h2 class="mt-4 act-title fade-in">Logged Activities</h2>
        <hr style="border: 3px solid #ab2cd6" />
        <ActivitiesSection :activities="activities" />

        <h2 class="mt-4 workout-title fade-in">Upcoming Workouts</h2>
        <hr style="border: 3px solid #ff8640" />
        <WorkoutsSection :workouts="workouts" />

        <h2 class="mt-4 goals-title fade-in">Your Current Goals</h2>
        <hr style="border: 3px solid #ff3434" />
        <GoalsSection :goals="goals" />
        
        <h2 class="mt-4 meals-title fade-in">Your Logged Meals</h2>
        <hr style="border: 3px solid #f534ff" />
        <MealsSection :meals="meals" />


      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import ActivitiesSection from '@/components/DashboardSections/ActivitiesSection.vue';
import WorkoutsSection from '@/components/DashboardSections/WorkoutsSection.vue';
import GoalsSection from '@/components/DashboardSections/GoalsSection.vue';
import MealsSection from '@/components/DashboardSections/MealsSection.vue';

export default {
  name: 'Dashboard',

  components: {
    ActivitiesSection,
    WorkoutsSection,
    GoalsSection,
    MealsSection
  },

  data() {
    return {
      dashboardCards: [],
      activities: [],
      workouts: [],
      goals: [],
      meals: []
    }
  },
  created() {
    this.loadData()
  },
  methods: {
    loadData() {
      axios
        .get('http://127.0.0.1:5000/get_activities')
        .then((response) => {
          console.log('activities :', response.data)
          this.activities = response.data
          this.updateDashboardCards()
        })
        .catch((error) => {
          console.error('There was an error fetching activities!', error)
        })

      axios
        .get('http://127.0.0.1:5000/get_workouts')
        .then((response) => {
          console.log('workouts :', response.data)
          this.workouts = response.data.filter(workout => workout.is_done === false)
          this.updateDashboardCards()
        })
        .catch((error) => {
          console.error('There was an error fetching workouts!', error)
        })

      axios
        .get('http://127.0.0.1:5000/get_goals')
        .then((response) => {
          console.log('goals :', response.data)
          this.goals = response.data.filter(goal => goal.is_done === false)
          this.updateDashboardCards()
        })
        .catch((error) => {
          console.error('There was an error fetching goals!', error)
        })

      axios
        .get('http://127.0.0.1:5000/get_meals')
        .then((response) => {
          console.log('meals :', response.data)
          this.meals = response.data
          this.updateDashboardCards()
        })
        .catch((error) => {
          console.error('There was an error fetching meals!', error)
        })
    },
    updateDashboardCards() {
      const completedActivities = this.activities.length
      const caloriesBurned = this.activities.reduce((sum, activity) => {
        if (Array.isArray(activity.details)) {
          // Find the entry where the name is "Calories Burned"
          const caloriesEntry = activity.details.find((detail) => detail.name === 'Calories Burned')
          return sum + (caloriesEntry ? parseInt(caloriesEntry.value) : 0)
        } else if (activity.details && activity.details.calories_burned) {
          // Handle the object structure
          return sum + (activity.details.calories_burned.value || 0)
        } else {
          return sum
        }
      }, 0)
      const upcomingWorkouts = this.workouts.length
      const goalsSet = this.goals.length
      // Calculate total active minutes
      const activeMinutes = this.activities.reduce((sum, activity) => {
        // Access the duration detail directly from the details object
        const durationDetail = activity.details['duration']

        if (durationDetail) {
          const value = parseInt(durationDetail.value, 10)
          return sum + value
        }
        return sum
      }, 0)

      this.dashboardCards = [
        {
          number: completedActivities,
          text: 'ACTIVITIES COMPLETED',
          bgColor: 'bg-c-blue',
          icon: 'fas fa-dumbbell'
        },
        {
          number: caloriesBurned,
          text: 'CALORIES BURNED',
          bgColor: 'bg-c-green',
          icon: 'fas fa-fire'
        },
        {
          number: upcomingWorkouts,
          text: 'UPCOMING WORKOUTS',
          bgColor: 'bg-c-yellow',
          icon: 'fas fa-calendar-alt'
        },
        {
          number: goalsSet,
          text: 'GOALS SET',
          bgColor: 'bg-c-red',
          icon: 'fa-solid fa-bullseye'
        },
        {
          number: activeMinutes,
          text: 'TOTAL ACTIVE MINUTES',
          bgColor: 'bg-c-pink', // Choose a color class or define a new one
          icon: 'fas fa-clock' // Choose an appropriate icon
        }
      ]
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
  background: linear-gradient(to right, #1eec63, #5dffbc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;
}

.act-title {
    background: linear-gradient(to bottom right, #c445ff, #1de8ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
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

.meals-title {
    background: linear-gradient(to bottom right, #fa5dff, #ff5f97);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
}

.bg-c-blue {
  background: linear-gradient(45deg, #4099ff, #73b4ff);
}

.bg-c-green {
  background: linear-gradient(45deg, #2ed8b6, #59e0c5);
}

.bg-c-yellow {
  background: linear-gradient(45deg, #ffb64d, #ffcb80);
}

.bg-c-red {
  background: linear-gradient(45deg, #ff5370, #ff869a);
}

.bg-c-pink {
  background: linear-gradient(45deg, #ff53ee, #ff86df);
}
</style>
