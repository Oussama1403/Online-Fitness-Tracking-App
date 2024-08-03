import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.min'
import './assets/style.css'


import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { Field, Form, ErrorMessage, defineRule, configure } from 'vee-validate';
import { required, email, min, max, numeric, alpha } from '@vee-validate/rules';
import { localize, setLocale } from '@vee-validate/i18n';
import en from '@vee-validate/i18n/dist/locale/en.json';

// Create Vue app
const app = createApp(App);

// Register VeeValidate components
app.component('Form', Form);
app.component('Field', Field);
app.component('ErrorMessage', ErrorMessage);

// Define and register rules individually
defineRule('required', required);
defineRule('email', email);
defineRule('min', min);
defineRule('max', max);
defineRule('numeric', numeric);
defineRule('alpha', alpha);


// Custom validation rule to check if unit is selected
defineRule("unit_required", value => {
  return value !== "" || "Unit is required"; // Ensure the value is not empty
});
// Custom rule for non-negative values
defineRule('non_negative', value => {
  if (value >= 0) {
    return true;
  }
  return 'The field must be a non-negative number';
});


/*
// Custom messages
const customMessages = {
  en: {
    /*
    messages: {
      required: '{field} is required.',
      numeric: '{field} must be a number.',
      // You can add more custom messages here
    },
    
    names: {
      // Goal Forms

      type: 'Goal Type',
      description: 'Goal Description ',
      currentProgress: 'Current Progress ',
      targetDate: 'Target Date',

      // Fitness Forms
      workoutName: 'Workout Name',
      workoutDate: 'Workout Date',
      exerciseName: 'Exercise Name',
      reps: 'Reps',
      sets: 'Sets',
      // Map other field names here if needed
    }
  }
};
*/

// Custom Field Names

const fieldNames = {
  type: 'Goal Type',
  description: 'Goal Description ',
  currentProgress: 'Current Progress ',
  targetDate: 'Target Date',

  // Fitness Forms
  workoutName: 'Workout Name',
  workoutDate: 'Workout Date',
};

// Configure VeeValidate for custom messages and to handle dynamic fields like 'exerciseName'

configure({
  generateMessage: (ctx) => {
    // Get the field name from the fieldNames mapping or (||) use the field name directly
    const fieldName = fieldNames[ctx.name] || ctx.field;

    // Define custom messages for each rule
    const messages = {
      required: `${fieldName} is required.`,
      numeric: `${fieldName} must be a number.`,
    };

    // Custom handling for specific field names
    if (ctx.name.startsWith('exerciseName')) {
      return `Exercise Name is required.`;
    }
    if (ctx.name.startsWith('reps')) {
      return `Reps must be a number.`;
    }
    if (ctx.name.startsWith('sets')) {
      return `Sets must be a number.`;
    }

    // Return custom message or default message
    return messages[ctx.rule.name] || `${fieldName} is invalid.`;
  },
  validateOnInput: true, // Validate on input rather than change
});

// Set default locale
setLocale('en');

app.use(router)

app.mount('#app')
