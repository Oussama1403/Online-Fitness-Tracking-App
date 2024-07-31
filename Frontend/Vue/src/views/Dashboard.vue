<template>
  <div class="dashboard">
    <div class="container-fluid px-4">
      <h2 class="mb-4 mt-4 dash-title">Dashboard</h2>
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
      <div class="row">
        <div v-for="(activity, index) in activities" :key="index" class="col-xl-4 col-md-6 mb-4">
          <div class="card activities-section h-100 shadow-sm"  @click="goToEdit(activity, 'edit-activity')">
            <div class="card-body">
              <h5 class="card-title text-center">{{ activity.name }}</h5>
              <p class="card-subtitle mb-1">Date:<br><strong class="details-title">{{ activity.date }}</strong></p>
              <p class="card-text mb-1">Start: <strong class="details-title">{{ activity.startTime }}</strong> - End: <strong class="details-title">{{
                activity.endTime }}</strong></p>
              <p class="card-text mb-1">Duration:<br><strong class="details-title">{{ activity.duration }}</strong></p>
              <p class="card-text mb-1">Distance:<br><strong class="details-title">{{ activity.distance }}</strong></p>
              <p class="card-text mb-1">Calories Burned:<br><strong class="details-title">{{ activity.caloriesBurned }}</strong></p>
            </div>
          </div>
        </div>
      </div>

      <!-- Saved Workouts Section -->
      <h2 class="mb-4 mt-4 workout-title">Upcoming Workouts</h2>
      <div class="row">
        <div v-for="(workout, index) in workouts" :key="index" class="col-xl-4 col-md-6 mb-4">
          <div class="card saved-workouts-section h-100 shadow-sm"  @click="goToEdit(workout, 'edit-workout')">
            <div class="card-body">
              <h5 class="card-title text-center">{{ workout.name }}</h5>
              <h6 class="card-title text-center">{{ workout.date }}</h6>
              <ul class="list-group list-group-flush">
                <li class="list-group-item" v-for="(exercise, index) in workout.exercises" :key="index">
                  <strong class="exercise-name">{{ exercise.name }}</strong>
                  <p>Reps: <strong>{{ exercise.reps }} </strong> <br>Sets: <strong>{{ exercise.sets }} </strong></p>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Current Goals Section -->
      <h2 class="mb-4 mt-4 goals-title">Your Current Goals</h2>
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
export default {
  name: "Dashboard",
  data() {
    return {
      dashboardCards: [
        {
          number: '8',
          text: "WORKOUTS COMPLETED",
          bgColor: "bg-c-blue",
          icon: "fas fa-dumbbell",
        },
        {
          number: '900',
          text: "CALORIES BURNED",
          bgColor: "bg-c-green",
          icon: "fas fa-fire",
        },
        {
          number: '3',
          text: "UPCOMING WORKOUTS",
          bgColor: "bg-c-yellow",
          icon: "fas fa-calendar-alt",
        },
        {
          number: '2',
          text: "GOALS SET",
          bgColor: "bg-c-pink",
          icon: "fas fa-clock",
        },
      ],
      activities: [
        {
          name: "Morning Run",
          date: '2024-07-28',
          startTime: '07:00',
          endTime: '08:00',
          duration: '1 hour',
          distance: '5 km',
          caloriesBurned: '300 kcal',
        },
        {
          name: "Evening Walk",
          date: '2024-07-27',
          startTime: '18:30',
          endTime: '19:30',
          duration: '1 hour',
          distance: '4 km',
          caloriesBurned: '250 kcal',
        },
        {
          name: "Cycling",
          date: '2024-07-26',
          startTime: '06:00',
          endTime: '07:00',
          duration: '1 hour',
          distance: '6 km',
          caloriesBurned: '350 kcal',
        }
      ],
      workouts: [
        {
          name: "Leg Day",
          date: '2024-07-26',
          exercises: [
            { name: "Squats", reps: 12, sets: 4 },
            { name: "Lunges", reps: 15, sets: 3 },
            { name: "Leg Press", reps: 10, sets: 3 },
          ],
        },
        {
          name: "Upper Body",
          date: '2024-07-28',
          exercises: [
            { name: "Bench Press", reps: 10, sets: 4 },
            { name: "Pull-ups", reps: 8, sets: 3 },
            { name: "Bicep Curls", reps: 12, sets: 3 },
          ],
        },
        {
          name: "Cardio",
          date: '2024-07-30',
          exercises: [
            { name: "Running", reps: "N/A", sets: "N/A" },
            { name: "Cycling", reps: "N/A", sets: "N/A" },
            { name: "Jump Rope", reps: "N/A", sets: "N/A" },
          ],
        },
      ],
      goals: [
        {
          type: 'Weight Loss',
          description: 'Lose 5 kg in 2 months',
          currentProgress: '1 kg lost',
          targetDate: '2024-08-30', 
          notes: 'Focus on diet and cardio',
        },
        {
          type: 'Strength',
          description: 'Increase bench press by 20 kg',
          currentProgress: '5 kg increase',
          targetDate: '2024-09-15',
          notes: 'Add more protein to diet',
        }
      ],
    }
  },
  methods: {
  goToEdit(item, routeName) {
    // Clone the item object to strip away Vue's reactivity
    const clonedItem = JSON.stringify(item);
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
  color: rgb(37, 211, 37)
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
  background: linear-gradient(45deg, #a640ff, #af55fd);

}

.activities-section:hover {
  background: linear-gradient(45deg, #8823df, #af55fd);

}

.act-title {
  color: #ab2cd6;
}

.saved-workouts-section {
  background: linear-gradient(45deg, #ff8640, #ff985c);
}

.saved-workouts-section:hover {
  background: linear-gradient(45deg, #ed6a1f, #ff985c);
}

.workout-title {
  color: #ff8640;
}

.current-goals-section {
  background: linear-gradient(45deg, #ed1fe6, #f562f0);

}

.current-goals-section:hover {
  background: linear-gradient(45deg, #d105cb, #f562f0);

}

.goals-title {
  color: #ed1fe6;
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
  border: 2px rgb(255, 255, 255) solid;
  border-radius: 5px;
  color: inherit;
}
</style>
