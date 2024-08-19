<template>
  <div class="container custom-container mt-4">
    <Form @submit="saveActivity" v-slot="{ errors }">
      <span class="form-title fade-in">
        Log <span class="form-title-activityname">{{ activityName }}</span>
      </span>
      <div class="fade-in">
      <!-- Activity Name: -->
      <div class="form-group ">
        <label for="user_ActivityName">Activity name</label>
        <Field type="text" class="input form-control" id="user_ActivityName" name="Activity Name"
          v-model="user_ActivityName" rules="required" />
        <ErrorMessage name="Activity Name" class="error-msg" />
      </div>

      <!-- Activity details Section -->
      <div v-for="(detail, index) in filteredDetails" :key="index" class="group mb-3">
        <div class="form-group">
          <!-- Render Date input as calendar picker -->
          <template v-if="detail.name === 'Date'">
            <label :for="detail.name + index">{{ detail.name }}</label>
            <Field type="date" class="input form-control" :id="detail.name + index" :name="detail.name"
              v-model="detail.value" rules="required" />
            <ErrorMessage :name="detail.name" class="error-msg" />
          </template>

          <!-- Render Start Time input -->
          <template v-else-if="detail.name === 'Start Time'">
            <label :for="detail.name + index">{{ detail.name }}</label>
            <Field type="time" class="input form-control" :id="detail.name + index" :name="detail.name"
              v-model="detail.value" step="1" rules="required" @change="updateDuration" />
            <ErrorMessage :name="detail.name" class="error-msg" />
          </template>

          <!-- Render End Time input -->
          <template v-else-if="detail.name === 'End Time'">
            <label :for="detail.name + index">{{ detail.name }}</label>
            <Field type="time" class="input form-control" :id="detail.name + index" :name="detail.name"
              v-model="detail.value" step="1" rules="required" @change="updateDuration" />
            <ErrorMessage :name="detail.name" class="error-msg" />
          </template>

          <!-- There inputs are only rendered when weightlifting controlled by filteredDetails array-->
          <template v-else-if="detail.name === 'Exercise Type'">
            <label :for="detail.name + index">{{ detail.name }}</label>
            <Field as="select" :id="detail.name + index" :name="detail.name" v-model="detail.value"
              class="input form-control" rules="required">
              <option value="">Select Exercise</option>
              <option value="bench_press">Bench Press</option>
              <option value="squat">Squat</option>
              <option value="deadlift">Deadlift</option>
              <option value="overhead_press">Overhead Press</option>
              <option value="row">Row</option>
              <option value="other">Other</option>
            </Field>
            <ErrorMessage :name="detail.name" class="error-msg" />
          </template>

          <template v-else-if="detail.name === 'Weight Lifted'">
            <label :for="detail.name + index">{{ detail.name }}</label>
            <Field type="number" :id="detail.name + index" :name="detail.name" v-model="detail.value"
              class="input form-control" rules="required" />
            <ErrorMessage :name="detail.name" class="error-msg" />
          </template>

          <template v-else-if="detail.name === 'Reps'">
            <label :for="'detail.name' + index">{{ detail.name }}</label>
            <Field type="number" :id="'detail.name' + index" :name="detail.name" v-model="detail.value"
              class="input form-control" rules="required|numeric|non_negative" />
            <ErrorMessage :name="detail.name" class="error-msg" />
          </template>
          <template v-else-if="detail.name === 'Sets'">
            <label :for="'detail.name' + index">{{ detail.name }}</label>
            <Field type="number" :id="'detail.name' + index" :name="detail.name" v-model="detail.value"
              class="input form-control" rules="required|numeric|non_negative" />
            <ErrorMessage :name="detail.name" class="error-msg" />
          </template>

          <template v-else-if="detail.name === 'Laps'">
            <label :for="'detail.name' + index">{{ detail.name }}</label>
            <Field type="number" :id="'detail.name' + index" :name="detail.name" v-model="detail.value"
              class="input form-control" rules="required|numeric|non_negative" />
            <ErrorMessage :name="detail.name" class="error-msg" />
          </template>


          <template v-else-if="detail.name === 'Steps'">
            <label :for="'detail.name' + index">{{ detail.name }}</label>
            <Field type="number" :id="'detail.name' + index" :name="detail.name" v-model="detail.value"
              class="input form-control" rules="required|numeric|non_negative" />
            <ErrorMessage :name="detail.name" class="error-msg" />
          </template>

          <template v-else-if="detail.name === 'Intensity'">
            <label :for="detail.name + index">{{ detail.name }}</label>
            <Field as="select" :id="detail.name + index" :name="detail.name" v-model="detail.value"
              class="input form-control" rules="required">
              <option value="">Select Intensity</option>
              <option value="light">Light</option>
              <option value="moderate">Moderate</option>
              <option value="heavy">Heavy</option>
            </Field>
            <ErrorMessage :name="detail.name" class="error-msg" />
          </template>

          <template v-else-if="detail.name === 'Duration'">
            <div class="form-group">
              <label :for="detail.name + index">{{ detail.name }}</label>
              <div class="input-group">
                <Field type="text" class="input form-control" :id="detail.name + index" :name="detail.name"
                  v-model="detail.stringValue" readonly />
              </div>
            </div>
          </template>


          <template v-else-if="detail.name === 'Distance'">
            <div class="form-group">
              <label :for="detail.name + index">{{ detail.name }}</label>
              <div class="input-group">
                <Field type="number" class="input form-control" :id="detail.name + index" :name="detail.name"
                  v-model="detail.value" rules="required|numeric|non_negative" />
                <div class="input-group-append">
                  <button class="btn-dropdown btn btn-outline-secondary dropdown-toggle" type="button"
                    data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    {{ detail.unit || 'Unit' }}
                  </button>
                  <div class="dropdown-menu dropdown-menu-right">
                    <a class="dropdown-item" href="#" @click.prevent="detail.unit = 'Meters'">Meters</a>
                    <a class="dropdown-item" href="#" @click.prevent="detail.unit = 'Kilometers'">Kilometers</a>
                  </div>
                </div>
              </div>
              <!-- the hidden field allows us to make vee-validate aware of the unit selection and apply the custom unit_required validation rule to it. -->
              <Field type="hidden" :name="'detail.unit' + index" v-model="detail.unit" rules="unit_required" />
              <ErrorMessage :name="'detail.unit' + index" class="error-msg" />
            </div>
            <ErrorMessage :name="detail.name" class="error-msg" />
          </template>

          <template v-else-if="detail.name === 'Calories Burned'">
            <label :for="'detail.name' + index">{{ detail.name }}</label>
            <Field type="number" :id="'detail.name' + index" :name="detail.name" v-model="detail.value"
              class="input form-control" rules="required|numeric|non_negative" />
            <ErrorMessage :name="detail.name" class="error-msg" />
          </template>


          <!-- Render other inputs -->
          <template v-else>
            <label :for="detail.name + index">{{ detail.name }}</label>
            <Field type="text" class="input form-control" :id="detail.name + index" :name="detail.name"
              v-model="detail.value" />
            <ErrorMessage :name="detail.name" class="error-msg" />
          </template>
        </div>
      </div>


      <!-- Save Button -->
      <button type="submit" class="save-button btn btn-success">Save Activity</button>
      </div>
    </Form>
  </div>
