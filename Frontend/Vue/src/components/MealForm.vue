<template>
    <div class="meal-form">
      <div class="container custom-container mt-4">
      <Form @submit="handleSubmit" v-slot="{ errors }">

        <div v-if="mode === 'Log'">
          <span class="log-form-title fade-in"
            >Log Your <span class="form-title-important">Meal</span></span>
          <h5 class="mb-4 mt-4 text-center intro-text fade-in">
            Track your daily meals and nutrition to stay on top of your
            <span class="intro-important">fitness goals.</span>
          </h5>
        </div>

        <div v-if="mode === 'Edit'">
          <span class="edit-form-title fade-in"
            >Edit <span class="form-title-important">{{ meal.mealName }}</span></span>
        </div>

        <div v-if="errorMessage" class="mb-4 mt-4 alert" role="alert">
          {{ errorMessage }}
        </div>
        
        <div class="fade-in">
        <div class="form-group">
          <label for="mealName">Meal Name</label>
          <Field
            type="text"
            placeholder="Meal name"
            class="input form-control"
            id="mealName"
            name="Meal Name"
            v-model="meal.mealName"
            rules="required"
          />
          <ErrorMessage class="error-msg" name="Meal Name" />
        </div>

        <div class="form-group">
          <label for="mealName">Meal Date</label>
          <Field
            type="date"
            class="input form-control"
            name="Meal Date"
            v-model="meal.mealDate"
            rules="required"
          />
          <ErrorMessage name="Meal Date" class="error-msg" />
        </div>
        
        <div class="form-group">
          <label for="foodItems">Food Items</label>
          <Field type="text" name="Food Items" v-model="meal.foodItems" class="input form-control" placeholder="e.g., Chicken, Rice" rules="required"></Field>
          <ErrorMessage class="error-msg" name="Food Items" />
        </div>
  
        <div class="form-group">
          <label for="calories">Calories</label>
          <Field type="number" name="Calories" v-model="meal.calories" class="input form-control" placeholder="e.g., 300" rules="required|numeric|non_negative"></Field>
          <ErrorMessage class="error-msg" name="Calories" />
        </div>
  
        <div class="form-group">
          <label for="protein">Protein (g)</label>
          <Field type="number" name="Protein" v-model="meal.protein" class="input form-control" placeholder="e.g., 25" rules="required|numeric|non_negative"></Field>
          <ErrorMessage class="error-msg" name="Protein" />
        </div>
  
        <div class="form-group">
          <label for="carbs">Carbs (g)</label>
          <Field type="number" name="Carbs" v-model="meal.carbs" class="input form-control" placeholder="e.g., 50" rules="required|numeric|non_negative"></Field>
          <ErrorMessage class="error-msg" name="Carbs" />
        </div>
  
        <div class="form-group">
          <label for="fats">Fats (g)</label>
          <Field type="number" name="Fats" v-model="meal.fats" class="input form-control" placeholder="e.g., 10" rules="required|numeric|non_negative"></Field>
          <ErrorMessage class="error-msg" name="Fats" />
        </div>
  
        <button type="submit" class="save-meal btn btn-primary">Save Meal</button>
        <button
            v-if="mode === 'Edit'"
            type="button"
            @click="$emit('delete')"
            class="delete-meal btn btn-danger mt-3"
          >
            Delete Meal
          </button>
        </div>
      </form>
      </div>
    </div>
  </template>
  
  <script>
  import { Field } from 'vee-validate'

  export default {
    props: {
        meal: {
          type: Object,
          required: false
        },
        mode: {
          type: String,
          required: true
        },
        errorMessage: String
      },
    methods: {
        handleSubmit() {
          this.$emit('submit')
        },
    }
  };
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

.save-meal {
  background: #57b846;
}

.delete-meal {
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
  