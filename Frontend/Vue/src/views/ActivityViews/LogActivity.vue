<template>
  <div class="container custom-container mt-4">
    <ActivityForm
      :mode="'Log'"
      :user_ActivityName="activityName"
      :details="filteredDetails"
      :errorMessage="errorMessage"
      @update:user_ActivityName="updateUserActivityName"
      @submit="saveActivity"
      @timeChanged="updateDuration"
    />
  </div>
</template>

<script>
import ActivityForm from '@/components/ActivityForm.vue' // Import the ActivityForm component

import axios from 'axios'
import { Field } from 'vee-validate'
import { v4 as uuidv4 } from 'uuid'
import { jwtDecode } from 'jwt-decode'

export default {
  name: 'LogActivity',

  components: {
    ActivityForm // Register the ActivityForm component
  },

  data() {
    return {
      details: {
        date: { name: 'Date', value: '' },
        start_time: { name: 'Start Time', value: '' },
        end_time: { name: 'End Time', value: '' },
        exercise_type: { name: 'Exercise Type', value: '' },
        weight_lifted: { name: 'Weight Lifted', value: '' },
        reps: { name: 'Reps', value: '' },
        sets: { name: 'Sets', value: '' },
        steps: { name: 'Steps', value: '' },
        laps: { name: 'Laps', value: '' },
        intensity: { name: 'Intensity', value: '' },
        duration: { name: 'Duration', stringValue: '', value: '' },
        distance: { name: 'Distance', value: '', unit: '' },
        calories_burned: { name: 'Calories Burned', value: '' },
        comments: { name: 'Comments', value: '' }
      },
      user_ActivityName: '',
      activityName: this.$route.params.activityName || '',
      errorMessage: '',
      activityFieldConfig: {
        Weightlifting: [
          'Date',
          'Start Time',
          'End Time',
          'Exercise Type',
          'Weight Lifted',
          'Reps',
          'Sets',
          'Intensity',
          'Duration',
          'Calories Burned',
          'Comments'
        ],
        Running: [
          'Date',
          'Start Time',
          'End Time',
          'Distance',
          'Duration',
          'Calories Burned',
          'Comments'
        ],
        Cycling: [
          'Date',
          'Start Time',
          'End Time',
          'Distance',
          'Duration',
          'Calories Burned',
          'Comments'
        ],
        Swimming: [
          'Date',
          'Start Time',
          'End Time',
          'Laps',
          'Distance',
          'Duration',
          'Calories Burned',
          'Comments'
        ],
        Walking: [
          'Date',
          'Start Time',
          'End Time',
          'Steps',
          'Distance',
          'Duration',
          'Calories Burned',
          'Comments'
        ]
      }
    }
  },
  computed: {
    filteredDetails() {
      const detailsArray = Object.values(this.details)
      const relevantFields = this.activityFieldConfig[this.activityName] || []
      return detailsArray.filter((detail) => relevantFields.includes(detail.name))
    }
  },
  methods: {
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
        // Get user Id
        const token = localStorage.getItem('authToken')
        const decoded = jwtDecode(token)
        const userId = decoded.user_id

        const data = {
          _id: uuidv4(),
          user_id: userId,
          ActivityName: this.user_ActivityName,
          details: Object.fromEntries(
            Object.entries(this.details).filter(([key, value]) => value.value !== '')
          )
        }

        // Perform the POST request
        const response = await axios.post('http://127.0.0.1:5000/log_activity', data)

        // Handle the response
        console.log('Activity logged:', response.data)
        this.$router.push('/')
      } catch (error) {
        // Handle any errors
        console.error('There was an error logging the activity!', error)
        this.errorMessage = 'There was an error logging the activity!'
        this.scrollToTop()
      }
    }
  }
}
</script>
