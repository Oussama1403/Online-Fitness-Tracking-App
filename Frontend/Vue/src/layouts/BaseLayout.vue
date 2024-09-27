<template>
  <div>
    <!-- Navbar for small screens -->
    <nav class="navbar navbar-expand-md navbar-light bg-light d-md-none">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand brand-link">
          <span class="text-center brand m-1">FitTracker</span>
        </router-link>
        <button class="navbar-toggler" type="button" @click="toggleSidebar">
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>
    </nav>

    <!-- Main Content -->
    <div class="container-fluid">
      <div class="row">
        <!-- Sidebar -->
        <nav
          id="sidebar"
          :class="[
            'col-md-3',
            'col-lg-2',
            'd-md-block',
            'sidebar',
            { 'show-sidebar': isSidebarOpen }
          ]"
        >
          <div class="position-sticky">
            <ul class="nav flex-column">
              <router-link to="/" class="brand-link brand-sidebar" aria-current="page">
                <li class="text-center brand">FitTracker</li>
              </router-link>
              <hr class="brand-sidebar" style="border: 3px solid green" />

              <router-link
                v-for="route in routes"
                :key="route.path"
                :to="route.path"
                class="nav-item nav-link"
                :class="{ active: isActiveRoute(route) }"
              >
                <i :style="{ color: route.bgcolor }" :class="route.icon"></i> {{ route.name }}
              </router-link>

              <router-link to="/" class="nav-item nav-link" @click.prevent="logout">
                <i style="color: #4099ff" class="fas fa-sign-out-alt"></i> Log Out
              </router-link>
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
  name: 'BaseLayout',
  data() {
    return {
      isSidebarOpen: false,
      routes: [
        { path: '/', name: 'Dashboard', icon: 'fas fa-tachometer-alt', bgcolor: '#1eec63' },
        { path: '/activities', name: 'Activities', icon: 'fas fa-running', bgcolor: '#9114ff' },
        {
          path: '/create-workout',
          name: 'Create Workout Routine',
          icon: 'fas fa-dumbbell',
          bgcolor: '#fb6c19'
        },
        {
          path: '/set-goal',
          name: 'Set Fitness Goals',
          icon: 'fas fa-bullseye',
          bgcolor: '#ff3434'
        },
        {
          path: '/log-meal',
          name: 'log Meal',
          icon: 'fa fa-cutlery',
          bgcolor: '#f534ff'
        }
      ]
    }
  },
  methods: {
    toggleSidebar() {
      this.isSidebarOpen = !this.isSidebarOpen
    },
    isActiveRoute(route) {
      return this.$route.path === route.path
    },
    logout() {
      localStorage.removeItem('authToken')
      this.$router.push('/login') // Redirect to login page
    }
  }
}
</script>

<style scoped>
.navbar {
  background-color: rgb(236, 244, 253);
  color: rgb(18, 17, 17);
  z-index: 1040; /* Ensure navbar is above the sidebar */
}

#sidebar {
  height: 100vh;
  padding-top: 1rem;
  position: fixed;
  z-index: 1030; /* Sidebar z-index */
  left: 0;
  top: 0;
  background: -webkit-linear-gradient(left, #c6ffd9, #e0fff2);
}

.show-sidebar {
  display: block !important; /* Override the display property on small screens */
}

.brand {
  position: relative;
  padding: 10px;
  font-family: 'Montserrat', sans-serif;
  text-decoration: none;
  transition: color 0.3s;
  font-size: 1.75rem;
  font-weight: 700;
  border-radius: 10px;
  color: rgb(236, 244, 253);
  background: -webkit-linear-gradient(left, #0cf65a, #00ff95);
  transition: all 0.3s ease-in-out;
}

.brand:hover {
  background-color: rgb(37, 184, 37);
}

.brand-link {
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
  padding: 20px 20px;
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  color: #333;
  text-decoration: none;
  transition: color 0.3s;
  display: flex;
  align-items: center;
}
.nav-item i {
  min-width: 30px; /* Ensures consistent spacing */
  text-align: center; /* Centers the icon in the space */
  margin-right: 10px;
}
/*
.nav-item::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  bottom: 0;
  left: 0;
  background-color: rgb(37, 211, 37);
  visibility: hidden;
  transform: scaleX(0);
  transition: all 0.3s ease-in-out;
}

.nav-item:hover::before {
  visibility: visible;
  transform: scaleX(1);
}
*/
.nav-link {
  color: #1e1e1e;
  transition: color 0.2s;
  border-radius: 10px;
  transition: all 0.3s ease-in-out;
}

.nav-link i {
  margin-right: 8px;
}

.nav-link:hover {
  background-color: rgb(129, 255, 129);
  color: rgb(1, 96, 1);
}

.nav-link:active {
  color: rgb(173, 255, 173);
}

.sidebar-footer {
  position: absolute;
  bottom: 0;
  width: 100%;
}

.main-content {
  margin-left: 250px;
  padding: 2rem;
}

/* Add custom styles for responsive sidebar */
@media (max-width: 767.98px) {
  #sidebar {
    display: none;
    z-index: 1030; /* Ensure the sidebar is on top */
  }
  .brand-sidebar {
    display: none;
  }
  #sidebar.show-sidebar {
    display: block;
    position: fixed;
    top: 56px; /* Height of navbar */
    left: 0;
    width: 250px;
    height: calc(100vh - 56px); /* Adjust height to fit below navbar */
    background-color: white;
    z-index: 1030; /* Sidebar z-index should be less than navbar */
  }
}
</style>
