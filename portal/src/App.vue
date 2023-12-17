<template>
    <nav class="d-flex justify-content-between mb-5">
      <img id="logo" src="/logo.jpg" class="w-25">
      <div class="d-flex w-50 m-auto justify-content-around align-items-center">
        <router-link to="/">Home</router-link>
        <router-link v-if="isLoggedIn" to="/search-solicitudes">Ver mis solicitudes</router-link>
        <!-- <router-link to="/search-solicitudes">Ver mis solicitudes</router-link> -->
        <router-link to="/charts">Estadísticas</router-link>
        <router-link v-if="!isLoggedIn" class="btn btn-outline-primary" to="/login">Login</router-link>
        <LogoutComp v-if="isLoggedIn" @click="logout" class="btn btn-outline-primary"/>
      </div>
    </nav> 
    <main id="main-content">
      <router-view />
    </main>  
    <footer>
      120 nº3080 | Teléfono: 221 200 4222 | Correo: soporte@gmail.com
    </footer>

</template>

<script>
import LogoutComp from '@/components/LogoutComp.vue';
import { mapGetters, mapActions } from 'vuex';

export default {
  components: {
    LogoutComp,
  },
  data() {
    return {
      token: '',
    };
  },

  computed: {
    ...mapGetters(['isLoggedIn', 'idFromToken']),   
  },
  methods: {
    ...mapActions(['loginUser', 'logoutUser']),
    login() {
      // Dispatch the loginUser action from Vuex store
      this.loginUser();
    },
    logout() {
      // Dispatch the logoutUser action from Vuex store
      this.logoutUser();
    },
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
