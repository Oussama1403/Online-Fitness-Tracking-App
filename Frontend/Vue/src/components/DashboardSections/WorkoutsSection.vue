<template>
    <div>
        <div v-if="workouts.length === 0" class="section fade-in">
            <div style="width: 400px">
                <router-link to="/create-workout" class="log-workout button btn">Log your first workout!</router-link>
            </div>
        </div>
        <div class="row">
            <div v-for="(workout, index) in workouts" :key="index" class="col-xl-4 col-md-6 mb-4 fade-in">
                <div class="card saved-workouts-section" @click="goToEdit(workout, 'edit-workout')">
                    <div class="card-body">
                        <h5 class="card-title text-center">{{ workout.WorkoutName }}</h5>
                        <hr />
                        <p class="card-text title date-section mb-1">Workout Date:</p>
                        <strong class="card-text date-section" style="font-size: 1.2em;">
                            {{ workout.WorkoutDate }}
                        </strong>
                        <hr />
                        <li style="list-style-type: none" v-for="(exercise, index) in workout.Exercises" :key="index">
                            <div class="list-group-item">
                                <div class="exercise">
                                    <p class="card-text exercise-name mb-1">{{ exercise.name }}</p>
                                    <div class="workout-details">
                                        <div class="detail-item">
                                            <span class="detail-name"> Reps:</span> <span class="detail-value">{{
                                                exercise.reps }}</span>
                                        </div>
                                        <div class="detail-item">
                                            <span class="detail-name"> Sets:</span> <span class="detail-value">{{
                                                exercise.sets }}</span>
                                        </div>
                                    </div>
                                </div>
                                <hr />
                            </div>
                        </li>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        workouts: Array
    },
    methods: {
        goToEdit(item, routeName) {
            const clonedItem = JSON.stringify(item)
            console.log('clonedItem :', clonedItem)
            this.$router.push({
                name: routeName,
                query: { item: clonedItem }
            })
        }
    }
};
</script>

<style scoped>
@import "@/assets/SharedCardStyles.css";

.saved-workouts-section {
    background: linear-gradient(to bottom right, #fcecc3, #f6fc8e);
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    padding: 5px;
    /* Optional: Spacing inside the card */
}

.saved-workouts-section:hover {
    background: linear-gradient(to bottom right, #ffe49e, #f6fc8e);
    transform: translateY(-5px);
    box-shadow: 20px 20px 20px rgba(0, 0, 0, 0.15);
}


.workout-details {
    display: flex;
    flex-direction: column;
    /* Stack items vertically */
}

.date-section {
    color: #424242;
}

.exercise-name {
    color: #c55e84;
    font-size: 1.3em;
    font-weight: bold;
}

.detail-item {
  display: flex;
  justify-content: space-between;
  /* Space between label and value */
  width: 100px;
  /* Set a consistent width to align values */
}

.detail-value {
  font-size: 1.1em;
  font-weight: bold;
  color: #ec8d3a;
}

.log-workout {
    background: transparent;
    border: 2px solid #ff8640;
    color: #ff8640;
}

.log-workout:hover {
    background: #ffa16b;
    color: #ffffff;
}

.log-workout:focus {
    background: #ff7525;
    color: #ffffff;
    border: none;
}
</style>