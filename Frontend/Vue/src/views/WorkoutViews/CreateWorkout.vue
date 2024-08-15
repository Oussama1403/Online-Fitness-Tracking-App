<template>
  <div class="container custom-container mt-4">
    <Form @submit="saveWorkout" v-slot="{ errors }">
      <span class="form-title">
        Create custom <span class="form-title-important">workout routine</span>
      </span>

      <!-- Workout Name -->
      <div class="form-group">
        <Field type="text" placeholder="Workout name" class="input form-control" id="workoutName" name="workoutName"
          v-model="workoutName" rules="required" />
        <ErrorMessage name="workoutName" class="error-msg" />
      </div>

      <div class="form-group">
        <Field type="date" class="input form-control" :id="'workoutDate'" name="workoutDate" v-model="workoutDate"
          rules="required" />
        <ErrorMessage name="workoutDate" class="error-msg" />
      </div>

      <!-- Exercises Section -->
      <div v-for="(exercise, index) in exercises" :key="index" class="exercise-group mb-3">
        <div class="form-group">
          <Field type="text" placeholder="Exercise name" class="input form-control" :id="'exerciseName' + index"
            v-model="exercise.name" :name="'exerciseName' + index" rules="required" />
          <ErrorMessage :name="'exerciseName' + index" class="error-msg" />
        </div>
        <div class="form-group">
          <Field type="number" placeholder="Reps" class="input form-control" :id="'reps' + index"
            v-model="exercise.reps" :name="'reps' + index" rules="required|numeric" />
          <ErrorMessage :name="'reps' + index" class="error-msg" />
        </div>
        <div class="form-group">
          <Field type="number" placeholder="Sets" class="input form-control" :id="'sets' + index"
            v-model="exercise.sets" :name="'sets' + index" rules="required|numeric" />
          <ErrorMessage :name="'sets' + index" class="error-msg" />
        </div>
        <button type="button" class="remove-button btn btn-danger" @click="removeExercise(index)">Remove
          Exercise</button>
      </div>

      <!-- Add New Exercise Button -->
      <button type="button" class="add-button btn btn-primary mb-3" @click="addExercise">Add Another Exercise</button>

      <!-- Save Button -->
      <button type="submit" class="save-button btn btn-success">Save Workout</button>
    </Form>
  </div>
</template>

<script>
import axios from 'axios';
import { v4 as uuidv4 } from 'uuid';
import { jwtDecode } from "jwt-decode";


export default {
  data() {
    return {
      workoutName: '',
      workoutDate: '',
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
      if (this.exercises.length > 1) {
        this.exercises.splice(index, 1);
      }
    },
    saveWorkout() {
      // Get user Id
      const token = localStorage.getItem('authToken');
      const decoded = jwtDecode(token);
      const userId = decoded.user_id;

      let data = {
        _id: uuidv4(),
        user_id: userId,
        'WorkoutName': this.workoutName,
        'WorkoutDate': this.workoutDate,
        'Exercises': this.exercises
      }
      axios.post('http://127.0.0.1:5000/log_workout', data)
        .then(response => {
          console.log('Workout logged:', response.data);
          alert('Workout logged successfully!');
          this.$router.push('/');
        })
        .catch(error => {
          console.error('There was an error logging the workout!', error);
          alert('There was an error logging the workout!');
        });

    }
  }
};
</script>

<style scoped>
.error-msg {
  color: red;
  font-size: 0.875rem;
  margin-top: 0.25rem;
}

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
  font-weight: 700;
  font-size: 24px;
  color: #333333;
  line-height: 1.2;
  text-align: center;
  padding-bottom: 44px;
}

.form-title-important {
  color: #57B846;
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
.input:hover {
  border: 1px solid #00ff99;
}
.input:focus {
  box-shadow: 0 0 0 0.2rem #00ff99;
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
  font-weight: 700;

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