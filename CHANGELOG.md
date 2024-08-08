# Changelog

## Aug 8, 2024
- **Transitioned from SQLite3 to MongoDB:**
  - Migrated the project’s database from SQLite3 to MongoDB for improved scalability and flexibility.
- Created a new `CustomActivity` component that allows users to dynamically create and manage custom labels and values for activities.
- `Dashboard.vue`:
  - Updated dashboard cards to display real data based on activities, workouts, and goals.
  - Fixed errors related to data formatting and processing in Dashboard.vue.
  - Enhanced data fetching and error handling in Dashboard.vue to ensure robust performance and user feedback.
  - Added calculations to display the number of completed workouts, calories burned, upcoming workouts, and goals set.
- `app.py`:
  - Added update routes for activities, workouts, and goals:
  - Updated delete routes to delete by ID:
- Added `CustomActivity` Component that allows users
- `vite.config.js`:
  - Updated to allow the development server to start on a local IP address instead of just localhost. See README.md for instructions.
- Update README.md, included MongoDB Installation Instructions.
- Update TODO.md

## Aug 6, 2024
- `BaseLayout.vue`:
  - Implemented a responsive layout where a navbar appears at the top on small screen sizes, with a toggle icon to expand the sidebar
  - Code improved with List Rendering (`v-for`).

## Aug 4, 2024
- Limit exercise deletion to ensure at least one exercise field remains in `CreateWorkout.vue`.
- `LogActivity.vue`: Show all fields when Creating Custom Activity.

## Aug 3, 2024

### Forms Validation
- Implemented Vee-Validate to check for empty fields, string and numeric fields in:
  - CreateWorkout
  - setFitnessGoal
  - Log Activity

### Dynamic Field Names Handling
- Handled dynamic field names using Vee-Validate library across forms.

### UI Consistency
- Fixed and standardized UI across all forms to ensure consistency.

### Log Activity Form
- Added labels for start time and end time.
- Added seconds to the time input.
- For weightlifting activities, included fields for Exercise Type, Weight Lifted, Reps, Sets, and Intensity.
- Fixed duration format to allow only numbers and include minutes and hours as units.
- Fixed distance format to allow only numbers and include meters and kilometers as units.
- Ensured that number inputs are non-negative.

### Create Workout Form
- Prevent saving a workout if the exercise fields are not filled out.

### Views Folder
- Reorganized views components into appropriate folders.

## Jul 31, 2024
- Improved UI of all components for better aesthetics.
- Added new component: `setFitnessGoal.vue`.
- Made all cards in the dashboard clickable, routing to their respective "edit" routes.
- Added components for editing:
  - `EditActivity.vue`
  - `EditWorkout.vue`
  - `EditGoal.vue`

## Jul 29, 2024
- Update Dashboard: Display Workout Routines, Activities Logged.

## Jul 28, 2024
- Updated Frontend: Added `Create Workout Routine` Component.
- Updated Frontend: Added `Activity` Component.
- Updated Frontend: Added `Log Activity` Component.

## Jul 26, 2024
- Commit first stable project files.