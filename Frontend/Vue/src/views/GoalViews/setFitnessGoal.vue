<template>
  <GoalForm :mode="'Log'" :goal="goal" :errorMessage="errorMessage" @submit="saveGoal" />
</template>

<script>
import GoalForm from '@/components/GoalForm.vue'

import axios from 'axios'
import { v4 as uuidv4 } from 'uuid'
import { jwtDecode } from 'jwt-decode'

export default {
  name: 'setFitnessGoal',
  components: {
    GoalForm
  },
  data() {
    return {
      goal: {
        type: '',
        description: '',
        currentProgress: '',
        targetDate: '',
        notes: '',
        is_done: false
      },
      errorMessage: ''
    }
  },
  methods: {
    scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth' // Smooth scrolling
      })
    },
    async saveGoal() {
      try {
        // Get user Id
        const token = localStorage.getItem('authToken')
        const decoded = jwtDecode(token)
        const userId = decoded.user_id

        let data = {
          _id: uuidv4(),
          user_id: userId,
          ...this.goal // spread operator
        }

        // Perform the POST request
        const response = await axios.post('http://127.0.0.1:5000/log_goal', data)
        console.log('Goal logged:', response.data)
        this.$router.push('/')
      } catch (error) {
        console.error('There was an error logging the goal!', error)
        this.errorMessage = 'There was an error logging the goal!'
        this.scrollToTop()
      }
    }
  }
}
</script>
