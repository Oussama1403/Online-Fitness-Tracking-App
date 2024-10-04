<template>
    <div>
        <div v-if="meals.length === 0" class="section fade-in">
            <div style="width: 400px">
                <router-link to="/log-meal" class="log-meal button btn">Log your first meal!</router-link>
            </div>
        </div>
        <div class="row">
            <div v-for="(meal, index) in meals" :key="index" class="col-xl-4 col-md-6 mb-4 fade-in">
                <div class="card meals-section h-100" @click="goToEdit(meal, 'edit-meal')">
                    <div class="card-body">
                        <h5 class="card-title text-center">{{ meal.mealName }}</h5>
                        <hr />
                        <div style="color: #424242">
                            <p class="title mb-1">Meal Date:</p>
                            <span style="font-size: 1.2em; font-weight: bold;">{{ meal.mealDate }}</span>
                        </div>
                        <hr />
                        <div class="mb-1">
                            <span class="card-text detail-name">Food Items:</span>
                            <ul class="food-items-list details-value">
                                <li v-for="item in meal.foodItems.split(',')" :key="item">{{ item.trim() }}</li>
                            </ul>
                        </div>
                        <hr />
                        <p class="card-text detail-name mb-1">Calories:</p>
                        <span class="detail-value">{{ meal.calories }}</span>
                        <hr />
                        <p class="card-text detail-name mb-1">Protein:</p>
                        <span class="detail-value">{{ meal.protein }}</span>
                        <hr />
                        <p class="card-text detail-name mb-1">Carbs:</p>
                        <span class="detail-value">{{ meal.carbs }}</span>
                        <hr />
                        <p class="card-text detail-name">Fats:</p>
                        <span class="detail-value">{{ meal.fats }}</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        meals: Array
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

.meals-section {
    background: linear-gradient(to bottom right, #ffebfb, #f48fe2);
    /* Softer gradient */
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    padding: 5px;
    /* Optional: Spacing inside the card */
}

.meals-section:hover {
    background: linear-gradient(to bottom right, #ffc2f3, #f48fe2);
    transform: translateY(-5px);
    box-shadow: 20px 20px 20px rgba(0, 0, 0, 0.15);
}

.detail-value {
  font-size: 1.2em;
  font-weight: bold;
  color: #AD1457;
}

ul.food-items-list {
    list-style-type: disc;
    padding-left: 20px;
    margin: 5px 0;
}

ul.food-items-list li {
    font-size: 1em;
    color: #D81B60 ;
    font-weight: bold;
}

.list-group-item {
    background: none;
    border: 0;
    color: inherit;
}

.log-meal {
    background: transparent;
    border: 2px solid #f534ff;
    color: #f534ff;
}

.log-meal:hover {
    background: #e763ee;
    color: #ffffff;
}

.log-meal:focus {
    background: #f30aff;
    color: #ffffff;
    border: none;
}
</style>