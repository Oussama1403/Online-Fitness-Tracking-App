<template>
    <div>
        <div class="row">
            <div v-if="activities.length === 0" class="section">
                <div style="width: 400px">
                    <router-link to="/activities" class="log-activity button btn fade-in">Log your first
                        activity!</router-link>
                </div>
            </div>

            <div v-for="(activity, index) in activities" :key="index" class="col-xl-4 col-md-6 mb-4 fade-in">
                <div class="card activities-section" @click="goToEdit(activity, 'edit-activity')">
                    <div class="card-body">
                        <h5 class="card-title text-center">{{ activity.ActivityName }}</h5>
                        <hr />
                        <div v-for="(detail, key) in activity.details" :key="key">
                            <p class="card-text detail-name mb-1">
                                {{ detail.name }}:
                            </p>
                            <p class="card-text">
                                <strong class="detail-value">{{ detail.name === 'Duration' ? detail.stringValue :
                                    detail.value }}</strong>
                                <strong v-if="detail.unit" class="detail-value">{{ detail.unit }}</strong>
                            </p>
                            <hr />
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
        activities: Array
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

.activities-section {
    /*background: linear-gradient(135deg, #9114ff, #d666ed);/*/
    background: linear-gradient(to bottom right, #eac3fc, #8ef1fc);
    flex-direction: column;
    justify-content: flex-start;
    padding: 5px;
    /* Optional: Spacing inside the card */
}

.activities-section:hover {
    background: linear-gradient(to bottom right, #e5adff, #8ef1fc);
    transform: translateY(-5px);
    box-shadow: 20px 20px 20px rgba(0, 0, 0, 0.15);
}

.detail-value {
  font-size: 1.1em;
  font-weight: bold;
}

.log-activity {
    background: transparent;
    border: 2px solid #da6bff;
    color: #da6bff;
}

.log-activity:hover {
    background: #da6bff;
    color: #ffffff;
}

.log-activity:focus {
    background: #bf18f7;
    color: #ffffff;
    border: none;
}
</style>