<template>
  <WorkoutForm
    :mode="'Log'"
    :workoutName="workoutName"
    :workoutDate="workoutDate"
    :exercises="exercises"
    :errorMessage="errorMessage"
    @update:workoutName="updateWorkoutName"
    @update:workoutDate="updateWorkoutDate"
    @submit="saveWorkout"
    @addExercise="addExercise"
    @removeExercise="removeExercise"
  />
</template>

<script>
import axios from 'axios'
import { v4 as uuidv4 } from 'uuid'
import { jwtDecode } from 'jwt-decode'

import WorkoutForm from '@/components/WorkoutForm.vue'

export default {
  name: 'CreateWorkout',

  components: {
    WorkoutForm
  },
  data() {
    return {
      workoutName: '',
      workoutDate: '',
      exercises: [
        { name: '', reps: '', sets: '' } // Initial exercise fields
      ],
      errorMessage: ''
    }
  },
  methods: {
    addExercise() {
      this.exercises.push({ name: '', reps: '', sets: '' })
    },
    removeExercise(index) {
      if (this.exercises.length > 1) {
        this.exercises.splice(index, 1)
      }
    },

    updateWorkoutName(value) {
      this.workoutName = value
    },
    updateWorkoutDate(value) {
      this.workoutDate = value
    },
    scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth' // Smooth scrolling
      })
    },

    async saveWorkout() {
      // Get user Id
      const token = localStorage.getItem('authToken')
      const decoded = jwtDecode(token)
      const userId = decoded.user_id

      let data = {
        _id: uuidv4(),
        user_id: userId,
        WorkoutName: this.workoutName,
        WorkoutDate: this.workoutDate,
        Exercises: this.exercises
      }

      try {
        const response = await axios.post('http://127.0.0.1:5000/log_workout', data)
        console.log('Workout logged:', response.data)
        this.$router.push('/')
      } catch (error) {
        console.error('There was an error logging the workout!', error)
        this.errorMessage = 'There was an error logging the workout!'
        this.scrollToTop()
      }
    }
  }
}
</script>
