<template>
  <div class="container custom-container mt-4">
    <Form @submit="saveActivity" v-slot="{ errors }">
      <span class="form-title">
        Log <span class="form-title-activityname">{{ activityName }}</span>
      </span>

      <!-- Activity Name: -->
      <div class="form-group">
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
              v-model="detail.value" step="1" rules="required" />
            <ErrorMessage :name="detail.name" class="error-msg" />
          </template>

          <!-- Render End Time input -->
          <template v-else-if="detail.name === 'End Time'">
            <label :for="detail.name + index">{{ detail.name }}</label>
            <Field type="time" class="input form-control" :id="detail.name + index" :name="detail.name"
              v-model="detail.value" step="1" rules="required" />
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
              class="input form-control" rules="required|numeric" />
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
                  v-model="detail.value" rules="required|numeric|non_negative" />
                <div class="input-group-append">
                  <button class="btn-dropdown btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown"
                    aria-haspopup="true" aria-expanded="false">
                    {{ detail.unit || 'Unit' }}
                  </button>
                  <div class="dropdown-menu dropdown-menu-right">
                    <a class="dropdown-item" href="#" @click.prevent="detail.unit = 'seconds'">Seconds</a>
                    <a class="dropdown-item" href="#" @click.prevent="detail.unit = 'minutes'">Minutes</a>
                    <a class="dropdown-item" href="#" @click.prevent="detail.unit = 'hours'">Hours</a>
                  </div>
                </div>
              </div>
              <!-- the hidden field allows us to make vee-validate aware of the unit selection and apply the custom unit_required validation rule to it. -->
              <Field
              type="hidden"
              :name="'detail.unit' + index"
              v-model="detail.unit"
              rules="unit_required"
               />
              <ErrorMessage :name="'detail.unit' + index" class="error-msg" />
            </div>
            <ErrorMessage :name="detail.name" class="error-msg" />
          </template>


          <template v-else-if="detail.name === 'Distance'">
            <div class="form-group">
              <label :for="detail.name + index">{{ detail.name }}</label>
              <div class="input-group">
                <Field type="text" class="input form-control" :id="detail.name + index" :name="detail.name"
                  v-model="detail.value" rules="required|numeric|non_negative" />
                <div class="input-group-append">
                  <button class="btn-dropdown btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown"
                    aria-haspopup="true" aria-expanded="false">
                    {{ detail.unit || 'Unit' }}
                  </button>
                  <div class="dropdown-menu dropdown-menu-right">
                    <a class="dropdown-item" href="#" @click.prevent="detail.unit = 'Meters'">Meters</a>
                    <a class="dropdown-item" href="#" @click.prevent="detail.unit = 'Kilometers'">Kilometers</a>
                  </div>
                </div>
              </div>
              <!-- the hidden field allows us to make vee-validate aware of the unit selection and apply the custom unit_required validation rule to it. -->
              <Field
              type="hidden"
              :name="'detail.unit' + index"
              v-model="detail.unit"
              rules="unit_required"
               />
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
              v-model="detail.value" rules="required" />
            <ErrorMessage :name="detail.name" class="error-msg" />
          </template>
        </div>
      </div>


      <!-- Save Button -->
      <button type="submit" class="save-button btn btn-success">Save Activity</button>
    </Form>
  </div>
</template>

<script>
import axios from 'axios';
import { Field } from 'vee-validate';

export default {
  data() {
    return {
      details: [
        { name: 'Date', value: '' },
        { name: 'Start Time', value: '' },
        { name: 'End Time', value: '' },
        { name: 'Exercise Type', value: ''}, 
        { name: 'Weight Lifted', value: ''},
        { name: 'Reps', value: ''},
        { name: 'Sets', value: ''},
        { name: 'Intensity', value: ''},
        { name: 'Duration', value: '', unit: '' },
        { name: 'Distance', value: '', unit: '' },
        { name: 'Calories Burned', value: '' },
        { name: 'Comments', value: '' },
      ],
      user_ActivityName: '',
      activityName: this.$route.params.activityName || '',
    };
  },
  computed: {
    filteredDetails() {
      // Filter details based on the activity name
      return this.details.filter(detail => {
        if (this.activityName === 'Weightlifting' && detail.name === 'Distance') {
          return false;
        }
        if (this.activityName !== 'Weightlifting' && (detail.name === 'Exercise Type' || detail.name === 'Weight Lifted' || detail.name === 'Reps' || detail.name === 'Sets' || detail.name === 'Intensity' )) {
          return false;
        }
        // Add more conditions for other activity names if needed
        return true;
      });
    }
  },
  methods: {
    // log activity
    saveActivity() {

      let data = {
        'user_ActivityName': this.user_ActivityName
      };
      // fill data from details array
      this.details.forEach(detail => {
        data[detail.name] = detail.value;
      });

      axios.post('http://127.0.0.1:5000/log_activity', data)
        .then(response => {
          console.log('Activity logged:', response.data);
        })
        .catch(error => {
          console.error('There was an error logging the activity!', error);
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
</style>