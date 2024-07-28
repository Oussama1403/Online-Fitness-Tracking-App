<template>
  <div>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg">
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
                <router-link to="/" class="nav-link" aria-current="page">
                  Dashboard
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/activities" class="nav-link">
                  Activities
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/create-workout" class="nav-link">
                  Create Workout Routine
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
.navbar {
  background-color: rgb(236, 244, 253);
  color: rgb(18, 17, 17);
}
.navbar-brand {
  font-size: 1.25rem;
  font-weight: 700;
}

#sidebar {
  height: 100vh;
  padding-top: 1rem;
  position: fixed;
}

.nav-item {
  position: relative;
  padding: 10px 20px;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  color: #333;
  text-decoration: none;
  transition: color 0.3s;
}

.nav-item::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 3px;
  bottom: 0;
  left: 0;
  background-color: #1e1e1e; /* The color of the underline */
  visibility: hidden;
  transform: scaleX(0);
  transition: all 0.3s ease-in-out;
}

.nav-item:hover::before {
  visibility: visible;
  transform: scaleX(1);
}

.nav-link.active {
  font-weight: bold;
  color: #007bff;
}

.nav-link {
  color: #1e1e1e;
  transition: color 0.2s;
}

.sidebar-footer {
  position: absolute;
  bottom: 0;
  width: 100%;
}

.main-content {
  margin-left: 250px; /* Width of the sidebar */
  padding: 2rem;
}
</style>
