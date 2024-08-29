<template>
    <div class="auth-page">
      <div class="auth-container">
        <div class="auth-pic js-tilt" data-tilt>
          <img :src="resolvedImageSrc" :alt="imageAlt" />
        </div>
  
        <Form @submit="onSubmit" v-slot="{ errors }" class="auth-form">
          <span class="auth-form-title">{{ title }}</span>
  
          <div v-if="errorMessage" class="alert" role="alert">
            {{ errorMessage }}
          </div>
  
          <div v-for="(field, index) in fields" :key="index" class="form-field">
            <Field
              :type="field.type"
              :name="field.name"
              v-model="form[field.name]"
              class="input form-control"
              :placeholder="field.placeholder"
              :rules="field.rules"
            />
            <ErrorMessage class="alert-validate" :name="field.name" />
          </div>
  
          <div class="auth-form-btn-container">
            <button type="submit" class="auth-form-btn">
              <span>
                {{ buttonText }}
                <i class="fa fa-long-arrow-right" aria-hidden="true"></i>
              </span>
            </button>
          </div>
  
          <div class="auth-link-section text-center">
            <span class="link-section-text">{{ linkText }}</span
            ><br />
            <router-link :to="linkUrl" class="link-section-link" aria-current="page">
              {{ linkActionText }}
            </router-link>
          </div>
        </Form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      title: String,
      imageSrc: String,
      imageAlt: String,
      fields: Array,
      buttonText: String,
      linkText: String,
      linkActionText: String,
      linkUrl: String,
      handleSubmit: Function,
      errorMessage: String
    },
    data() {
      return {
        form: {}
      }
    },
  
    computed: {
      resolvedImageSrc() {
        return new URL(this.imageSrc, import.meta.url).href
      }
    },
    methods: {
      onSubmit() {
        this.handleSubmit(this.form)
      }
    }
  }
  </script>
  
  <style scoped>
  input::placeholder,
  textarea::placeholder {
    color: #999;
  }
  
  /*--------------------------------------------- */
  
  .auth-page {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    width: 100%;
    font-family: 'Montserrat', sans-serif;
    background: #00ff99;
    background: -webkit-linear-gradient(left, #00ff55, #00ff99);
    background: -o-linear-gradient(left, #00ff55, #00ff99);
    background: -moz-linear-gradient(left, #00ff55, #00ff99);
    background: linear-gradient(left, #00ff55, #00ff99);
  }
  
  @-webkit-keyframes Gradient {
    0% {
      background-position: 0% 50%;
    }
  
    50% {
      background-position: 100% 50%;
    }
  
    100% {
      background-position: 0% 50%;
    }
  }
  
  @-moz-keyframes Gradient {
    0% {
      background-position: 0% 50%;
    }
  
    50% {
      background-position: 100% 50%;
    }
  
    100% {
      background-position: 0% 50%;
    }
  }
  
  @keyframes Gradient {
    0% {
      background-position: 0% 50%;
    }
  
    50% {
      background-position: 100% 50%;
    }
  
    100% {
      background-position: 0% 50%;
    }
  }
  
  .auth-container {
    width: 1163px;
    background: #fff;
    border-radius: 10px;
    overflow: hidden;
    background: #fff;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: center;
    padding: 90px 130px 88px 148px;
  }
  
  .auth-pic {
    width: 296px;
  }
  
  .auth-pic img {
    max-width: 100%;
  }
  
  .auth-form {
    width: 390px;
  }
  
  .auth-form-title {
    display: block;
    font-family: 'Montserrat', sans-serif;
    font-size: 24px;
    color: #333333;
    line-height: 1.2;
    text-align: center;
    padding-bottom: 44px;
  }
  
  /* input fields */
  
  .input {
    outline: none;
    border: 1px solid #00ff99;
    height: 50px;
    border-radius: 25px;
    padding: 0 30px;
    display: block;
    width: 100%;
    background: #efecec;
    font-family: 'Montserrat', sans-serif;
    font-size: 15px;
    line-height: 1.5;
    color: #666666;
  }
  
.input:hover {
  border: 3px solid #00ff99;
}
.input:focus {
  box-shadow: none;
  border: 3px solid #00ff99;
}

  /*---------------------------------------------*/
  
  .form-field {
    position: relative;
    width: 100%;
    z-index: 1;
    margin-bottom: 20px;
  }
  
  /* button */
button {
	outline: none !important;
	border: none;
	background: transparent;
}

button:hover {
	cursor: pointer;
}   
  
  .auth-form-btn-container {
    display: -webkit-box;
    display: -webkit-flex;
    display: -moz-box;
    display: -ms-flexbox;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
  
  .auth-form-btn {
    min-width: 193px;
  height: 50px;
  border-radius: 25px;
  background: #57b846;
  font-family: 'Montserrat', sans-serif;
  font-size: 15px;
  line-height: 1.5;
  color: #fff;
  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 25px;
  
    -webkit-transition: all 0.4s;
    -o-transition: all 0.4s;
    -moz-transition: all 0.4s;
    transition: all 0.4s;
  }
  
  .auth-form-btn i {
    margin-left: 7px;
    -webkit-transition: all 0.4s;
    -o-transition: all 0.4s;
    -moz-transition: all 0.4s;
    transition: all 0.4s;
  }
  
  .auth-form-btn:hover i {
    -webkit-transform: translateX(10px);
    -moz-transform: translateX(10px);
    -ms-transform: translateX(10px);
    -o-transform: translateX(10px);
    transform: translateX(10px);
  }
  
  /*------------------------------------------------------------------
    [ Responsive ]*/
  
  @media (max-width: 1200px) {
    .auth-pic {
      width: 33.5%;
    }
  
    .auth-form {
      width: 44%;
    }
  }
  
  @media (max-width: 992px) {
    .auth-container {
      padding: 90px 80px 88px 90px;
    }
  
    .auth-pic {
      width: 35%;
    }
  
    .auth-form {
      width: 55%;
    }
  }
  
  @media (max-width: 768px) {
    .auth-container {
      padding: 90px 80px 88px 80px;
    }
  
    .auth-pic {
      display: none;
    }
  
    .auth-form {
      width: 100%;
    }
  }
  
  @media (max-width: 576px) {
    .auth-container {
      padding: 90px 15px 88px 15px;
    }
  }
  
  /*------------------------------------------------------------------
    [ Alerts ]*/
  
  .alert {
    background-color: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
    padding: 10px;
    border-radius: 25px;
    margin-bottom: 20px;
    text-align: center;
    font-family: 'Montserrat', sans-serif;
  }
  
  .validate-input {
    position: relative;
  }
  
  .alert-validate {
    content: '\f06a';
    font-family: 'Montserrat', sans-serif;
    display: block;
    position: absolute;
    color: #c80000;
    font-size: 0.7em;
    font-weight: bold;
    top: 50%;
    -webkit-transform: translateY(-50%);
    -moz-transform: translateY(-50%);
    -ms-transform: translateY(-50%);
    -o-transform: translateY(-50%);
    transform: translateY(-50%);
    right: 13px;
  }
  
  @media (max-width: 992px) {
    .alert-validate::before {
      visibility: visible;
      opacity: 1;
    }
  }
  
  /* Link section styles */
  
  .auth-link-section {
    margin: 1em;
    font-size: 1.1em;
  }
  
  .link-section-text {
    color: #333333;
    font-family: 'Montserrat', sans-serif;
  }
  
  .link-section-link {
    font-family: 'Montserrat', sans-serif;
    line-height: 1.7;
    margin: 0px;
    font-weight: 700;
    transition: all 0.4s;
    -webkit-transition: all 0.4s;
    -o-transition: all 0.4s;
    -moz-transition: all 0.4s;
    background: linear-gradient(to right, #09ea05, #00eb85);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
    border-bottom: 1px solid #09ea05;
  }
  
  .link-section-link:focus {
    outline: none !important;
  }
  
  .link-section-link:hover {
    background: linear-gradient(to left, #09ea05, #00eb85);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
  }
  </style>
  