<template>
    <div class="login">
      <h1 class="title">Inicie sesión</h1>
      <form class="form" @submit.prevent="login_main">
        <label class="form-label" for="#email">Email:</label>
        <input
          v-model="email"
          class="form-input"
          type="email"
          id="email"
          required
          placeholder="Email"
        />
        <label class="form-label" for="#password">Password:</label>
        <input
          v-model="password"
          class="form-input"
          type="password"
          id="password"
          placeholder="Password"
          autocomplete="on"
        />
        <p v-if="error" class="error">
          Has introducido mal el email o la contraseña.
        </p>
        
        <button type="submit" class="form-submit">Login</button>
        <button class="btn bg-white border border-radius mt-3"> 
          <a class="google-btn" href="#">Iniciar Sesión  <i class="bi bi-google"></i></a>
      </button>
      </form>
    </div>
  </template>
  
  <script>
  import { mapGetters, mapActions } from 'vuex';


      export default {
          data() {
          return {
            email: '', // Agrega estas líneas para definir las variables
            password: '',
            error: false,
          };
          },
          computed: {
    ...mapGetters(['isLoggedIn']),
  },
        methods: {
          ...mapActions(['loginUser', 'logoutUser']),
          login() {
            // Dispatch the loginUser action from Vuex store
            this.loginUser();
          },
          async login_main() {
            // console.log(this.email);
            // console.log(this.password);
                    try {
                const response = await this.$axios.post('/login', { email: this.email, password: this.password });
                // Verifica el código de estado de la respuesta
                if (response.status === 200) {
                  const token = response.data.access_token;
                  // Almacena el token en el Local Storage
                  localStorage.setItem('token', token);
                  console.log('Esto esta en localstorage:');
                  console.log(localStorage.getItem('token'));
                  this.login();
                  // Redirige al usuario al componente Home
                  this.$router.push({ name: 'home' });
                } else {
                  // Maneja otros códigos de estado según tus necesidades
                  console.log(response)
                  console.error('Error al iniciar sesión. Código de estado:', response.status);
                  this.error = true;
                }
                
              } catch (error) {
                console.error('Error al iniciar sesión:', error);
                this.error = true;
              }
          },
        },
      };
  </script>
  
  <style lang="scss" scoped>
  .login {
    padding: 2rem;
  }
  .title {
    text-align: center;
  }
  .form {
    margin: 3rem auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 20%;
    min-width: 350px;
    max-width: 100%;
    background: rgba(19, 35, 47, 0.9);
    border-radius: 5px;
    padding: 40px;
    box-shadow: 0 4px 10px 4px rgba(0, 0, 0, 0.3);
  }
  .form-label {
    margin-top: 2rem;
    color: white;
    margin-bottom: 0.5rem;
    &:first-of-type {
      margin-top: 0rem;
    }
  }
  .form-input {
    padding: 10px 15px;
    background: none;
    background-image: none;
    border: 1px solid white;
    color: white;
    &:focus {
      outline: 0;
      border-color: #1ab188;
    }
  }
  .form-submit {
    background: #1ab188;
    border: none;
    color: white;
    margin-top: 3rem;
    padding: 1rem 0;
    cursor: pointer;
    transition: background 0.2s;
    &:hover {
      background: #0b9185;
    }
  }
  .error {
    margin: 1rem 0 0;
    color: #ff4a96;
  }
  .msg {
    margin-top: 3rem;
    text-align: center;
  }
  </style>