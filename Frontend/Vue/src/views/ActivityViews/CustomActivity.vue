<template>
  <div class="container custom-container mt-4">
    <Form @submit="saveActivity" v-slot="{ errors }">
      <span class="form-title">
        Log <span class="form-title-activityname">{{ activityType }}</span>
      </span>

      <!-- Activity Name -->
      <div class="form-group">
        <Field type="text" placeholder="Activity name" class="input form-control" id="activityName" name="Activity Name"
          v-model="activityName" rules="required" />
        <ErrorMessage name="Activity Name" class="error-msg" />
      </div>

      <!-- Date -->
      <div class="form-group">
        <Field type="date" class="input form-control" id="activityDate" name="Date" v-model="activityDate"
          rules="required" />
        <ErrorMessage name="Date" class="error-msg" />
      </div>


      <div class="form-group">
        <label for="startTime">Start Time</label>
        <Field type="time" class="input form-control" id="startTime" name="Start Time" v-model="activityStartTime"
          step="1" rules="required" @change="updateDuration" />
        <ErrorMessage name="Start Time" class="error-msg" />
      </div>

      <div class="form-group">
        <label for="endTime">End Time</label>
        <Field type="time" class="input form-control" id="endTime" name="End Time" v-model="activityEndTime" step="1"
          rules="required" @change="updateDuration" />
        <ErrorMessage name="End Time" class="error-msg" />
      </div>

      <!-- fields Section -->
      <div v-for="(labelField, index) in fields" :key="index" class="group mb-3">
        <div class="form-group">
          <Field type="text" placeholder="Label name" class="input form-control label" :id="'labelName' + index"
            v-model="labelField.name" :name="'labelName' + index" rules="required" />
          <ErrorMessage :name="'labelName' + index" class="error-msg" />
        </div>
        <div class="form-group">
          <Field type="text" placeholder="Input value" class="input form-control" :id="'inputValue' + index"
            v-model="labelField.value" :name="'inputValue' + index" rules="required" />
          <ErrorMessage :name="'inputValue' + index" class="error-msg" />
        </div>
        <button type="button" class="remove-button btn btn-danger" @click="removeLabelField(index)">Remove
          Label</button>
      </div>

      <!-- Add New Label Button -->
      <button type="button" class="add-button btn btn-primary mb-3" @click="addLabelField">Add New Label</button>

      <!-- Save Activity Button -->
      <button type="submit" class="save-button btn btn-success">Save Activity</button>
    </Form>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { Field, Form, ErrorMessage } from 'vee-validate';
import axios from 'axios';
import { v4 as uuidv4 } from 'uuid';
import { jwtDecode } from "jwt-decode";


export default {
  setup() {
    const route = useRoute();
    const router = useRouter(); // Use useRouter to access router methods
    const activityType = route.params.activityName || '';

    const activityName = ref('');
    const activityDate = ref('');
    const activityStartTime = ref('');
    const activityEndTime = ref('');
    const fields = ref([{ name: '', value: '' }]);

    const durationDetail = ref({stringValue: '', value: 0 });

    const addLabelField = () => {
      fields.value.push({ name: '', value: '' });
    };

    const removeLabelField = (index) => {
      if (fields.value.length > 1) {
        fields.value.splice(index, 1);
      }
    };

    const calculateDuration = (startTime, endTime) => {
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
    };

    const updateDuration = () => {
      const startTime = activityStartTime.value;
      const endTime = activityEndTime.value;

      const duration = calculateDuration(startTime, endTime);

      durationDetail.value = duration;
      durationDetail.stringValue = duration.stringValue;
    };

    const saveActivity = () => {
      // Get user Id
      const token = localStorage.getItem('authToken');
      const decoded = jwtDecode(token);
      const userId = decoded.user_id;

      // Update duration before saving
      updateDuration();

      // Create the details object using reduce
      const detailsObject = fields.value.reduce((obj, field) => {
        if (field.name && field.value) {
          obj[field.name.toLowerCase().replace(/ /g, '_')] = {
            name: field.name,
            value: field.value
          };
        }
        return obj;
      }, {});

        // Add the date, start_time,end_time and duration detail to the details object
        detailsObject['duration'] = {name: 'Duration', ...durationDetail.value};
        detailsObject['date'] = {name: 'Date', value: activityDate.value };
        detailsObject['start_time'] = {name: 'Start Time', value: activityStartTime.value };
        detailsObject['end_time'] = {name: 'End Time', value: activityEndTime.value };

      const data = {
        _id: uuidv4(),
        user_id: userId,
        ActivityName: activityName.value,
        ActivityType: activityType,
        details: detailsObject,
      };

      axios.post('http://127.0.0.1:5000/log_activity', data)
        .then(response => {
          console.log('Activity logged:', response.data);
          alert('Activity logged successfully!');
          router.push('/');
        })
        .catch(error => {
          console.error('There was an error logging the activity!', error);
          alert('There was an error logging the activity!');
        });
    };

    return {
      activityType,
      activityName,
      activityDate,
      activityStartTime,
      activityEndTime,
      fields,
      addLabelField,
      removeLabelField,
      updateDuration,
      calculateDuration,
      saveActivity
    };
  },
};
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

label {
  color: #515151;
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
  padding-top: 2rem;
  padding-bottom: 2rem;
  border-radius: 5px;
}

.input {
  background: #e6e6e6;
  box-shadow: none;
  font-family: 'Montserrat', sans-serif;
  font-size: 15px;
  line-height: 1.5;
  color: #666666;
  outline: none;
  height: 50px;
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

.label {
  background-color: transparent;
  border-radius: 0px;
  border-top: 0px;
  border-right: 0px;
  border-left: 0px;
  border-bottom: 2px solid #a19f9f;
}

.label:hover {
  border: 0;
  border-bottom: 2px solid #00ff99;
}

.label:focus {
  border: 0;
  border-bottom: 4px solid #00ff99;
  box-shadow: none;
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

.add-button {
  background: #47c1e7;
}

.remove-button {
  background: #f43333;
}

.btn-dropdown {
  background: #57b846;
  margin: 0;
}
</style>