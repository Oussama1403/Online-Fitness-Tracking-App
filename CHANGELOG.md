# Changelog

## Aug 19,2024

- **Added Introductory Text to Pages**: Introduced a brief, explanatory text at the top of the 'Activities,' 'Create Workout,' and 'Set Fitness Goal' pages to guide users on the purpose of each page.
- **Aesthetic Enhancements:** Implemented a fade-in effect for each page to enhance the user experience with smooth transitions.

## Aug 18, 2024

#### **Design and Animation**
- **Improved Cards Design**: Enhanced the visual appearance of dashboard cards for a more appealing and consistent design.
- **Adjusted Fade In Animation**: Refined the fade-in animation for dashboard cards to improve user experience.

#### **Documentation**
- **Updated README**: Added detailed information on all features of the app to provide better clarity and guidance.
- **Updated Screenshots**.
- **Updated requirements.txt**.

#### **Features**
- **Active Minutes Tracking**: Implemented a feature to track and display the total number of active minutes or time spent on activities to encourage user motivation.

#### **Activity Logging**
- **Duration Calculation**: Added a function to calculate the duration based on start time and end time.
  - The **duration** field is now read-only and displays the calculated duration in a human-readable format.
  - **Dashboard**: Duration is displayed in a human-readable format.

#### **Custom Activity**
- **Start and End Time Fields**: Added fields for start time and end time in custom activities. Duration is now calculated automatically based on these times.

#### **Active Minutes Calculations**
- **Updated Calculation**: Adjusted active minutes calculations to use the new duration format.

#### **Bug Fixes and Improvements**
- **Fixed Bugs**: Resolved various bugs and performed code improvements to enhance the overall stability and performance of the app.

## Aug 16, 2024

1. **Implemented User Authentication**
   - Secure login and registration functionality added.
   - Utilizes JWT for managing user-specific data across the application.

2. **Data Management Enhancement**
   - Ensured that every piece of data in MongoDB is linked to the user who created it.
   - Added `user_id` to every data entry for proper user-specific data handling.

#### **Bug Fixes**

1. **Custom Activity Routing Fix**
   - Resolved an issue where saving a custom activity did not redirect to the dashboard.
   
2. **Calories Calculation Fix**
   - Fixed a bug where custom activities were not included in the total calories calculation.

3. **Multiple Bugs**
   - Fixed various minor bugs to improve overall stability.

#### **UI/UX Improvements**

1. **Activity Duration Input Improvement**
   - Updated input to allow users to type `:` between numbers to specify minutes in the activity duration.

2. **Sidebar Icon Colors**
   - Each icon on the sidebar now features a unique color for better visual distinction.

3. **Card Design Enhancement**
   - Added a box shadow to each card for a more modern and polished look.

4. **Improved Form Interactions**
   - Enhanced input fields with better hover and focus effects for a smoother user experience.

#### **Documentation**

1. **Added Screenshots to README.md**
   - Updated the README file with new screenshots to showcase the application.

2. **Todo List Update**
   - Added a new task in the todo list for implementing a language translation option (EN/FR).
  
## Aug 11, 2024
- **UI Enhancements:**
  - **Dashboard.vue:**
    - Added buttons to guide users to the respective section creation pages when sections are empty.
    - Updated the color scheme of the `Goals` section for better visibility.
  - **BaseLayout.vue:**
    - Enhanced the sidebar links with improved hover effects.
    - Aligned icons and text links for a cleaner and more consistent layout.

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