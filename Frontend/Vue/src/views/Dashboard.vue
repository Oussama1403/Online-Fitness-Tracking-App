<template>
  <div class="dashboard">
    <div class="container-fluid px-4">
      <h2 class="mb-4 mt-4 text-center dash-title">Dashboard</h2>
      <hr style="border: 3px solid rgb(37, 211, 37);">
      <div class="row">
        <div class="col-xl-3 col-md-6 mb-4" v-for="(card, index) in dashboardCards" :key="index">
          <div :class="`card ${card.bgColor} text-white h-100`">
            <div class="card-body">
              <div class="card-body-icon">
                <i :class="card.icon"></i>
              </div>
              <h6 class="mr-5"><strong style="font-size: 1.4em;">{{ card.number }}</strong> {{ card.text }}</h6>
            </div>
          </div>
        </div>
      <!-- Activities Section -->
      <h2 class="mb-4 mt-4 act-title">Logged Activities</h2>
      <hr style="border: 3px solid #ab2cd6;">
      <div class="row">
        
        <div v-if="activities.length === 0" class="section">
          <div style="width: 400px;">
          <router-link to="/activities" class="log-activity button btn">Log your first activity!</router-link>
          </div>
        </div>

        <div v-for="(activity, index) in activities" :key="index" class="col-xl-4 col-md-6 mb-4">
          <div class="card activities-section h-100 shadow-sm"  @click="goToEdit(activity, 'edit-activity')">
            <div class="card-body">
              <h5 class="card-title text-center">{{ activity.ActivityName }}</h5>
              <div v-for="(detail, key) in activity.details" :key="key">
                <p class="card-text mb-1">{{ detail.name }}:<br><strong class="details-title">{{ detail.value }}</strong> <strong v-if="detail.unit" class="details-title">{{ detail.unit }}</strong></p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Saved Workouts Section -->
      <h2 class="mb-4 mt-4 workout-title">Upcoming Workouts</h2>
      <hr style="border: 3px solid #ff8640;">
      
      <div v-if="activities.length === 0" class="section">
        <div style="width: 400px;">
          <router-link to="/create-workout" class="log-workout button btn">Log your first workout!</router-link>
        </div>
      </div>
      
      <div class="row">
        <div v-for="(workout, index) in workouts" :key="index" class="col-xl-4 col-md-6 mb-4">
          <div class="card saved-workouts-section h-100 shadow-sm"  @click="goToEdit(workout, 'edit-workout')">
            <div class="card-body">
              <h5 class="card-title text-center">{{ workout.WorkoutName }}</h5>
              <h6 class="card-title text-center">{{ workout.WorkoutDate }}</h6>
              <ul class="list-group list-group-flush">
                <li style="list-style-type: none;" v-for="(exercise, index) in workout.Exercises" :key="index">
                  <div class="list-group-item">
                  <strong class="exercise-name">{{ exercise.name }}</strong>
                  <p>Reps: <strong>{{ exercise.reps }} </strong> <br>Sets: <strong>{{ exercise.sets }} </strong></p>
                </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Current Goals Section -->
      <h2 class="mb-4 mt-4 goals-title">Your Current Goals</h2>
      <hr style="border: 3px solid #ff3434;">
      
      <div v-if="activities.length === 0" class="section">
        <div style="width: 400px;">
          <router-link to="/set-goal" class="log-goal button btn">Log your first goal!</router-link>
        </div>
      </div>
      
      <div class="row">
        <div v-for="(goal, index) in goals" :key="index" class="col-xl-4 col-md-6 mb-4">
          <div class="card current-goals-section h-100 shadow-sm" @click="goToEdit(goal, 'edit-goal')">
            <div class="card-body">
              <h5 class="card-title">{{ goal.type }}</h5>
              <p class="card-text pb-1" style="font-size: 1.1em;font-weight: bold;">{{ goal.description }}</p>
              <p class="card-text mb-1">Target Date: <strong class="details-title">{{ goal.targetDate }}</strong></p>
              <p class="card-text mb-1">Current Progress: <strong class="details-title">{{ goal.currentProgress }}</strong></p>
              <p class="card-text mb-1">Notes: <strong class="details-title">{{ goal.notes }}</strong></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

</template>

<script>
import axios from 'axios';

