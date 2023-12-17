<template>
    <button @click="logout">Cerrar Sesión</button>
</template>
  
 <script>
import axios from '@/plugins/axios';

export default {
  methods: {
    logout() {
      const token = localStorage.getItem('token');  
      //axios.get('http://127.0.0.1:5000/api/auth/logout_jwt', {
      axios.get('https://admin-grupo06.proyecto2023.linti.unlp.edu.ar/api/auth/logout_jwt', {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      })
        .then(() => {
          // Limpiar el token almacenado localmente o en cookies si es necesario
          localStorage.removeItem('token');
          // Actualizar el estado de autenticación localmente en el componente
          this.$emit('logout'); // Emitir un evento para notificar a los componentes padres sobre el logout
          this.$router.push('/login');
        })
        .catch(error => {
          console.error('Error al cerrar sesión:', error);
        });
    }
  }
};
</script>