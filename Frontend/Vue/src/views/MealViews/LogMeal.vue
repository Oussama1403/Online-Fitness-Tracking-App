<template>
    <MealForm :mode="'Log'" :meal="meal" :errorMessage="errorMessage" @submit="saveMeal"
    />
</template>

<script>
import MealForm from '@/components/MealForm.vue';
import axios from 'axios';
import { v4 as uuidv4 } from 'uuid'
import { jwtDecode } from 'jwt-decode'

export default {
    name: 'LogMeal',
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
            errorMessage: ''
        };
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
                const token = localStorage.getItem('authToken');
                const decoded = jwtDecode(token);
                const userId = decoded.user_id;

                let data = {
                    _id: uuidv4(),
                    user_id: userId,
                    ...this.meal,
                };

                const response = await axios.post('http://127.0.0.1:5000/log_meal', data);
                console.log('Meal logged:', response.data)
                this.$router.push('/'); // Redirect to meals dashboard
            } catch (error) {
                console.error('There was an error logging the meal!', error);
                this.errorMessage = 'There was an error logging the meal!'
                this.scrollToTop()
            }
        },
    },
};
</script>