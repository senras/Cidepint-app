<template>
  <div class="d-flex flex-column">
    <h1 class="mb-3">Top servicios más solicitados</h1>
    <div class="card border border-primary">
      <div class="card-body">
        <div class="table-responsive">
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Servicio</th>
                <th scope="col">Cantidad de solicitudes</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="servicio in servicios" :key="servicio.id">
                <td>{{ servicio.nombre }}</td>
                <td>{{ servicio.cantidad_solicitudes }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "TopServicios",
  data() {
    return {
      servicios: [],
    };
  },

  mounted() {
    this.getServicios();
  },
  methods: {
    getServicios() {
    axios
         .get("https://admin-grupo06.proyecto2023.linti.unlp.edu.ar/api/charts/servicios_mas_solicitados")
       // .get("http://127.0.0.1:5000/api/charts/servicios_mas_solicitados")
        .then((response) => {
          this.servicios = response.data.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