</template>

<script>
import axios from 'axios';
import { Field } from 'vee-validate';
import { v4 as uuidv4 } from 'uuid';
import { jwtDecode } from "jwt-decode";

export default {
  data() {
    return {
      details: {
        date: { name: "Date", value: "" },
        start_time: { name: "Start Time", value: "" },
        end_time: { name: "End Time", value: "" },
        exercise_type: { name: "Exercise Type", value: "" },
        weight_lifted: { name: "Weight Lifted", value: "" },
        reps: { name: "Reps", value: "" },
        sets: { name: "Sets", value: "" },
        steps: { name: "Steps", value: "" },
        laps: { name: "Laps", value: "" },
        intensity: { name: "Intensity", value: "" },
        duration: { name: "Duration", stringValue: "", value: "" },
        distance: { name: "Distance", value: "", unit: "" },
        calories_burned: { name: "Calories Burned", value: "" },
        comments: { name: "Comments", value: "" }
      },
      user_ActivityName: "",
      activityName: this.$route.params.activityName || "",

      activityFieldConfig: {
        Weightlifting: ['Date', 'Start Time', 'End Time', 'Exercise Type', 'Weight Lifted', 'Reps', 'Sets', 'Intensity', 'Duration', 'Calories Burned', 'Comments'],
        Running: ['Date', 'Start Time', 'End Time', 'Distance', 'Duration', 'Calories Burned', 'Comments'],
        Cycling: ['Date', 'Start Time', 'End Time', 'Distance', 'Duration', 'Calories Burned', 'Comments'],
        Swimming: ['Date', 'Start Time', 'End Time', 'Laps', 'Distance', 'Duration', 'Calories Burned', 'Comments'],
        Walking: ['Date', 'Start Time', 'End Time', 'Steps', 'Distance', 'Duration', 'Calories Burned', 'Comments'],
      }
    };
  },
  computed: {
    filteredDetails() {
      const detailsArray = Object.values(this.details);
      const relevantFields = this.activityFieldConfig[this.activityName] || [];
      return detailsArray.filter(detail => relevantFields.includes(detail.name));
    }
  },
  methods: {
    calculateDuration(startTime, endTime) {
      if (!startTime || !endTime) {
        return { stringValue: "", value: 0 };
      }

      const start = new Date(`1970-01-01T${startTime}Z`);
      const end = new Date(`1970-01-01T${endTime}Z`);

      const durationInMilliseconds = end - start;
      const durationInMinutes = durationInMilliseconds / 60000; // minutes with fractional part

      const hours = Math.floor(durationInMinutes / 60);
      const minutes = Math.floor(durationInMinutes % 60);
      const seconds = Math.round((durationInMilliseconds % 60000) / 1000);

      let stringValue = "";
      if (hours > 0) {
        stringValue += `${hours}h `;
      }
      if (minutes > 0 || hours > 0) { // Show minutes if there are hours
        stringValue += `${minutes}m `;
      }
      if (seconds > 0) {
        stringValue += `${seconds}s`;
      }

      return { stringValue: stringValue.trim(), value: durationInMinutes };
    },

    updateDuration() {
      const startTime = this.details.start_time.value;
      const endTime = this.details.end_time.value;
      console.log("Start time:", startTime);
      console.log("End time:", endTime);


      const duration = this.calculateDuration(startTime, endTime);
      console.log("Duration:", duration);

      this.details.duration.stringValue = duration.stringValue;
      this.details.duration.value = duration.value;
    },
    // log activity
    saveActivity() {
      // Get user Id
      const token = localStorage.getItem('authToken');
      const decoded = jwtDecode(token);
      const userId = decoded.user_id;

      const data = {
        _id: uuidv4(),
        user_id: userId,
        ActivityName: this.user_ActivityName,
        ActivityType: this.activityName,
        details: Object.fromEntries(Object.entries(this.details).filter(([key, value]) => value.value !== ""))
      };

      axios.post('http://127.0.0.1:5000/log_activity', data)
        .then(response => {
          console.log('Activity logged:', response.data);
          alert('Activity logged successfully!');
          this.$router.push('/');
        })
        .catch(error => {
          console.error('There was an error logging the activity!', error);
          alert('There was an error logging the activity!');
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

.save-button {
  background: #57b846;
}

.btn-dropdown {
  background: #57b846;
  margin: 0;
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