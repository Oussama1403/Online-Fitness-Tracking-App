# Changelog
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