<script>
import axios from "axios";

export default {
  name: "SolicitudDetalle",
  data() {
    return {
      notas: [],
      id_solicitud: this.$route.params.id,
    };
  },
  mounted() {
    this.getNotas();
  },
  methods: {
    getNotas() {
    axios
     .get("https://admin-grupo06.proyecto2023.linti.unlp.edu.ar/api/me/requests/" + this.$route.params.id)
    //   .get("http://127.0.0.1:5000/api/me/requests/" + this.$route.params.id)
        .then((response) => {
          this.notas = response.data.data.notas;
          console.log(this.notas);
          console.log("The id is: " + this.$route.params.id);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<template>
  <div class="d-flex flex-column w-50 m-auto">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h1 class="text-start">Notas de solicitud</h1>
      <router-link  class="btn btn-primary"
                    :to="{
                      name: 'AgregarNota',
                      params: { id_solicitud: id_solicitud, 
                        id_user: 1 },
                    }"
                    >Agregar nota <i class="bi bi-plus-square-dotted text-white"></i></router-link
                  >
    </div>
    <div class="card mb-5">
      <div class="card-body">
        <div class="table-responsive">
          <table class="table table-hover">
            <thead>
              <tr class="align-middle">
                <th>Autor</th>
                <th>Fecha</th>
                <th>Nota</th>
              </tr>
            </thead>
            <tbody>
              <tr class="align-middle" v-for="nota in notas" :key="nota.id">
                <td>{{ nota.author }}</td>
                <td>{{ nota.date }}</td>
                <td>{{ nota.comment }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>
