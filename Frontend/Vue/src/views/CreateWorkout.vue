<template>
  <div class="container custom-container mt-4">
    <form @submit.prevent="saveWorkout">
      <span class="form-title">
        Create custom workout routine
      </span>
      <!-- Workout Name -->
      <div class="form-group">
        <input type="text" placeholder="Workout name" class="input form-control" id="workoutName" v-model="workoutName"
          required>
      </div>

      <!-- Exercises Section -->
      <div v-for="(exercise, index) in exercises" :key="index" class="exercise-group mb-3">
        <div class="form-group">
          <input type="text" placeholder="Exercise name" class="input form-control" :id="'exerciseName' + index"
            v-model="exercise.name" required>
        </div>
        <div class="form-group">
          <input type="number" placeholder="Reps" class="input form-control" :id="'reps' + index"
            v-model="exercise.reps" required>
        </div>
        <div class="form-group">
          <input type="number" placeholder="Sets" class="input form-control" :id="'sets' + index"
            v-model="exercise.sets" required>
        </div>
        <button type="button" class="remove-button btn btn-danger" @click="removeExercise(index)">Remove
          Exercise</button>
      </div>

      <!-- Add New Exercise Button -->
      <button type="button" class="add-button btn btn-primary mb-3" @click="addExercise">Add Another Exercise</button>

      <!-- Save Button -->
      <button type="submit" class="save-button btn btn-success" @click="saveWorkout">Save Workout</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      workoutName: '',
      exercises: [
        { name: '', reps: '', sets: '' } // Initial exercise fields
      ]
    };
  },
  methods: {
    addExercise() {
      this.exercises.push({ name: '', reps: '', sets: '' });
    },
    removeExercise(index) {
      this.exercises.splice(index, 1);
    },
    saveWorkout() {
      // Handle form submission
      console.log('Workout Name:', this.workoutName);
      console.log('Exercises:', this.exercises);
      // You can add code here to save the workout data
    }
  }
};
</script>

<style scoped>
.custom-container {
  overflow: hidden;
  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;

}

form {
  width: 500px;
}

.form-title {
  display: block;
  font-family: 'Montserrat', sans-serif;
  font-size: 24px;
  color: #333333;
  line-height: 1.2;
  text-align: center;
  padding-bottom: 44px;
}

.exercise-group {
  padding-top: 2rem;
  padding-bottom: 2rem;
  border-radius: 5px;
}

.input {
  background: #e6e6e6;
  font-family: 'Montserrat', sans-serif;
  font-size: 15px;
  line-height: 1.5;
  color: #666666;
  outline: none;
  height: 50px;
  border-radius: 25px;
  padding: 0 30px;
}

.input::placeholder {
  color: #a19f9f;
}

button {
  padding: 16px 32px;
  margin: 4px;
  border: none;
  background: transparent;
  height: 50px;
  width: 100%;
  border-radius: 25px;
  font-family: 'Montserrat', sans-serif;
  font-size: 15px;
  line-height: 1.5;
  color: #fff;
  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 25px;

  -webkit-transition: all 0.4s;
  -o-transition: all 0.4s;
  -moz-transition: all 0.4s;
  transition: all 0.4s;
}

button:hover {
  cursor: pointer;
  background: #333333;
}

button:focus {
  background: #626262;
  border-color: #626262;
  box-shadow: none;

}

.remove-button {
  background: #f43333;
}

.add-button {
  background: #57b846;
}

.save-button {
  background: #57b846;
}
</style>