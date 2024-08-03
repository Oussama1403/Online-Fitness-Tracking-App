<template>
  <div class="set-fitness-goal">
    <div class="container custom-container mt-4">
      <Form @submit="saveGoal" v-slot="{ errors }">
        <span class="form-title">Set Your Fitness <span class="form-title-important">Goal</span></span>        
        <div class="form-group">
          <label for="goalType">Goal Type</label>
          <Field as="select" name="type" v-model="goal.type" class="input form-control" rules="required">
            <option value="">Select Goal Type</option>
            <option value="Weight Loss">Weight Loss</option>
            <option value="Strength">Strength</option>
            <option value="Cardio">Cardio</option>
            <option value="Flexibility">Flexibility</option>
            <option value="Endurance">Endurance</option>
            <option value="Nutrition">Nutrition</option>
            <option value="Habit">Habit</option>
          </Field>
          <ErrorMessage class="error-msg" name="type" />
        </div>

        <div class="form-group">
          <label for="goalDescription">Description</label>
          <Field type="text" name="description" v-model="goal.description" class="input form-control" placeholder="e.g., Lose 5 kg in 2 months" rules="required" />
          <ErrorMessage class="error-msg" name="description" />
        </div>

        <div class="form-group">
          <label for="currentProgress">Enter your current progress</label>
          <Field type="text" name="currentProgress" v-model="goal.currentProgress" class="input form-control" placeholder="e.g., X kg | X number of push-ups | Run X km/miles" rules="required" />
          <ErrorMessage class="error-msg" name="currentProgress" />
        </div>

        <div class="form-group">
          <label for="targetDate">Target Date</label>
          <Field type="date" name="targetDate" v-model="goal.targetDate" class="input form-control" rules="required" />
          <ErrorMessage class="error-msg" name="targetDate" />
        </div>

        <div class="form-group">
          <label for="notes">Notes</label>
          <Field type="text" name="notes" v-model="goal.notes" class="input form-control" placeholder="Additional information" />
          <ErrorMessage class="error-msg" name="notes" />
        </div>

        <button type="submit" class="submit-b btn btn-primary mt-3">Set Goal</button>
      </Form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      goal: {
        type: '',
        description: '',
        currentProgress: '',
        targetDate: '',
        notes: ''
      },
    };
  },
  methods: {
    saveGoal(values) {
      console.log(values)
      axios.post('http://127.0.0.1:5000/log_goal', values)
        .then(response => {
          console.log('Goal logged:', response.data);
        })
        .catch(error => {
          console.error('There was an error logging the goal!', error);
        });
    }
  }
}
</script>

<style scoped>
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

.submit-b {
  background: #57b846;
}
</style>
