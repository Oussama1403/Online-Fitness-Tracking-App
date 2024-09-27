<template>
    <MealForm :mode="'Edit'" :meal="meal" :errorMessage="errorMessage" @submit="saveMeal"  @delete="deleteMeal"
    />
</template>

<script>
import MealForm from '@/components/MealForm.vue';
import axios from 'axios';

export default {
    name: 'EditMeal',
    components: {
        MealForm,
    },
    data() {
        return {
            meal: {
                mealName: '',
                mealDate: '',
                foodItems: '',
                calories: 0,
                protein: 0,
                carbs: 0,
                fats: 0,
            },
            errorMessage: '',
            id: '',
            userId: '',
        };
    },
    created() {
        const item = this.$route.query.item
        const parsedItem = JSON.parse(item)
        this.meal.mealName = parsedItem.mealName
        this.meal.mealDate = parsedItem.mealDate
        this.meal.foodItems = parsedItem.foodItems
        this.meal.calories = parsedItem.calories
        this.meal.protein = parsedItem.protein
        this.meal.carbs = parsedItem.carbs
        this.meal.fats = parsedItem.fats
        this.id = parsedItem._id
        this.userId = parsedItem.user_id
    },
    methods: {
        scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth' // Smooth scrolling
            })
        },
        async saveMeal() {
            try {
                let data = {
                    _id: this.id,
                    user_id: this.userId,
                    ...this.meal,
                };

                const response = await axios.post('http://127.0.0.1:5000/update_meal', data);
                console.log('Meal updated:', response.data)
                this.$router.push('/');
            } catch (error) {
                console.error('There was an error updating the meal!', error);
                this.errorMessage = 'There was an error updating the meal!'
                this.scrollToTop()
            }
        },
        async deleteMeal() {
            try {
                let data = {
                    _id: this.id,
                    user_id: this.userId,
                    ...this.meal,
                };
              const response = await axios.post('http://127.0.0.1:5000/delete_meal', data)
              console.log('Meal deleted:', response.data)
              this.$router.push('/')
            } catch (error) {
              console.error('There was an error deleting the meal!', error)
              this.errorMessage = 'There was an error deleting the meal!'
              this.scrollToTop()
            }
        }
    }
};
</script>