<template>
    <div class="container custom-container mt-4">
      <form @submit.prevent="saveActivity">
        <span class="form-title">
          Edit <span class="form-title-activityname">{{ user_ActivityName }}</span>
        </span>
  
        <!-- Activity Name: -->
        <div class="form-group">
          <input type="text" placeholder="Activity name" class="input form-control" id="user_ActivityName" v-model="user_ActivityName" required>
        </div>
  
        <!-- Activity details Section -->
        <div v-for="(detail, index) in details" :key="index" class="group mb-3">
          <div class="form-group">
            <!-- Render Date input as calendar picker -->
            <input v-if="detail.name === 'Date'" type="date" class="input form-control" :id="'detail.name' + index" v-model="detail.value" required>
  
            <!-- Render Start Time and End Time inputs -->
            <input v-else-if="detail.name === 'Start Time'" type="time" class="input form-control" :id="'detail.name' + index" v-model="detail.value" required>
            <input v-else-if="detail.name === 'End Time'" type="time" class="input form-control" :id="'detail.name' + index" v-model="detail.value" required>
  
            <!-- Render other inputs -->
            <input v-else type="text" :placeholder="detail.name" class="input form-control" :id="'detail.name' + index" v-model="detail.value" required>
          </div>
        </div>
  
        <!-- Save Button -->
        <button type="submit" class="save-button btn btn-success">Save Activity</button>
        <!-- del button -->
        <button type="button" @click="deleteActivity" class="delete-button btn btn-danger">Delete Activity</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'EditActivity',

    data() {
      return {
        details: [
          { name: 'date', value: '' },
          { name: 'startTime', value: '' },
          { name: 'endTime', value: '' },
          { name: 'duration', value: '' },
          { name: 'distance', value: '' },
          { name: 'caloriesBurned', value: '' },
        ],
        user_ActivityName: '',
      };
    },
    created() {
    const item = this.$route.query.item;
    if (item) {
      try {
        const parsedItem = JSON.parse(item);
        console.log(parsedItem);
        console.log(parsedItem.name);
        this.user_ActivityName = parsedItem.name;
        this.details.forEach(detail => {
          // Find the matching key in parsedItem
          const value = parsedItem[detail.name];
          if (value !== undefined) {
            detail.value = value;
          }
        });
      } catch (error) {
        console.error('Failed to parse item:', error);
      }
    }
  },
    methods: {
      saveActivity() {
        // Handle form submission
        console.log('Activity Name:', this.user_ActivityName);
        console.log('Activity Details:', this.details);
        // Add your save logic here
      },
      deleteActivity() {
        // Handle delete activity
        console.log('Activity Deleted:', this.user_ActivityName);
        // Add your delete logic here
      }
    }
  };
  </script>
  
  <style scoped>
  /* Your existing CSS styles */
  </style>
    
  
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
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
  }
  
  form {
    width: 500px;
  }
  
  .form-title {
    display: block;
    font-size: 24px;
    color: #333333;
    line-height: 1.2;
    text-align: center;
    padding-bottom: 44px;
  }
  .form-title-activityname {
    color: #57B846;
  }
  
  .group {
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
    font-weight: 700;
    font-size: 15px;
    line-height: 1.5;
    color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0 25px;
  
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
  
  .save-button {
    background: #57b846;
  }
  .delete-button {
    background: #f43333;
}
  </style>
  