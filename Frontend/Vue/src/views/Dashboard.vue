<template>
  <div class="dashboard">
    <div class="container-fluid px-4">
      <h2 class="mb-4 mt-4 text-center dash-title fade-in">Dashboard</h2>
      <hr style="border: 3px solid #1eec63;">
      <div class="row">
        <div class="col-xl-3 col-md-6 mb-4 fade-in" v-for="(card, index) in dashboardCards" :key="index">
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
        <h2 class="mb-4 mt-4 act-title fade-in">Logged Activities</h2>
        <hr style="border: 3px solid #ab2cd6;">
        <div class="row">

          <div v-if="activities.length === 0" class="section">
            <div style="width: 400px;">
              <router-link to="/activities" class="log-activity button btn fade-in">Log your first
                activity!</router-link>
            </div>
          </div>

          <div v-for="(activity, index) in activities" :key="index" class="col-xl-4 col-md-6 mb-4 fade-in">
            <!-- for cards to be on the same height, add h-100 to card class -->
            <div class="card activities-section" @click="goToEdit(activity, 'edit-activity')">
              <div class="card-body">
                <h5 class="card-title text-center">{{ activity.ActivityName }}</h5>
                <div v-for="(detail, key) in activity.details" :key="key">
                  <p class="card-text mb-1">{{ detail.name }}:<br>
                    <strong class="details-title">{{ detail.name === 'Duration' ? detail.stringValue : detail.value
                      }}</strong>
                    <strong v-if="detail.unit" class="details-title">{{ detail.unit }}</strong>
                  </p>
                  <hr>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Saved Workouts Section -->
        <h2 class="mb-4 mt-4 workout-title fade-in">Upcoming Workouts</h2>
        <hr style="border: 3px solid #ff8640;">

        <div v-if="workouts.length === 0" class="section fade-in">
          <div style="width: 400px;">
            <router-link to="/create-workout" class="log-workout button btn">Log your first workout!</router-link>
          </div>
        </div>
        <div class="row">
          <div v-for="(workout, index) in workouts" :key="index" class="col-xl-4 col-md-6 mb-4 fade-in">
            <!-- for cards to be on the same height, add h-100 to card class -->
            <div class="card saved-workouts-section" @click="goToEdit(workout, 'edit-workout')">
              <div class="card-body">
                <h5 class="card-title text-center">{{ workout.WorkoutName }}</h5>
                <h6 class="text-center" style="font-size: 1.2em;margin-bottom: 1em;font-weight: 700;">{{
                  workout.WorkoutDate }}</h6>
                <ul class="list-group list-group-flush">
                  <li style="list-style-type: none;" v-for="(exercise, index) in workout.Exercises" :key="index">
                    <div class="list-group-item">
                      <div class="exercise">
                        <strong class="exercise-name">{{ exercise.name }}</strong>
                        <p>Reps: <strong>{{ exercise.reps }} </strong> <br>Sets: <strong>{{ exercise.sets }} </strong>
                        </p>
                      </div>
                    </div>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <!-- Current Goals Section -->
        <h2 class="mb-4 mt-4 goals-title fade-in">Your Current Goals</h2>
        <hr style="border: 3px solid #ff3434;">

        <div v-if="goals.length === 0" class="section fade-in">
          <div style="width: 400px;">
            <router-link to="/set-goal" class="log-goal button btn">Log your first goal!</router-link>
          </div>
        </div>

        <div class="row">
          <div v-for="(goal, index) in goals" :key="index" class="col-xl-4 col-md-6 mb-4 fade-in">
            <!-- for cards to be on the same height, add h-100 to card class -->
            <div class="card current-goals-section" @click="goToEdit(goal, 'edit-goal')">
              <div class="card-body">
                <h5 class="card-title">{{ goal.type }}</h5>
                <p class="card-text pb-1" style="font-size: 1.1em;font-weight: bold;">{{ goal.description }}</p>
                <p class="card-text mb-1">Target Date: <strong class="details-title">{{ goal.targetDate }}</strong></p>
                <p class="card-text mb-1">Current Progress: <strong class="details-title">{{ goal.currentProgress
                    }}</strong></p>
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
      dashboardCards: [],
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
          console.log("activities :", response.data)
          this.activities = response.data;
          this.updateDashboardCards();
        })
        .catch(error => {
          console.error('There was an error fetching activities!', error);
        });

      axios.get('http://127.0.0.1:5000/get_workouts')
        .then(response => {
          console.log("workouts :", response.data)
          this.workouts = response.data;
          this.updateDashboardCards();
        })
        .catch(error => {
          console.error('There was an error fetching workouts!', error);
        });

      axios.get('http://127.0.0.1:5000/get_goals')
        .then(response => {
          console.log("goals :", response.data)
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
        if (Array.isArray(activity.details)) {
          // Find the entry where the name is "Calories Burned"
          const caloriesEntry = activity.details.find(detail => detail.name === "Calories Burned");
          return sum + (caloriesEntry ? parseInt(caloriesEntry.value) : 0);
        } else if (activity.details && activity.details.calories_burned) {
          // Handle the object structure
          return sum + (activity.details.calories_burned.value || 0);
        } else {
          return sum;
        }
      }, 0);
      const upcomingWorkouts = this.workouts.length;
      const goalsSet = this.goals.length;
      // Calculate total active minutes
      const activeMinutes = this.activities.reduce((sum, activity) => {
        // Access the duration detail directly from the details object
        const durationDetail = activity.details['duration'];

        if (durationDetail) {
          const value = parseInt(durationDetail.value, 10);
          return sum + value;
        }
        return sum;
      }, 0);

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
        {
          number: activeMinutes,
          text: "TOTAL ACTIVE MINUTES",
          bgColor: "bg-c-pink", // Choose a color class or define a new one
          icon: "fas fa-clock",   // Choose an appropriate icon
        },
      ];
    },
    goToEdit(item, routeName) {
      const clonedItem = JSON.stringify(item);
      console.log("clonedItem :", clonedItem);
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
  font-size: 36px;
  font-weight: bold;
  background: linear-gradient(to right, #1eec63, #5dffbc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;
}

.card {
  border-radius: 25px;
  box-shadow: 5px 5px 10px -3px rgb(201, 198, 198);
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
  letter-spacing: 0.1rem;
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
  background: linear-gradient(135deg, #9114ff, #d666ed);
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding: 5px;
  /* Optional: Spacing inside the card */
}

.activities-section:hover {
  background: linear-gradient(135deg, #9114ff, #9114ff);

}

.act-title {
  background: linear-gradient(to right, #9114ff, #d666ed);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;
}

.saved-workouts-section {
  background: linear-gradient(135deg, #ff640a, #ff4343);
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding: 5px;
  /* Optional: Spacing inside the card */
}

.saved-workouts-section:hover {
  background: linear-gradient(135deg, #ff640a, #ff640a);
}

.workout-title {
  background: linear-gradient(to right, #ff640a, #ff4343);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;
}

.current-goals-section {
  background: linear-gradient(135deg, #fa1818, #f56262);
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  padding: 5px;
  /* Optional: Spacing inside the card */

}

.current-goals-section:hover {
  background: linear-gradient(135deg, #fa1818, #fa1818);

}

.goals-title {
  background: linear-gradient(to right, #fa1818, #f56262);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;
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
  border: 0;
  color: inherit;
}

.exercise {
  border-bottom: 1px rgb(255, 255, 255) solid;
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
  background: #ffa16b;
  color: #ffffff;
}

.log-workout:focus {
  background: #ff7525;
  color: #ffffff;
  border: none;
}

.log-goal {
  background: transparent;
  border: 2px solid #ff3434;
  color: #ff3434;
}

.log-goal:hover {
  background: #f54c4c;
  color: #ffffff;
}

.log-goal:focus {
  background: #ff2a2a;
  color: #ffffff;
  border: none;
}


/* Define the fade-in animation */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Apply the fade-in animation to elements */
.fade-in {
  opacity: 0;
  animation: fadeIn 1s ease-out forwards;
}

/* Staggered animation delay for sequential appearance */
.fade-in:nth-child(1) {
  animation-delay: 0.5s;
}

.fade-in:nth-child(2) {
  animation-delay: 0.8s;
}

.fade-in:nth-child(3) {
  animation-delay: 1.1s;
}

.fade-in:nth-child(4) {
  animation-delay: 1.4s;
}

.fade-in:nth-child(5) {
  animation-delay: 1.7s;
}

/* Adjust delays as needed for more items */
</style>
