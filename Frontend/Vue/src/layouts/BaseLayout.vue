<template>
  <div>
    <!-- Main Content -->
    <div class="container-fluid">
      <div class="row">
        <!-- Sidebar -->
        <nav id="sidebar" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
          <div class="position-sticky">
            <ul class="nav flex-column">
              <router-link to="/" class="brand-link" aria-current="page">
                <li class="brand">
                  Online Fitness Tracking App
                </li>
              </router-link>

              <hr style="border: 3px solid green;">

              <li class="nav-item">
                <router-link to="/" class="nav-link" aria-current="page">
                  <i class="fas fa-tachometer-alt"></i> Dashboard
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/activities" class="nav-link">
                  <i class="fas fa-running"></i> Activities
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/create-workout" class="nav-link">
                  <i class="fas fa-dumbbell"></i> Create Workout Routine
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/set-goal" class="nav-link">
                  <i class="fas fa-bullseye"></i> Set Fitness Goals
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

#sidebar {
  height: 100vh;
  padding-top: 1rem;
  position: fixed;
}
.brand {
  position: relative;
  padding: 10px 20px;
  font-family: 'Montserrat', sans-serif;
  text-decoration: none;
  transition: color 0.3s;
  font-size: 1.25rem;
  font-weight: 700;
  color: rgb(37, 211, 37)
}

.brand:hover {
  border-radius: 10px;
  color: rgb(236, 244, 253) ;
  background-color: rgb(37, 211, 37) ;
}
.brand-link { /* unstyled link*/
  color: inherit; 
  text-decoration: none;
  background: none; 
  border: none;
  padding: 0; 
  margin: 0;
  display: inline; 
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
  background-color: rgb(37, 211, 37);  /* The color of the underline */
  visibility: hidden;
  transform: scaleX(0);
  transition: all 0.3s ease-in-out;
}

.nav-item:hover::before {
  visibility: visible;
  transform: scaleX(1);
}

.nav-link {
  color: #1e1e1e;
  transition: color 0.2s;
}

.nav-link i {
  margin-right: 8px; /* Adjust the spacing between the icon and text */
}

.nav-link:hover {
  color: rgb(37, 211, 37);
}

.nav-link:active {
  color: rgb(24, 158, 24);
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
