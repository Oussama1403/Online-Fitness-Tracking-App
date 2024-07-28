<template>
  <div>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand ps-3" href="#">Online Fitness Tracking App</a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">
          <!-- Add any additional navbar items here -->
        </ul>
      </div>
    </nav>

    <!-- Main Content -->
    <div class="container-fluid">
      <div class="row">
        <!-- Sidebar -->
        <nav id="sidebar" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
          <div class="position-sticky">
            <ul class="nav flex-column">
              <li class="nav-item">
                <router-link to="/" class="nav-link active" aria-current="page">
                  Dashboard
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/log-activity" class="nav-link">
                  Log Activity
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/view-activities" class="nav-link">
                  View Activities
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/create-workout" class="nav-link">
                  Create Workout Routine
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/view-workouts" class="nav-link">
                  View Workouts
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/set-fitness-goals" class="nav-link">
                  Set Fitness Goals
                </router-link>
              </li>
            </ul>
          </div>
        </nav>

        <!-- Content -->
        <main class="col-md-9 ml-sm-auto col-lg-10 px-md-4">
          <router-view />
        </main>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BaseLayout",
};
</script>

<style scoped>
.navbar-brand {
  font-size: 1.25rem;
}

#sidebar {
  height: 100vh;
  padding-top: 1rem;
  position: fixed;
}

.sidebar-footer {
  position: absolute;
  bottom: 0;
  width: 100%;
}

.nav-link.active {
  font-weight: bold;
  color: #007bff;
}

.nav-link {
  color: #000;
  transition: color 0.2s;
}

.nav-link:hover {
  color: #007bff;
}

.main-content {
  margin-left: 250px; /* Width of the sidebar */
  padding: 2rem;
}
</style>
