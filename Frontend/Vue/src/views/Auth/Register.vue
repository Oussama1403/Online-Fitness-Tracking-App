<template>
  <AuthForm
    title="Sign Up"
    imageSrc="../assets/images/register.png"
    imageAlt="Register Image"
    :fields="signupFields"
    buttonText="Sign Up"
    linkText="Already have an account?"
    linkActionText="Log In"
    linkUrl="/login"
    :handleSubmit="register"
    :errorMessage="errorMessage"
  />
</template>

<script>
import AuthForm from '@/components/AuthForm.vue'
import axios from 'axios'

export default {
  components: {
    AuthForm
  },
  data() {
    return {
      errorMessage: '' // State to hold the error message
    }
  },
  computed: {
    signupFields() {
      return [
        {
          type: 'text',
          name: 'username',
          placeholder: 'Username',
          rules: 'required'
        },
        {
          type: 'email',
          name: 'email',
          placeholder: 'Email',
          rules: 'required|email'
        },
        {
          type: 'password',
          name: 'password',
          placeholder: 'Password',
          rules: 'required'
        },
        {
          type: 'password',
          name: 'confirmPassword',
          placeholder: 'Confirm Password',
          rules: 'required|sameAs:@password'
        }
      ]
    }
  },
  methods: {
    register(formData) {
      this.errorMessage = '' // Reset error message before each request
      axios
        .post('http://127.0.0.1:5000/register', {
          username: formData.username,
          email: formData.email,
          password: formData.password,
          confirmPassword: formData.confirmPassword
        })
        .then(() => {
          this.$router.push('/login')
        })
        .catch((error) => {
          console.error('Registration error:', error)
          if (error.response.data.message === 'User already exists') {
            this.errorMessage = 'User already exists'
          } else if (error.response.data.message === 'Username, email or password are required') {
            this.errorMessage = 'Username, email or password are required'
          } else {
            this.errorMessage = 'An error occurred during registration, please report to the admin'
          }
        })
    }
  }
}
</script>
