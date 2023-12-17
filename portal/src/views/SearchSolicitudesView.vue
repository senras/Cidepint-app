<template>
  <div class="d-flex flex-column w-50 m-auto">
    <h1 class="my-3">Mis solicitudes</h1>
    <!-- Formulario de búsqueda -->
    <form
      class="d-flex justify-content-between m-auto my-3"
      @submit.prevent="getSolicitudes"
    > 
      <div class="d-flex justify-content-around">   
        <div class="input-group">
          <span class="input-group-text" id="basic-addon1">Estado</span>
          <select class="form-select form-control" v-model="estado" id="select-estado">
            <option v-for="estado in estados" :key="estado" :value="estado">
              {{ estado }}
            </option>
          </select>
        </div>
        <div class="input-group">
          <span class="input-group-text" id="basic-addon2">Orden</span>
          <select class="form-select form-control" v-model="order" id="select-orden">
            <option v-for="order in orders" :key="order" :value="order">
              {{ order }}
            </option>
          </select>
        </div>
        <div class="input-group">
          <span class="input-group-text" id="basic-addon3">Criterio</span>
          <select class="form-select" v-model="sort" id="select-criterio">
            <option v-for="sort in sorts" :key="sort" :value="sort">
              {{ sort }}
            </option>
          </select>
        </div>
        <div class="input-group">
          <span class="input-group-text" id="basic-addon4">Fecha</span>
          <input class="form-control" type="date" v-model="fecha" id="fecha" />
        </div>
    </div>
      <button class="btn btn-primary">Filtrar</button>
    </form>
  </div>
  <SolicitudesDataTable :solicitudes="solicitudes" />
</template>

<script>
import SolicitudesDataTable from "../components/SearchSolicitudes/SolicitudesDataTable.vue";
import axios from "axios";
import { mapGetters } from 'vuex';

export default {
  name: "SearchSolicitudes",
  components: {
    SolicitudesDataTable,
  },
  computed: {
    ...mapGetters(['idFromToken']),
    },
  data() {
    return {
      sort: "",
      order: "",
      estado: "",
      fecha: "",
      user_id: this.$store.getters.idFromToken,
      solicitudes: [],
      estados: [
        ("Aceptada", "Aceptada"),
        ("Rechazada", "Rechazada"),
        ("En_proceso", "En proceso"),
        ("Finalizada", "Finalizada"),
        ("Cancelada", "Cancelada"),
        ("Todas", "Todas"),
      ],
      sorts: [("fecha", "fecha"), ("estado", "estado")],
      orders: [("ascendente", "ascendente"), ("descendente", "descendente")],
    };
  },
  mounted() {
    this.setupSolicitudes();
  },
  methods: {
    getSolicitudes() {
      axios
           .get("https://admin-grupo06.proyecto2023.linti.unlp.edu.ar/api/me/requests", {
          //.get("http://127.0.0.1:5000/api/me/requests", {
          params: {
            estado: this.estado,
            sort: this.sort,
            order: this.order,
            fecha: this.fecha,
            user_id: this.user_id,
          },
        })
        .then((response) => {
          console.log(response.data);
          console.log("Estado de solicitud: ", this.estado);
          console.log("Criterio de orden: ",this.sort);
          console.log("Orden (asc/desc): ",this.order);
          console.log("Fecha: ",this.fecha);
          console.log("Id de usuario: ",this.idFromToken);
          this.solicitudes = response.data.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    setupSolicitudes() {
      axios
        .get("https://admin-grupo06.proyecto2023.linti.unlp.edu.ar/api/me/requests",{ 
        //.get("http://127.0.0.1:5000/api/me/requests",{
          params: {
            user_id: this.user_id,
          },
        })
        .then((response) => {
          console.log(response.data);
          this.solicitudes = response.data.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
