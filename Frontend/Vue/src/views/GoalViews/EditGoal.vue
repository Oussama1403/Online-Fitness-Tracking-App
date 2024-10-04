<template>
  <GoalForm
    :mode="'Edit'"
    :isDone="goal.is_done"
    :goalName="goalName"
    :goal="goal"
    :errorMessage="errorMessage"
    @submit="saveGoal"
    @delete="deleteGoal"
    @markDone="markDone"
    @markUndone="markUndone"
  />
</template>

<script>
import GoalForm from '@/components/GoalForm.vue'
import { is_not } from '@vee-validate/rules';

import axios from 'axios'
import { jwtDecode } from 'jwt-decode'

export default {
  name: 'EditGoal',
  components: {
    GoalForm
  },
  data() {
    return {
      goalName: '',
      goal: {
        _id: '',
        user_id: '',
        type: '',
        description: '',
        currentProgress: '',
        targetDate: '',
        notes: '',
        is_done: ''
      },
      goals: [],
      errorMessage: ''
    }
  },
  created() {
    const item = this.$route.query.item
    const parsedItem = JSON.parse(item)
    this.goalName = parsedItem.type
    this.goal.type = parsedItem.type
    this.goal.description = parsedItem.description
    this.goal.currentProgress = parsedItem.currentProgress
    this.goal.targetDate = parsedItem.targetDate
    this.goal.notes = parsedItem.notes
    this.goal.is_done = parsedItem.is_done
    this.goal._id = parsedItem._id
    this.goal.user_id = parsedItem.user_id
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
        const response = await axios.post('http://127.0.0.1:5000/update_goal', this.goal)
        console.log('Goal updated:', response.data)
        this.$router.push('/')
      } catch (error) {
        console.error('There was an error updating the goal!', error)
        this.errorMessage = 'There was an error updating the goal!'
        this.scrollToTop()
      }
    },

    async deleteGoal() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/delete_goal', this.goal)
        console.log('Goal deleted:', response.data)
        this.$router.push('/')
      } catch (error) {
        console.error('There was an error deleting the goal!', error)
        this.errorMessage = 'There was an error deleting the goal!'
        this.scrollToTop()
      }
    },
    
    markDone() {
      this.goal.is_done = true
      console.log('Goal marked as done.')
      this.saveGoal() 
    },

    markUndone() {
      this.goal.is_done = false
      console.log('Goal marked as undone.')
      this.saveGoal()
    },
  }
}
</script>
