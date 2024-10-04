<template>
  <WorkoutForm
    :mode="'Edit'"
    :isDone="isDone"
    :workoutName="workoutName"
    :workoutDate="workoutDate"
    :exercises="exercises"
    :errorMessage="errorMessage"
    @update:workoutName="updateWorkoutName"
    @update:workoutDate="updateWorkoutDate"
    @submit="saveWorkout"
    @addExercise="addExercise"
    @removeExercise="removeExercise"
    @markDone="markDone"
    @markUndone="markUndone"
    @delete="deleteWorkout"
  />
</template>

<script>
import axios from 'axios'

import WorkoutForm from '@/components/WorkoutForm.vue'

export default {
  name: 'EditWorkout',

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
      isDone: '',
      id: '',
      errorMessage: ''
    }
  },
  created() {
    const item = this.$route.query.item
    const parsedItem = JSON.parse(item)
    //console.log("parsedItem:", parsedItem);
    this.workoutName = parsedItem.WorkoutName
    this.workoutDate = parsedItem.WorkoutDate
    this.exercises = parsedItem.Exercises
    this.isDone = parsedItem.is_done
    this.id = parsedItem._id
    this.userId = parsedItem.user_id
  },
  methods: {
    addExercise() {
      this.exercises.push({ name: '', reps: '', sets: '' })
    },
    removeExercise(index) {
      this.exercises.splice(index, 1)
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
      let data = {
        _id: this.id,
        user_id: this.userId,
        WorkoutName: this.workoutName,
        WorkoutDate: this.workoutDate,
        Exercises: this.exercises,
        is_done: this.isDone
      }

      try {
        const response = await axios.post('http://127.0.0.1:5000/update_workout', data)
        console.log('Workout updated:', response.data)
        this.$router.push('/')
      } catch (error) {
        console.error('There was an error updating the workout!', error)
        this.errorMessage = 'There was an error updating the workout!'
        this.scrollToTop()
      }
    },

    async deleteWorkout() {
      let data = {
        _id: this.id,
        user_id: this.userId,
        WorkoutName: this.workoutName,
        WorkoutDate: this.workoutDate,
        Exercises: this.exercises,
        is_done: this.isDone
      }

      try {
        const response = await axios.post('http://127.0.0.1:5000/delete_workout', data)
        console.log('Workout deleted:', response.data)
        this.$router.push('/')
      } catch (error) {
        console.error('There was an error deleting the workout!', error)
        this.errorMessage = 'There was an error deleting the workout!'
        this.scrollToTop()
      }
    },
    
    async markDone() {
      let data = {
        _id: this.id,
        user_id: this.userId,
        WorkoutName: this.workoutName,
        WorkoutDate: this.workoutDate,
        Exercises: this.exercises,
        is_done: true
      }

      try {
        const response = await axios.post('http://127.0.0.1:5000/update_workout', data)
        console.log('Workout is Marked Done:', response.data)
        this.$router.push('/')
      } catch (error) {
        console.error('There was an error updating the workout!', error)
        this.errorMessage = 'There was an error updating the workout!'
        this.scrollToTop()
      }
    },
    async markUndone() {
      let data = {
        _id: this.id,
        user_id: this.userId,
        WorkoutName: this.workoutName,
        WorkoutDate: this.workoutDate,
        Exercises: this.exercises,
        is_done: false
      }

      try {
        const response = await axios.post('http://127.0.0.1:5000/update_workout', data)
        console.log('Workout is Marked Undone:', response.data)
        this.$router.push('/')
      } catch (error) {
        console.error('There was an error updating the workout!', error)
        this.errorMessage = 'There was an error updating the workout!'
        this.scrollToTop()
      }
    },
  }
}
</script>
