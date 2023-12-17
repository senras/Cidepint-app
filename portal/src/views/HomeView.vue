<template>
  <BuscadorServicio/>
  <div>
    <h1 v-if="isAuthenticated">Hay una sesión iniciada!</h1>
    <h1 v-else>No hay sesión iniciada!</h1>
  </div>
</template>

<script>
import BuscadorServicio from '@/components/BuscadorServicio.vue';


export default {
  name: 'HomeView',
  components: {
    BuscadorServicio
  },
  computed: {
    isAuthenticated() {
      // Verificar si el usuario está autenticado basándose en la existencia del token
      return !!localStorage.getItem('token');
    },
  },
}
</script>
