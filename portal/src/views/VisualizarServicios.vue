<template>
  <div class="container">
    <!-- Título del Servicio -->
    <h1>{{ servicio.name }}</h1>

    <div class="row">
      <!-- #### Columna izquierda -->
      <div class="col-md-6">
        <!-- Sección Detalle -->
        <div>
          <h2>Detalle</h2>
          <p>{{ servicio.description }}</p>
        </div>

        <!-- Sección Institución -->
        <div>
          <h2>{{ servicio.nameInstitucion }}</h2>
          <p>{{ servicio.infoInstitucion }}</p>
        </div>
      </div>

      <!-- #### Columna derecha -->
      <div class="col-md-6">
        <!-- Botón Solicitar -->
        <button @click="solicitarServicio" class="btn btn-primary">
          Solicitar
        </button>

        <!-- Recuadro "¿Cómo llegar?" -->
        <div class="map-container">
          <h2>¿Cómo llegar?</h2>
          <!-- Aca se integrará el componente del mapa -->
          <!-- Verifica que la latitud y longitud estén disponibles antes de renderizar el mapa -->
          <MapComponent
            v-if="servicio.latitud && servicio.longitud"
            :destinationLatLng="[servicio.latitud, servicio.longitud]"
            :destinationAddress="servicio.address" 
            @userLocation="updateUserLocation"
          />
          <div v-else>
            Cargando mapa...
          </div>
        </div>

        <!-- Alert para mostrar solicitud creada -->
        <div
          v-if="solicitudCreada"
          class="alert alert-success alert-dismissible fade show"
          role="alert"
        >
          La solicitud fue creada exitasamente!!
          <button
            type="button"
            class="close"
            @click="cerrarAlert"
            aria-label="Close"
          >
            <span aria-hidden="true">&times;</span>
          </button>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
import MapComponent from '../components/MapComponent.vue';
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
  components: {
    MapComponent,
  },

  data() {
    return {
      servicio: {
        name: '',
        description: '',
        nameInstitucion: '',
        infoInstitucion: '',
        id_token: null,
        latitud: null,
        longitud: null,
      },
      userLocation: null,
      solicitudCreada: false, // flag para mostrar el mensaje de solicitud creada
    };
  },

  mounted() {
    // Realiza la llamada a la API al montar el componente
    this.fetchServicio();
  },


  computed: {
    ...mapGetters(['idFromToken']),   
  },

  methods: {
    solicitarServicio() {

      // Obtiene el ID del servicio del parámetro de ruta
      const id_serv = this.$route.params.id;
      this.id_token = this.$store.state.idFromToken;

      //  #### Si no esta logeado el usuario te manda al login
      if (this.id_token == null) {
        this.$router.push('/login');
        return;
      }

      const solicitudData = {
        user_id: this.id_token,
        servicio_id: id_serv,
      };

    // #### Realiza la llamada a la API para solicitar el servicio - llamar al endpoint create_solicitud() en solicitudes.py
     axios.post('https://admin-grupo06.proyecto2023.linti.unlp.edu.ar/api/me/requests/', solicitudData)
      //axios.post('http://localhost:5000/api/me/requests/', solicitudData)
        .then((response) => {
          // Mostrar el alert de éxito
          this.solicitudCreada = true;
          console.log('Solicitud realizada con éxito:', response.data);
        })
        .catch((error) => {
          console.error('Error al solicitar el servicio:', error);
        });

    },


    updateUserLocation(location) {
      console.log('----> Ubicación del usuario actualizada:', location);
      this.userLocation = location;
    },


    fetchServicio() {
       // Obtiene el ID del servicio del parámetro de ruta
      const id = this.$route.params.id;

      // #### Realiza la llamada a la API para obtener los detalles del servicio con el id como parámetro
      //axios.get(`http://localhost:5000/api/services/${id}`)
      axios.get(`https://admin-grupo06.proyecto2023.linti.unlp.edu.ar/api/services/${id}`)
        .then((response) => {
          this.servicio = response.data;
          console.log('----> método fetchServicio : ', response.data);
        })
        .catch((error) => {
          console.error(' ----> Error fetching service info:', error);
        });
    },

    cerrarAlert() {
      this.solicitudCreada = false;
    },

  },
};
</script>

<style>
/* Estilos generales para el cuerpo de la aplicación */
body {
  font-family: 'Arial', sans-serif;
  background-color: #f8f9fa; /* Color de fondo general */
}

.container {
  margin-top: 20px; /* Espacio superior en el contenedor principal */
}

/* Estilos para las columnas */
.col-md-6 {
  margin-bottom: 20px;
}

/* Estilos para el botón de "Solicitar" */
.btn-primary {
  background-color: #007bff; /* Color primario de Bootstrap */
  border-color: #007bff;
}

.btn-primary:hover {
  background-color: #0056b3; /* Cambio de color al pasar el ratón */
  border-color: #0056b3;
}

/* Estilos para el recuadro del mapa */
.map-container {
  height: 450px;   /* Ajusta la altura según sea necesario */
  width: 90%;      /* Ajusta el ancho según sea necesario */
  margin: 0 auto;  /* Centra el contenedor horizontalmente */
  border: 2px solid #007bff; /* Borde del contenedor */
  border-radius: 10px;  /* Bordes redondeados */
  overflow: hidden; /* Evita que el contenido sobresalga del contenedor */
  margin-top: 20px; /* Espacio superior */
}

/* Estilos para el mensaje de alerta */
.alert {
  position: fixed;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 80%;
  max-width: 400px;
  z-index: 1000;
}

/* Estilos adicionales para hacer la alerta responsive */
@media (max-width: 576px) {
  .alert {
    width: 90%;
    max-width: 100%;
  }
}

</style>
