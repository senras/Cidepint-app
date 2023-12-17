<template>
  <l-map :center="mapCenter" :zoom="mapZoom" style="height: 300px" @click="handleMapClick" ref="mapObject">
    <l-tile-layer :url="tileLayerUrl"></l-tile-layer>

    <!-- Icono para la posición actual del usuario -->
    <l-marker v-if="userLocation" :lat-lng="userLocation" :icon="userIcon" @click="showUserLocationPopup"></l-marker>

    <!-- Icono para la posición del destino -->
    <l-marker v-if="destinationLatLng" :lat-lng="destinationLatLng" :icon="destinationIcon" @click="showDestinationInfo">
      <l-popup v-if="destinationAddress">
        <div>
          <strong>Dirección:</strong> {{ destinationAddress }}
        </div>
      </l-popup>
    </l-marker>
  </l-map>
</template>

<script>
import { LMap, LTileLayer, LMarker, LPopup } from 'vue3-leaflet';
import 'leaflet/dist/leaflet.css';

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
  },

  props: {
    destinationLatLng: {
      type: Array,
      required: true,
    },

    destinationAddress: {
    type: String, 
    default: '',
    },
  },

  data() {
    return {
      mapCenter: this.destinationLatLng, // Ajustado para centrar en la ubicación del destino
      mapZoom: 16,
      tileLayerUrl: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      userLocation: null,
      userIcon: null,
      destinationIcon: null,
      userPopupContent: 'ESTOY AQUI!',
    };
  },

  methods: {
    // Método para crear un icono personalizado
    createCustomIcon(iconUrl) {
      return L.icon({
        iconUrl: iconUrl,
        iconSize: [32, 32],
        iconAnchor: [16, 32],
        popupAnchor: [0, -32],
      });
    },


    // Método para obtener la ubicación del usuario mediante geolocalización
    getUserLocation() {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          this.userLocation = [position.coords.latitude, position.coords.longitude];
          this.mapCenter = this.userLocation;
          this.$refs.mapObject.setView(this.userLocation, this.mapZoom);
          this.$emit('userLocation', this.userLocation);
        },
        (error) => {
          console.error('Error obteniendo la ubicación del usuario:', error);
        }
      );
    },

     handleMapClick(event) {
      const { lat, lng } = event.latlng;
      console.log('Clic en el mapa en la ubicación:', lat, lng);
    }, 


  // #### Muestra informacion traida de la api con datos del destino
  showDestinationInfo() {
  if (this.$refs.mapObject && this.$refs.mapObject._map && this.destinationAddress) {
    this.$refs.mapObject.setView(this.destinationLatLng, this.mapZoom);
    this.$refs.mapObject.openPopup(this.destinationAddress, this.destinationLatLng);
  } else {
    console.error('El mapa no está disponible o la dirección de destino no está definida.');
  }
},

  // #### Muestra informacion DE LA UBICACION DEL USUARIO
 showUserLocationPopup() {
    if (this.$refs.mapObject && this.$refs.mapObject._map) {
      this.$refs.mapObject.setView(this.userLocation, this.mapZoom); // Centra el mapa en la ubicación del usuario al hacer clic
      this.$refs.mapObject.openPopup(this.userPopupContent, this.userLocation);
    } else {
      console.error('El mapa no está disponible todavía.');
    } 
  },

  }, 

  mounted() {
    this.userIcon = this.createCustomIcon('/icons/ubicacionDea.ico');
    this.destinationIcon = this.createCustomIcon('/icons/ubicacionDestino.ico');
    this.getUserLocation();
  },
  
};
</script>
