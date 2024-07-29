<template>
  <div class="dashboard">
    <div class="container-fluid px-4">
      <h1 class="mb-4 mt-4">Dashboard</h1>
      <div class="row">
        <div class="col-xl-3 col-md-6 mb-4">
          <div class="card bg-primary text-white h-100">
            <div class="card-body">
              <div class="card-body-icon">
                <i class="fas fa-dumbbell"></i>
              </div>
              <div class="mr-5">8 WORKOUTS COMPLETED</div>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-md-6 mb-4">
          <div class="card bg-success text-white h-100">
            <div class="card-body">
              <div class="card-body-icon">
                <i class="fas fa-fire"></i>
              </div>
              <div class="mr-5">500 CALORIES BURNED</div>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-md-6 mb-4">
          <div class="card bg-info text-white h-100">
            <div class="card-body">
              <div class="card-body-icon">
                <i class="fas fa-calendar-alt"></i>
              </div>
              <div class="mr-5">3 WORKOUT PLANS</div>
              <div class="progress progress-sm my-2">
                <div class="progress-bar bg-white" role="progressbar" style="width: 60%" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"></div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-md-6 mb-4">
          <div class="card bg-warning text-white h-100">
            <div class="card-body">
              <div class="card-body-icon">
                <i class="fas fa-clock"></i>
              </div>
              <div class="mr-5">2 UPCOMING WORKOUTS</div>
            </div>
          </div>
        </div>
      </div>
      <!-- activities section -->
      <h1 class="mb-4 mt-4">Logged Activities</h1>
      <div class="row">
        <div v-for="(activity, index) in activities" :key="index" class="col-xl-4 col-md-6 mb-4">
          <div class="card activities-section h-100 shadow-sm">
            <div class="card-body">
              <h5 class="card-title text-center">{{ activity.name +' '+ index }}</h5>
              <h5 class="card-title">{{ activity.date }}</h5>
              <h6 class="card-subtitle mb-2">Start: {{ activity.startTime }} - End: {{ activity.endTime }}</h6>
              <p class="card-text">Duration: {{ activity.duration }}</p>
              <p class="card-text">Distance: {{ activity.distance }}</p>
              <p class="card-text">Calories Burned: {{ activity.caloriesBurned }}</p>
            </div>
          </div>
        </div>
      </div> 
       <!-- Saved Workouts Section -->
       <h1 class="mb-4 mt-4">Saved Workouts</h1>
      <div class="row">
        <div class="col-xl-4 col-md-6 mb-4" v-for="workout in workouts" :key="workout.name">
          <div class="card saved-workouts-section h-100">
            <div class="card-body">
              <h5 class="card-title text-center">{{ workout.name }}</h5>
              <ul class="list-group list-group-flush">
                <li class="list-group-item" v-for="exercise in workout.exercises" :key="exercise.name">
                  <strong>{{ exercise.name }}</strong>
                  <p>Reps: {{ exercise.reps }}<br>
                  Sets: {{ exercise.sets }}</p>
                </li>
              </ul>
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
      activities: [
        {
          name: "Activity Name",
          date: '2024-07-28',
          startTime: '07:00',
          endTime: '08:00',
          duration: '1 hour',
          distance: '5 km',
          caloriesBurned: '300 kcal',
        },
        {
          name: "Activity Name",
          date: '2024-07-27',
          startTime: '08:30',
          endTime: '09:30',
          duration: '1 hour',
          distance: '4 km',
          caloriesBurned: '250 kcal',
        },
        {
          name: "Activity Name",
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
          exercises: [
            { name: "Squats", reps: 12, sets: 4 },
            { name: "Lunges", reps: 15, sets: 3 },
            { name: "Leg Press", reps: 10, sets: 3 },
          ],
        },
        {
          name: "Upper Body",
          exercises: [
            { name: "Bench Press", reps: 10, sets: 4 },
            { name: "Pull-ups", reps: 8, sets: 3 },
            { name: "Bicep Curls", reps: 12, sets: 3 },
          ],
        },
        {
          name: "Cardio",
          exercises: [
            { name: "Running", reps: "N/A", sets: "N/A" },
            { name: "Cycling", reps: "N/A", sets: "N/A" },
            { name: "Jump Rope", reps: "N/A", sets: "N/A" },
          ],
        },
      ],
    }
  }
};
</script>

<style scoped>
.dashboard {
  margin-top: 20px;
}
.card {
  border: none;
  border-radius: 0.75rem;
  transition: all 0.3s ease-in-out;
  color: aliceblue;
}

.card:hover {
  transform: scale(1.05);
}
.activities-section {
  background-color: #c75aec;
}
.activities-section:hover {
  background-color: #ab2cd6;
}
.saved-workouts-section {
  background-color: #8E8FFA;
}
.saved-workouts-section:hover {
  background-color: #5659d2;
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
  border: none;
  color: aliceblue;
}
</style>
