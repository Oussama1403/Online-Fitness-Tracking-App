<template>
    <div class="set-fitness-goal">
      <div class="container custom-container mt-4">
        <form @submit.prevent="setGoal">
          <span class="form-title">Edit <span class="form-title-important">{{ goalName}}</span></span>
          <div class="form-group">
            <label for="goalType">Goal Type</label>
            <select class="input form-control" id="goalType" v-model="goal.type">
              <option>Weight Loss</option>
              <option>Strength</option>
              <option>Cardio</option>
              <option>Flexibility</option>
              <option>Endurance</option>
              <option>Nutrition</option>
              <option>Habit</option>
            </select>
          </div>
          <div class="form-group">
            <label for="goalDescription">Description</label>
            <input type="text" class="input form-control" id="goalDescription" v-model="goal.description" placeholder="e.g., Lose 5 kg in 2 months">
          </div>
          <div class="form-group">
            <label for="currentProgress">Enter your current progress</label>
            <input type="text" class="input form-control" id="currentProgress" v-model="goal.currentProgress" placeholder="e.g., X kg | X number of push-ups | Run X km/miles">
          </div>
          <div class="form-group">
            <label for="targetDate">Target Date</label>
            <input type="date" class="input form-control" id="targetDate" v-model="goal.targetDate">
          </div>
          <div class="form-group">
            <label for="notes">Notes</label>
            <input type="text" class="input form-control" id="notes" v-model="goal.notes" placeholder="Additional information">
          </div>
          <button type="submit" class="save-goal btn btn-primary mt-3">Save Goal</button>
          <button type="button" class="delete-goal btn btn-danger mt-3">Delete Goal</button>

        </form>
        
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        goalName: '',
        goal: {
          type: '',
          description: '',
          currentProgress: '',
          targetDate: '',
          notes: ''
        },
        goals: []
      };
    },
    created() {
       const item = this.$route.query.item;
       const parsedItem = JSON.parse(item);
       this.goalName = parsedItem.type;

       this.goal.type = parsedItem.type;
       this.goal.description = parsedItem.description;
       this.goal.currentProgress = parsedItem.currentProgress;
       this.goal.targetDate = parsedItem.targetDate;
       this.goal.notes = parsedItem.notes;
       console.log(this.goal);
    },
    methods: {
      setGoal() {
        if (this.goal.type && this.goal.description && this.goal.targetDate) {
          this.goals.push({ ...this.goal });
          this.goal = { type: '', description: '', currentProgress: '', targetDate: '', notes: '' };
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* .set-fitness-goal {
    margin-top: 20px;
  }*/
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
    .form-title-important {
      color: #57B846;
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
    
    .save-goal {
      background: #57b846;
    }
    .delete-goal {
      background: #f43333;
    }
  
  </style>
  