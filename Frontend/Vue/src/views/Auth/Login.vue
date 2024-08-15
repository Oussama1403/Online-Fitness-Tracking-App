<template>
    
	<div class="contact1">
		<div class="container-contact1">
			<div class="contact1-pic js-tilt" data-tilt>
				<img src='@/assets/images/login.png' alt="IMG">
			</div>

			<Form @submit="login" v-slot="{ errors }" class="contact1-form ">
				<span class="contact1-form-title">
					Login
				</span>

				<div class="wrap-input1">
          <Field type="text" name="username" v-model="username" class="input form-control" placeholder="Username" rules="required" />
          <ErrorMessage class="alert-validate" name="username" />
				</div>

        <div class="wrap-input1">
          <Field type="text" name="Password" v-model="password" class="input form-control" placeholder="Password" rules="required" />
          <ErrorMessage class="alert-validate" name="Password" />
				</div>

				<div class="container-contact1-form-btn">
					<button type="submit" class="contact1-form-btn">
						<span>
							Log in
							<i class="fa fa-long-arrow-right" aria-hidden="true"></i>
						</span>
					</button>
				</div>

        <div class="link-section text-center">
          <span class="text-link">Not an User ?</span>
          <br>
          <router-link to="/register" class="link" aria-current="page">
           Sign Up
          </router-link>
        </div>
        
			</form>
		</div>
	</div>
</template>
  
<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    login() {
      axios.post('http://127.0.0.1:5000/login', {
        username: this.username,
        password: this.password,
      })
      .then(response => {
        localStorage.setItem('authToken', response.data.access_token);
        console.log('Login successful:', response.data.access_token);
        this.$router.push('/'); ///protected
      })
      .catch(error => {
        console.error('Login error:', error);
        alert('Invalid username or password');
      });
    },
  },
};
</script>
  

<style scoped>

/*---------------------------------------------*/
.link-section {
  margin: 1em;
  font-size: 1.1em;
}
/* change ro router-link later */
.link {
	font-family: 'Montserrat', sans-serif;
	line-height: 1.7;
	color: #666666;
	margin: 0px;
	transition: all 0.4s;
	-webkit-transition: all 0.4s;
  -o-transition: all 0.4s;
  -moz-transition: all 0.4s;
  color: #57b846;
}

.link:focus {
	outline: none !important;
}

.link:hover {
	text-decoration: none;
  color: #333333;
}

/*---------------------------------------------*/
h1,h2,h3,h4,h5,h6 {
	margin: 0px;
}

p {
	font-family: 'Montserrat', sans-serif;
	font-size: 14px;
	line-height: 1.7;
	color: #666666;
	margin: 0px;
}

ul, li {
	margin: 0px;
	list-style-type: none;
}


/*---------------------------------------------*/
	
input::-webkit-input-placeholder { color: #999999; }
input:-moz-placeholder { color: #999999; }
input::-moz-placeholder { color: #999999; }
input:-ms-input-placeholder { color: #999999; }

textarea::-webkit-input-placeholder { color: #999999; }
textarea:-moz-placeholder { color: #999999; }
textarea::-moz-placeholder { color: #999999; }
textarea:-ms-input-placeholder { color: #999999; }

/*---------------------------------------------*/
button {
	outline: none !important;
	border: none;
	background: transparent;
}

button:hover {
	cursor: pointer;
}


/*//////////////////////////////////////////////////////////////////
[ Contact 1 ]*/

.contact1 {
  min-height: 100vh;
  padding: 15px;

  background: #00ff99;
  background: -webkit-linear-gradient(left, #00ff55, #00ff99);
  background: -o-linear-gradient(left, #00ff55, #00ff99);
  background: -moz-linear-gradient(left, #00ff55, #00ff99);
  background: linear-gradient(left, #00ff55, #00ff99);

  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
}

.container-contact1 {
  width: 1163px;
  background: #fff;
  border-radius: 10px;
  overflow: hidden;

  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;

  padding: 90px 130px 88px 148px;
}

/*------------------------------------------------------------------
[  ]*/
  
.contact1-pic {
  width: 296px;
}

.contact1-pic img {
  max-width: 100%;
}


/*------------------------------------------------------------------
[  ]*/
.contact1-form {
  width: 390px;
}

.contact1-form-title {
  display: block;
  font-family: 'Montserrat', sans-serif;
  font-size: 24px;
  color: #333333;
  line-height: 1.2;
  text-align: center;
  padding-bottom: 44px;
}

.input {
  outline: none;
	border: none;
  height: 50px;
  border-radius: 25px;
  padding: 0 30px;
  display: block;
  width: 100%;
  background: #e6e6e6;
  font-family:'Montserrat', sans-serif;
  font-size: 15px;
  line-height: 1.5;
  color: #666666;
  transition: all 0.3s ease-in-out;

}
.input:hover {
  border: 1px solid #00ff99;
}
.input:focus {
  box-shadow: 0 0 0 0.2rem #00ff99;
}

/*---------------------------------------------*/
.wrap-input1 {
  position: relative;
  width: 100%;
  z-index: 1;
  margin-bottom: 20px;
}


/*---------------------------------------------*/
.container-contact1-form-btn {
  display: -webkit-box;
  display: -webkit-flex;
  display: -moz-box;
  display: -ms-flexbox;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.contact1-form-btn {
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

.contact1-form-btn i {
  margin-left: 7px;

  -webkit-transition: all 0.4s;
  -o-transition: all 0.4s;
  -moz-transition: all 0.4s;
  transition: all 0.4s;
}

.contact1-form-btn:hover {
  background: #333333;
}

.contact1-form-btn:hover i {
  -webkit-transform: translateX(10px);
  -moz-transform: translateX(10px);
  -ms-transform: translateX(10px);
  -o-transform: translateX(10px);
  transform: translateX(10px);
}




/*------------------------------------------------------------------
[ Responsive ]*/

@media (max-width: 1200px) {
  .contact1-pic {
    width: 33.5%;
  }

  .contact1-form {
    width: 44%;
  }
}

@media (max-width: 992px) {
  .container-contact1 {
    padding: 90px 80px 88px 90px;
  }

  .contact1-pic {
    width: 35%;
  }

  .contact1-form {
    width: 55%;
  }
}

@media (max-width: 768px) {
  .container-contact1 {
    padding: 90px 80px 88px 80px;
  }

  .contact1-pic {
    display: none;
  }

  .contact1-form {
    width: 100%;
  }
}

@media (max-width: 576px) {
  .container-contact1 {
    padding: 90px 15px 88px 15px;
  }
}


/*------------------------------------------------------------------
[ Alert validate ]*/

.validate-input {
  position: relative;
}
/*
.alert-validate::before {
  content: attr(data-validate);
  position: absolute;
  max-width: 70%;
  background-color: white;
  border: 1px solid #c80000;
  border-radius: 13px;
  padding: 4px 25px 4px 10px;
  top: 50%;
  -webkit-transform: translateY(-50%);
  -moz-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  -o-transform: translateY(-50%);
  transform: translateY(-50%);
  right: 8px;
  pointer-events: none;

  font-family: 'Montserrat', sans-serif;
  color: #c80000;
  font-size: 13px;
  line-height: 1.4;
  text-align: left;

  visibility: hidden;
  opacity: 0;

  -webkit-transition: opacity 0.4s;
  -o-transition: opacity 0.4s;
  -moz-transition: opacity 0.4s;
  transition: opacity 0.4s;
}
*/

.alert-validate {
  content: "\f06a";
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
</style>
  