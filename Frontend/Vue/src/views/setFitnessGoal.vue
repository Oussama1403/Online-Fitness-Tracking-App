<template>
    <div class="set-fitness-goal">
      <div class="container-fluid px-4">
        <h1 class="mt-4">Set Your Fitness Goal</h1>
        <form @submit.prevent="setGoal">
          <div class="form-group">
            <label for="goalType">Goal Type</label>
            <select class="form-control" id="goalType" v-model="goal.type">
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
            <input type="text" class="form-control" id="goalDescription" v-model="goal.description" placeholder="e.g., Lose 5 kg in 2 months">
          </div>
          <div class="form-group">
            <label for="targetDate">Target Date</label>
            <input type="date" class="form-control" id="targetDate" v-model="goal.targetDate">
          </div>
          <button type="submit" class="btn btn-primary mt-3">Set Goal</button>
        </form>
        <h2 class="mt-5">Your Current Goals</h2>
        <div class="goal-list">
          <div class="card mt-3" v-for="goal in goals" :key="goal.description">
            <div class="card-body">
              <h5 class="card-title">{{ goal.type }}</h5>
              <p class="card-text">{{ goal.description }}</p>
              <p class="card-text"><small class="text-muted">Target Date: {{ goal.targetDate }}</small></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "SetFitnessGoal",
    data() {
      return {
        goal: {
          type: '',
          description: '',
          targetDate: ''
        },
        goals: []
      };
    },
    methods: {
      setGoal() {
        if (this.goal.type && this.goal.description && this.goal.targetDate) {
          this.goals.push({ ...this.goal });
          this.goal = { type: '', description: '', targetDate: '' };
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .set-fitness-goal {
    margin-top: 20px;
  }
  .card {
    border: none;
    border-radius: 0.75rem;
    transition: all 0.3s ease-in-out;
  }
  .card:hover {
    transform: scale(1.05);
  }
  </style>
  