export default {
  name: "Dashboard",
  data() {
    return {
      dashboardCards: [
        {
          number: 0,
          text: "ACTIVITIES COMPLETED",
          bgColor: "bg-c-blue",
          icon: "fas fa-dumbbell",
        },
        {
          number: 0,
          text: "CALORIES BURNED",
          bgColor: "bg-c-green",
          icon: "fas fa-fire",
        },
        {
          number: 0,
          text: "UPCOMING WORKOUTS",
          bgColor: "bg-c-yellow",
          icon: "fas fa-calendar-alt",
        },
        {
          number: 0,
          text: "GOALS SET",
          bgColor: "bg-c-pink",
          icon: "fas fa-clock",
        },
      ],
      activities: [],
      workouts: [],
      goals: [],
    }
  },
  created() {
    this.loadData();
  },
  methods: {
    loadData() {
      axios.get('http://127.0.0.1:5000/get_activities')
        .then(response => {
          console.log("activities :",response.data)
          this.activities = response.data;
          this.updateDashboardCards();
        })
        .catch(error => {
          console.error('There was an error fetching activities!', error);
        });

      axios.get('http://127.0.0.1:5000/get_workouts')
        .then(response => {
          console.log("workouts :",response.data)
          this.workouts = response.data;
          this.updateDashboardCards();
        })
        .catch(error => {
          console.error('There was an error fetching workouts!', error);
        });

      axios.get('http://127.0.0.1:5000/get_goals')
        .then(response => {
          console.log("goals :",response.data)
          this.goals = response.data;
          this.updateDashboardCards();
        })
        .catch(error => {
          console.error('There was an error fetching goals!', error);
        });
    },
    updateDashboardCards() {
      const completedActivities = this.activities.length;
      const caloriesBurned = this.activities.reduce((sum, activity) => {
        return sum + (activity.details.calories_burned?.value || 0);
      }, 0);
      const upcomingWorkouts = this.workouts.length;
      const goalsSet = this.goals.length;

      this.dashboardCards = [
        {
          number: completedActivities,
          text: "ACTIVITIES COMPLETED",
          bgColor: "bg-c-blue",
          icon: "fas fa-dumbbell",
        },
        {
          number: caloriesBurned,
          text: "CALORIES BURNED",
          bgColor: "bg-c-green",
          icon: "fas fa-fire",
        },
        {
          number: upcomingWorkouts,
          text: "UPCOMING WORKOUTS",
          bgColor: "bg-c-yellow",
          icon: "fas fa-calendar-alt",
        },
        {
          number: goalsSet,
          text: "GOALS SET",
          bgColor: "bg-c-pink",
          icon: "fas fa-clock",
        },
      ];
    },
    goToEdit(item, routeName) {
      const clonedItem = JSON.stringify(item);
      console.log("clonedItem :",clonedItem);
      this.$router.push({
        name: routeName,
        query: { item: clonedItem }
      });
    }
  }
};
</script>


<style scoped>
.dashboard {
  margin-top: 20px;
  font-family: 'Montserrat', sans-serif;
}

.dash-title {
  color: rgb(37, 211, 37);
  font-weight: bold; 
}

.card {
  border-radius: 5px;
  -webkit-box-shadow: 0 1px 2.94px 0.06px rgba(4, 26, 55, 0.16);
  box-shadow: 0 1px 2.94px 0.06px rgba(4, 26, 55, 0.16);
  border: none;
  margin-bottom: 30px;
  -webkit-transition: all 0.3s ease-in-out;
  transition: all 0.3s ease-in-out;
  color: azure;
}

.card:hover {
  transform: scale(1.1);
}
.card-title {
  font-size: 1.5em;
  margin-bottom: 1em;
  font-weight: 700;
}
.details-title {
  font-size: 1.2em;
}
.exercise-name {
  font-size: 1.4em;
}

.order-card {
  color: #fff;
}

.bg-c-blue {
  background: linear-gradient(45deg, #4099ff, #73b4ff);
}

.bg-c-green {
  background: linear-gradient(45deg, #2ed8b6, #59e0c5);
}

.bg-c-yellow {
  background: linear-gradient(45deg, #FFB64D, #ffcb80);
}

.bg-c-pink {
  background: linear-gradient(45deg, #FF5370, #ff869a);
}

.card .card-block {
  padding: 25px;
}

.card .card-body {
  padding: 25px;
}

.order-card i {
  font-size: 26px;
}


.activities-section {
  background: linear-gradient(45deg, #9114ff, #af55fd);

}

.activities-section:hover {
  background: linear-gradient(45deg, #6806be, #af55fd);

}

.act-title {
  color: #ab2cd6;
}

.saved-workouts-section {
  background: linear-gradient(45deg, #fb6c19, #ff985c);
}

.saved-workouts-section:hover {
  background: linear-gradient(45deg, #d75001, #ff985c);
}

.workout-title {
  color: #ff8640;
}

.current-goals-section {
  background: linear-gradient(45deg, #ed1f1f, #f56262);

}

.current-goals-section:hover {
  background: linear-gradient(45deg, #d10505, #f56262);

}

.goals-title {
  color: #ff3434;
}

.card-body-icon {
  position: absolute;
  top: 0.75rem;
  right: 0.75rem;
  opacity: 0.4;
  font-size: 2.5rem;
}

.shadow-sm {
  box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
}

.list-group-item {
  background: none;
  border:0;
  border-bottom: 2px rgb(255, 255, 255) solid;
  color: inherit;
}
.section {
  /* center all elements */
  display: flex;
  justify-content: center;
  align-items: center;
}
.button {
  padding: 16px 32px;
  margin: 4px;
  border: none;
  background: transparent;
  height: 50px;
  width: 100%;
  border-radius: 25px;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  font-size: 15px;
  line-height: 1.5;
  color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 25px;
}

button:hover {
  cursor: pointer;
  box-shadow: none;
}

button:focus {
  background: #626262;
  border-color: #626262;
  box-shadow: none;
  box-shadow: none;
}

.log-activity {
  background: transparent;
  border: 2px solid #da6bff;
  color: #da6bff;
 
}
.log-activity:hover {
  background: #da6bff;
  color: #ffffff;
}
.log-activity:focus {
  background: #bf18f7;
  color: #ffffff;
  border: none;
}

.log-workout {
  background: transparent;
  border: 2px solid #ff8640;
  color: #ff8640;
}
.log-workout:hover {
  background: #ffa16b ;
  color: #ffffff;
}
.log-workout:focus {
  background: #ff7525 ;
  color: #ffffff;
  border: none;
}
.log-goal {
  background: transparent;
  border: 2px solid #ff3434;
  color: #ff3434;
}
.log-goal:hover {
  background: #f54c4c ;
  color: #ffffff;
}
.log-goal:focus {
  background: #ff2a2a ;
  color: #ffffff;
  border: none;
}
</style>
