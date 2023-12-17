import '@babel/polyfill'
import 'mutationobserver-shim'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { LMap, LTileLayer, LMarker } from 'vue3-leaflet';
import 'leaflet/dist/leaflet.css';
import { BootstrapVue } from 'bootstrap-vue-next'
import store from "./store";
import VueAxios from 'vue-axios';
import axiosInstance from '@/plugins/axios';

const app = createApp(App)

// boostrap
app.use(BootstrapVue);

// Registra los componentes de vue3-leaflet 
app.component('l-map', LMap);
app.component('l-tile-layer', LTileLayer);
app.component('l-marker', LMarker);

// Set up VueAxios with the custom axios instance
app.use(VueAxios, axiosInstance);


// Set the axios instance as a property on the app instance
app.config.globalProperties.$axios = axiosInstance;

app.use(store);

app.use(router).mount('#app')