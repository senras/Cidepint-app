<template>
  <div class="d-flex flex-column">
    <h1 class="mb-3">Top instituciones</h1>
    <div class="card border border-primary">
      <div class="card-body">
        <div class="table-responsive">
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Institución</th>
                <th scope="col">Tiempo de resolución <i>(en horas)</i></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="institucion in instituciones" :key="institucion.id">
                <td>{{ institucion.nombre }}</td>
                <td>{{ institucion.promedio }}</td>
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
  name: "TopInstituciones",
  data() {
    return {
      instituciones: [],
    };
  },

  mounted() {
    this.getinstituciones();
  },
  methods: {
    getinstituciones() {
      axios
          .get(
             "https://admin-grupo06.proyecto2023.linti.unlp.edu.ar/api/charts/instituciones_mejor_tiempo_resolucion"
           )
/*           .get(
            "http://127.0.0.1:5000/api/charts/instituciones_mejor_tiempo_resolucion"
          ) */
          .then((response) => {
            this.instituciones = response.data.data;
          })
          .catch((error) => {
            console.log(error);
          });
      },
  },
};
</script>
