<template>
  <div class="container custom-container mt-4">
    <Form @submit="saveActivity" v-slot="{ errors }">
      <span class="form-title">
        Log <span class="form-title-activityname">{{ activityType }}</span>
      </span>

      <!-- Activity Name -->
      <div class="form-group">
        <Field type="text" placeholder="Activity name" class="input form-control" id="activityName" name="activityName"
          v-model="activityName" rules="required" />
        <ErrorMessage name="activityName" class="error-msg" />
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
        <button type="button" class="remove-button btn btn-danger" @click="removeLabelField(index)">Remove Label</button>
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
import { useRoute } from 'vue-router';
import { Field, Form, ErrorMessage } from 'vee-validate';
import axios from 'axios';
import { v4 as uuidv4 } from 'uuid';


export default {
  setup() {
    const route = useRoute();
    const activityType = route.params.activityName || '';

    const activityName = ref('');
    const fields = ref([{ name: '', value: '' }]);

    const addLabelField = () => {
      fields.value.push({ name: '', value: '' });
    };

    const removeLabelField = (index) => {
      if (fields.value.length > 1) {
        fields.value.splice(index, 1);
      }
    };

    const saveActivity = () => {
      const data = {
        _id: uuidv4(),
        ActivityName: activityName.value,
        ActivityType: activityType,
        details: fields.value,
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
    };

    return {
      activityType,
      activityName,
      fields,
      addLabelField,
      removeLabelField,
      saveActivity,
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
  
  .label {
    background-color: transparent;
    border-radius: 0px;
    border-top: 0px ;
    border-right: 0px;
    border-left: 0px;
    border-bottom: 2px solid #a19f9f;
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
 