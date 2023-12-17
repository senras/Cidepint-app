<template>
    <div class="card p-2 mb-4 mx-4">
      <h4 class="text-center">Buscador de servicios</h4>
      <form class="row gy-2 gx-3 align-items-center" @submit.prevent="buscarServicio">
        <div class="col-md-2">
          <label class="visually-hidden" for="autoSizingInput">Titulo</label>
          <input v-model="titulo" type="text" class="form-control" placeholder="Título">
        </div>
        <div class="col-md-2">
          <label class="visually-hidden" for="autoSizingInput">Descripcion</label>
          <input v-model="descripcion" type="text" class="form-control" placeholder="Descripción">
        </div>
        <div class="col-md-3">
          <label class="visually-hidden" for="autoSizingInput">Nombre de Institucion</label>
          <input v-model="institucion" type="text" class="form-control" placeholder="Nombre de institución">
        </div>
        <div class="col-md-2">
          <label class="visually-hidden" for="autoSizingInput">Tags</label>
          <input v-model="tags" type="text" class="form-control" placeholder="Tags">
        </div>
        <!-- Desplegable con la lista de servicios -->
        <div class="col-md-3">
          <label class="visually-hidden" for="autoSizingSelect">Tipo de Servicio</label>
          <select class="form-select" v-model="tipoServicio">
            <option value="">Seleccione tipo...</option>
            <option v-for="servicio in servicios" :key="servicio" :value="servicio">{{ servicio }}</option>
          </select>
        </div>
        <div class="col-12 text-center mt-3">
          <button type="submit" class="btn btn-primary">Buscar</button>
        </div>
      </form>
    </div>
    
    <div class="card p-2 mx-4" v-if="busquedaRealizada && resultadosBusqueda.length">
      <!-- Listado de resultados de la búsqueda -->
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">Nombre</th>
            <th scope="col">Descripción</th>
            <th scope="col">Laboratorio</th>
            <th scope="col">Palabras clave</th>
            <th scope="col">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="resultado in resultadosBusqueda" :key="resultado.name">
            <td>{{ resultado.name }}</td>
            <td>{{ resultado.description }}</td>
            <td>{{ resultado.laboratory }}</td>
            <td>{{ Array.isArray(resultado.keywords) ? resultado.keywords.join(', ') : resultado.keywords }}</td>
            <td>
              <button type="button" class="btn btn-primary" @click="navigateToPage(resultado)">Ver</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-if="busquedaRealizada && !resultadosBusqueda.length">
        <p class="text-center">No se encontraron resultados para tu búsqueda.</p>
    </div>

    <div class="text-center mt-2" v-if="busquedaRealizada && resultadosBusqueda.length">
      <button class="btn btn-success mx-2" @click="currentPage--; buscarServicio()" :disabled="currentPage === 1">Anterior</button>
      <button class="btn btn-success" @click="currentPage++; buscarServicio()" :disabled="currentPage === totalPages">Siguiente</button>
    </div>

</template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        titulo: '',
        descripcion: '',
        institucion: '',
        tags: '',
        tipoServicio: '',
        servicios: [],
        resultadosBusqueda: [],
        busquedaRealizada: false, // nueva variable
        currentPage: 1,
        totalPages: 0,
      };
    },
    created() {
      this.obtenerTiposDeServicios();
    },
    methods: {
      obtenerTiposDeServicios() {
       axios.get(`https://admin-grupo06.proyecto2023.linti.unlp.edu.ar/api/services/types`)
        //axios.get(`http://127.0.0.1:5000/api/services/types`)
          .then(response => {
            this.servicios = response.data.data;
          })
          .catch(error => {
            console.error(error);
          });
      },
      navigateToPage(resultado) {//eso es para enviar el id por parametro, hay que cambiar el name:
        this.$router.push({ name: "VisualizarServicios", params: { id: resultado.id } });
      },
      buscarServicio() {
        this.busquedaRealizada = true; // establecer en true cuando se realiza una búsqueda
        axios.get(`https://admin-grupo06.proyecto2023.linti.unlp.edu.ar/api/services/search`, {
        //axios.get(`http://127.0.0.1:5000/api/services/search`, {
          params: {
            q: this.titulo,
            type: this.tipoServicio,
            description: this.descripcion,
            laboratory: this.institucion,
            keywords: this.tags,
            page: this.currentPage,
            per_page: 1
          }
        })
        .then(response => {
          this.resultadosBusqueda = response.data.data;
          this.totalPages = Math.ceil(response.data.total / response.data.per_page);
        })
        .catch(error => {
          console.error(error);
        });
      },
    },
  };
  </script>