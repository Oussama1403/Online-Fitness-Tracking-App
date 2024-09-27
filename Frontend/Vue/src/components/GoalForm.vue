<template>
  <div class="set-fitness-goal">
    <div class="container custom-container mt-4">
      <Form @submit="handleSubmit" v-slot="{ errors }">
        <div v-if="mode === 'Log'">
          <span class="log-form-title fade-in"
            >Set Your Fitness <span class="form-title-important">Goal</span></span>
          <h5 class="mb-4 mt-4 text-center intro-text fade-in">
            Define and track your fitness objectives to stay
            <span class="intro-important">motivated and on target.</span>
          </h5>
        </div>

        <div v-if="mode === 'Edit'">
          <span class="edit-form-title fade-in"
            >Edit <span class="form-title-important">{{ goalName }}</span></span
          >
        </div>

        <div v-if="errorMessage" class="mb-4 mt-4 alert" role="alert">
          {{ errorMessage }}
        </div>

        <div class="fade-in">
          <div class="form-group">
            <label for="goalType">Goal Type</label>
            <Field
              as="select"
              name="type"
              v-model="goal.type"
              class="input form-control"
              rules="required"
            >
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
            <Field
              type="text"
              name="description"
              v-model="goal.description"
              class="input form-control"
              placeholder="e.g., Lose 5 kg in 2 months"
              rules="required"
            />
            <ErrorMessage class="error-msg" name="description" />
          </div>

          <div class="form-group">
            <label for="currentProgress">Enter your current progress</label>
            <Field
              type="text"
              name="currentProgress"
              v-model="goal.currentProgress"
              class="input form-control"
              placeholder="e.g., X kg | X number of push-ups | Run X km/miles"
              rules="required"
            />
            <ErrorMessage class="error-msg" name="currentProgress" />
          </div>

          <div class="form-group">
            <label for="targetDate">Target Date</label>
            <Field
              type="date"
              name="targetDate"
              v-model="goal.targetDate"
              class="input form-control"
              rules="required"
            />
            <ErrorMessage class="error-msg" name="targetDate" />
          </div>

          <div class="form-group">
            <label for="notes">Notes</label>
            <Field
              type="text"
              name="notes"
              v-model="goal.notes"
              class="input form-control"
              placeholder="Additional information"
            />
            <ErrorMessage class="error-msg" name="notes" />
          </div>

          <button type="submit" class="save-goal btn btn-primary mt-3">Set Goal</button>
          <button
            v-if="mode === 'Edit'"
            type="button"
            @click="$emit('delete')"
            class="delete-goal btn btn-danger mt-3"
          >
            Delete Goal
          </button>
        </div>
      </Form>
    </div>
  </div>
</template>

<script>
import { Field } from 'vee-validate'

export default {
  props: {
    mode: {
      type: String,
      required: true
    },
    goalName: {
      type: String,
      required: false
    },
    goal: {
      type: Object,
      required: false
    },
    errorMessage: String
  },
  methods: {
    handleSubmit() {
      this.$emit('submit')
    }
  }
}
</script>

<style scoped>
.intro-text {
  color: #333333;
  padding-bottom: 1rem;
  font-family: 'Montserrat', sans-serif;
}
.intro-important {
  color: #57b846;
}
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

.log-form-title {
  display: block;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  font-size: 1.8em;
  color: #333333;
  line-height: 1.2;
  text-align: center;
}
.edit-form-title {
  display: block;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  font-size: 24px;
  color: #333333;
  line-height: 1.2;
  text-align: center;
  padding-bottom: 44px;
}

.form-title-important {
  color: #57b846;
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
.input:hover {
  border: 1px solid #00ff99;
}
.input:focus {
  box-shadow: 0 0 0 0.2rem #00ff99;
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

.alert {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
  padding: 10px;
  border-radius: 25px;
  margin-bottom: 20px;
  text-align: center;
  font-family: 'Montserrat', sans-serif;
}

/* Define the fade-in animation */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}
/* Apply the fade-in animation to elements */
.fade-in {
  opacity: 0;
  animation: fadeIn 1s ease-out forwards;
}

/* Staggered animation delay for sequential appearance */
.fade-in:nth-child(1) {
  animation-delay: 0.5s;
}

.fade-in:nth-child(2) {
  animation-delay: 0.8s;
}
</style>
