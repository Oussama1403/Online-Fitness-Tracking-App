<template>
  <div class="dashboard">
    <div class="container-fluid px-4">
      <h1 class="mt-4">Dashboard</h1>
      <div class="row">
        <div class="col-xl-3 col-md-6 mb-4">
          <div class="card bg-primary text-white h-100">
            <div class="card-body">
              <div class="card-body-icon">
                <i class="fas fa-dumbbell"></i>
              </div>
              <div class="mr-5">8 WORKOUTS COMPLETED</div>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-md-6 mb-4">
          <div class="card bg-success text-white h-100">
            <div class="card-body">
              <div class="card-body-icon">
                <i class="fas fa-fire"></i>
              </div>
              <div class="mr-5">500 CALORIES BURNED</div>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-md-6 mb-4">
          <div class="card bg-info text-white h-100">
            <div class="card-body">
              <div class="card-body-icon">
                <i class="fas fa-calendar-alt"></i>
              </div>
              <div class="mr-5">3 WORKOUT PLANS</div>
              <div class="progress progress-sm my-2">
                <div class="progress-bar bg-white" role="progressbar" style="width: 60%" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"></div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-md-6 mb-4">
          <div class="card bg-warning text-white h-100">
            <div class="card-body">
              <div class="card-body-icon">
                <i class="fas fa-clock"></i>
              </div>
              <div class="mr-5">2 UPCOMING WORKOUTS</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Dashboard",
};
</script>

<style scoped>
.dashboard {
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
.card-body-icon {
  position: absolute;
  top: 0.75rem;
  right: 0.75rem;
  opacity: 0.4;
  font-size: 2.5rem;
}
</style>
