<template>
    <div class="activities">
      <div class="container-fluid px-4">
        <h2 class="mb-4 mt-4 text-center title fade-in">Activities</h2>
        <h5 class="mb-4 mt-4 text-center intro-text fade-in">Track your progress by logging the activities <span class="intro-important"> you've completed.</span></h5>
        <div class="row">
          <div class="col-xl-3 col-md-6 mb-4" v-for="activity in activities" :key="activity.name">
            <div class="card text-center bg-light text-dark h-100 fade-in">
              <img :src="activity.image" class="card-img-top" :alt="activity.name">
              <div class="card-body">
                <div class="fw-bold">{{ activity.name }}</div>
                <router-link :to="{ name: 'LogActivity', params: { activityName: activity.name } }" class="btn btn-primary mt-3">
                  Log {{ activity.name }}
                </router-link>
              </div>
            </div>
          </div>
          <div class="col-xl-3 col-md-6 mb-4">
          <div class="card text-center bg-light text-dark h-100 fade-in">
              <img src='@/assets/images/custom.png' class="card-img-top" alt="custom">
              <div class="card-body">
                <div class="fw-bold">Add your own activity</div>
                <router-link :to="{ name: 'CustomActivity', params: { activityName: custom_activity } }" class="btn btn-primary mt-3">
                  Log Activity
                </router-link>
              </div>
           </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Activities",
    data() {
      return {
        activities: [
          { name: 'Running', image: 'src/assets/images/running.png' },
          { name: 'Cycling', image: 'src/assets/images/cycling.png'},
          { name: 'Swimming', image: 'src/assets/images/swimming.png' },
          { name: 'Weightlifting', image: 'src/assets/images/weightlifting.png' },
          { name: 'Walking', image: 'src/assets/images/walking.png'}
        ],
        custom_activity: 'Custom Activity'
      };
    }
  };
  </script>
  
  <style scoped>
  .activities {
    font-family: 'Montserrat', sans-serif;
    margin-top: 20px;
  }
  .title {
    color: #57B846;
    font-weight: 700;
  }
  .intro-text {
    color: #333333;
    padding-bottom: 15px;
  }
  .intro-important {
    color: #57B846;
  }
  .card {
    border: none;
    border-radius: 0.75rem;
    transition: all 0.3s ease-in-out;
  }
  .card:hover {
    transform: scale(1.05);
  }
  .card-body-icon {
    position: absolute;
    top: 0.75rem;
    right: 0.75rem;
    opacity: 0.4;
    font-size: 2.5rem;
  }
  .card-img-top {
    border-radius: 0.75rem 0.75rem 0 0;
    height: 150px;
    object-fit: contain;
    width: 100%; /* This makes sure the image takes the full width of the container */
  }
  .btn-primary {
    background-color: #007bff;
    border: none;
    border-radius: 25px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    padding: 10px 20px;
  }
  .btn-primary:hover {
    background-color: #0056b3;
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
  