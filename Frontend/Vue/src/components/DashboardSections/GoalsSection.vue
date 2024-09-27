<template>
    <div>
        <h2 class="mb-4 mt-4 goals-title fade-in">Your Current Goals</h2>
        <hr style="border: 3px solid #ff3434" />
        <div v-if="goals.length === 0" class="section fade-in">
            <div style="width: 400px">
                <router-link to="/set-goal" class="log-goal button btn">Log your first goal!</router-link>
            </div>
        </div>
        <div class="row">
            <div v-for="(goal, index) in goals" :key="index" class="col-xl-4 col-md-6 mb-4 fade-in">
                <div class="card current-goals-section" @click="goToEdit(goal, 'edit-goal')">
                    <div class="card-body">
                        <h5 class="card-title text-center">{{ goal.type }}</h5>
                        <hr />
                        <div style="color: #424242">
                            <p class="title mb-1">Description:</p>
                            <span style="font-size: 1.2em; font-weight: bold;">{{ goal.description }}</span>
                        </div>
                        <hr />
                        <p class="card-text detail-name mb-1">Target Date:</p>
                        <p class="detail-value">{{ goal.targetDate }}</p>
                        <hr />
                        <p class="card-text detail-name mb-1">Current Progress:</p>
                        <p class="detail-value">{{ goal.currentProgress }}</p>
                        <div v-if="goal.notes">
                            <p class="card-text mb-1 detail-name">
                                <hr />Notes:
                            </p>
                            <p class="detail-value">{{ goal.notes }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        goals: Array
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

.current-goals-section {
    background: linear-gradient(to bottom right, #FFCDD2, #F06292);
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    padding: 5px;
    /* Optional: Spacing inside the card */
}

.current-goals-section:hover {
    background: linear-gradient(to bottom right, #ff87a3, #ff5d6d);
    transform: translateY(-5px);
    box-shadow: 20px 20px 20px rgba(0, 0, 0, 0.15);
}

.goals-title {
    background: linear-gradient(to bottom right, #fb7091, #f73158);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
}

.detail-value {
  font-size: 1.1em;
  font-weight: bold;
  color: #D32F2F;
}

.log-goal {
    background: transparent;
    border: 2px solid #ff3434;
    color: #ff3434;
}

.log-goal:hover {
    background: #f54c4c;
    color: #ffffff;
}

.log-goal:focus {
    background: #ff2a2a;
    color: #ffffff;
    border: none;
}
</style>