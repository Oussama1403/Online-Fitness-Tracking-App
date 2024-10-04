<template>
  <div class="container custom-container mt-4">
    <Form @submit="handleSubmit" v-slot="{ errors }">
      <div v-if="mode === 'Log'">
        <span class="log-form-title fade-in">
          Create custom <span class="form-title-important">workout routine</span>
        </span>
        <h5 class="mb-4 mt-4 text-center intro-text fade-in">
          Design your personalized workout routine to achieve your
          <span class="intro-important">fitness goals.</span>
        </h5>
      </div>

      <span v-if="mode === 'Edit'" class="edit-form-title fade-in">
        Edit <span class="form-title-important">{{ workoutName }}</span>
      </span>

      <div v-if="errorMessage" class="alert" role="alert">
        {{ errorMessage }}
      </div>

      <div class="fade-in">
        <!-- Workout Name -->
        <div class="form-group">
          <Field
            type="text"
            placeholder="Workout name"
            class="input form-control"
            id="workoutName"
            name="workoutName"
            :value="workoutName"
            @input="updateWorkoutName($event.target.value)"
            rules="required"
          />
          <ErrorMessage name="workoutName" class="error-msg" />
        </div>

        <!-- Workout Date -->
        <div class="form-group">
          <Field
            type="date"
            class="input form-control"
            :id="'workoutDate'"
            name="workoutDate"
            :value="workoutDate"
            @input="updateWorkoutDate($event.target.value)"
            rules="required"
          />
          <ErrorMessage name="workoutDate" class="error-msg" />
        </div>

        <!-- Exercises Section -->
        <div
          v-for="(exercise, index) in exercises"
          :key="index"
          class="exercise-group mb-3 fade-in"
        >
          <div class="form-group">
            <Field
              type="text"
              placeholder="Exercise name"
              class="input form-control"
              :id="'exerciseName' + index"
              v-model="exercise.name"
              :name="'exerciseName' + index"
              rules="required"
            />
            <ErrorMessage :name="'exerciseName' + index" class="error-msg" />
          </div>
          <div class="form-group">
            <Field
              type="number"
              placeholder="Reps"
              class="input form-control"
              :id="'reps' + index"
              v-model="exercise.reps"
              :name="'reps' + index"
              rules="required|numeric"
            />
            <ErrorMessage :name="'reps' + index" class="error-msg" />
          </div>
          <div class="form-group">
            <Field
              type="number"
              placeholder="Sets"
              class="input form-control"
              :id="'sets' + index"
              v-model="exercise.sets"
              :name="'sets' + index"
              rules="required|numeric"
            />
            <ErrorMessage :name="'sets' + index" class="error-msg" />
          </div>
          <button
            type="button"
            class="remove-button btn btn-danger"
            @click="$emit('removeExercise', index)"
          >
            Remove Exercise
          </button>
        </div>

        <!-- Add New Exercise Button -->
        <button type="button" class="add-button btn btn-primary mb-3" @click="$emit('addExercise')">
          Add Another Exercise
        </button>

        <!-- Save Button -->
        <button type="submit" class="save-button btn btn-success">Save Workout</button>
        
        <!-- Mark Done button -->
        <button
          v-if="mode === 'Edit' && isDone === false"
          type="button"
          @click="$emit('markDone')"
          class="markDone-button btn"
        >
          Mark Done
        </button>

        <!-- Mark UnDone button -->
        <button
          v-if="mode === 'Edit' && isDone === true"
          type="button"
          @click="$emit('markUndone')"
          class="markDone-button btn"
        >
          Mark Undone
        </button>

        <!-- Del button -->
        <button
          v-if="mode === 'Edit'"
          type="button"
          @click="$emit('delete')"
          class="delete-button btn btn-danger"
        >
          Delete Workout
        </button>
      </div>
    </Form>
  </div>
</template>

<script>
export default {
  name: 'WorkoutForm',

  props: {
    mode: {
      type: String,
      required: true
    },
    workoutName: {
      type: String,
      required: false
    },
    workoutDate: {
      type: String,
      required: false
    },
    exercises: {
      type: Array,
      required: false
    },
    isDone: {
      type: Boolean,
      required: true
    },
    errorMessage: String
  },

  methods: {
    handleSubmit() {
      this.$emit('submit')
    },

    updateWorkoutName(value) {
      this.$emit('update:workoutName', value) // Emit an event to update the prop
    },

    updateWorkoutDate(value) {
      this.$emit('update:workoutDate', value)
    }
  }
}
</script>

<style scoped>
.intro-text {
  color: #333333;
  padding-bottom: 1rem;
  font-family: 'Montserrat', sans-serif;
}
.intro-important {
  color: #57b846;
}
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

.log-form-title {
  display: block;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  font-size: 1.8em;
  color: #333333;
  line-height: 1.2;
  text-align: center;
}
.edit-form-title {
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
  color: #57b846;
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
  color: white;
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
  background: #393939;
}

.save-button {
  background: #57b846;
}
.delete-button {
  background: #f43333;
}

.markDone-button {
  background: #b846b4;
}

.alert {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
  padding: 10px;
  border-radius: 25px;
  margin-bottom: 20px;
  text-align: center;
  font-family: 'Montserrat', sans-serif;
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
</style>
