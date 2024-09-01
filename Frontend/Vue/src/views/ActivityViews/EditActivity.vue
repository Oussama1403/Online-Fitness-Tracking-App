<template>
  <div class="container custom-container mt-4">
    <ActivityForm
      :mode="'Edit'"
      :activityName="user_ActivityName"
      :user_ActivityName="user_ActivityName"
      :details="details"
      :errorMessage="errorMessage"
      @update:user_ActivityName="updateUserActivityName"
      @submit="saveActivity"
      @delete="deleteActivity"
      @timeChanged="updateDuration"
    />
  </div>
</template>

<script>
import ActivityForm from '@/components/ActivityForm.vue' // Import the ActivityForm component

import axios from 'axios'
import { jwtDecode } from 'jwt-decode'

export default {
  name: 'EditActivity',

  components: {
    ActivityForm // Register the ActivityForm component
  },

  data() {
    return {
      details: {},
      user_ActivityName: '',
      id: '',
      userId: '',
      errorMessage: ''
    }
  },
  created() {
    this.initializeDataFromRoute()
  },

  methods: {
    initializeDataFromRoute() {
      const item = this.$route.query.item
      if (item) {
        try {
          const parsedItem = JSON.parse(item)
          this.user_ActivityName = parsedItem.ActivityName
          this.details = parsedItem.details
          this.id = parsedItem._id
          this.userId = parsedItem.user_id
        } catch (error) {
          console.error('Failed to parse item:', error)
        }
      }
    },
    calculateDuration(startTime, endTime) {
      if (!startTime || !endTime) {
        return { stringValue: '', value: 0 }
      }

      const start = new Date(`1970-01-01T${startTime}Z`)
      const end = new Date(`1970-01-01T${endTime}Z`)

      const durationInMilliseconds = end - start
      const durationInMinutes = durationInMilliseconds / 60000 // minutes with fractional part

      const hours = Math.floor(durationInMinutes / 60)
      const minutes = Math.floor(durationInMinutes % 60)
      const seconds = Math.round((durationInMilliseconds % 60000) / 1000)

      let stringValue = ''
      if (hours > 0) {
        stringValue += `${hours}h `
      }
      if (minutes > 0 || hours > 0) {
        // Show minutes if there are hours
        stringValue += `${minutes}m `
      }
      if (seconds > 0) {
        stringValue += `${seconds}s`
      }

      return { stringValue: stringValue.trim(), value: durationInMinutes }
    },

    updateDuration() {
      const startTime = this.details.start_time.value
      const endTime = this.details.end_time.value
      const duration = this.calculateDuration(startTime, endTime)
      this.details.duration.stringValue = duration.stringValue
      this.details.duration.value = duration.value
    },

    updateUserActivityName(newName) {
      this.user_ActivityName = newName
    },
    scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth' // Smooth scrolling
      })
    },

    async saveActivity() {
      try {
        const data = {
          _id: this.id,
          user_id: this.userId,
          ActivityName: this.user_ActivityName,
          details: this.details
        }

        const response = await axios.post('http://127.0.0.1:5000/update_activity', data)
        console.log('Activity updated:', response.data)
        this.$router.push('/')
      } catch (error) {
        console.error('Error updating the activity:', error)
        this.errorMessage = 'There was an error updating the activity!'
        this.scrollToTop()
      }
    },

    async deleteActivity() {
      try {
        const data = {
          _id: this.id,
          user_id: this.userId,
          ActivityName: this.user_ActivityName,
          details: this.details
        }

        const response = await axios.post('http://127.0.0.1:5000/delete_activity', data)
        console.log('Activity deleted:', response.data)
        this.$router.push('/')
      } catch (error) {
        console.error('Error deleting the activity:', error)
        this.errorMessage = 'There was an error deleting the activity!'
        this.scrollToTop()
      }
    }
  }
}
</script>
