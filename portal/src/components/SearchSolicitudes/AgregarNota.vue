<template>
  <div class="d-flex flex-column w-50 m-auto">
    <div class="d-flex justify-content-between">
      <h3 class="mb-3 text-start">Agregar una nota</h3>
    </div>
    <form @submit.stop.prevent="postNota">
        <textarea class="form-control" v-model="nota" minlength="5" id="nota" name="" cols="30" rows="10" placeholder="Ingrese aquí un comentario para que vea el staff.."></textarea>
        <button id="btn-blue" class="btn w-100" type="submit">Comentar</button>
    </form>
  </div>
</template>



<script>
import axios from "axios";
import { mapGetters } from 'vuex';

export default {
  name: "AgregarNota",
  data() {
    return {
      nota: "",
      id_solicitud: this.$route.params.id_solicitud,
      id_user: this.$store.getters.idFromToken,

    };
  },
  computed: {
    ...mapGetters(['idFromToken']),
    },
  methods: {
    postNota() {
        let self = this;
        event.preventDefault();
       axios.post("https://admin-grupo06.proyecto2023.linti.unlp.edu.ar/api/me/requests/" + this.$route.params.id_solicitud + "/notes", {
     // axios.post("http://127.0.0.1:5000/api/me/requests/" + this.$route.params.id_solicitud + "/notes", {
        comentario: this.nota,
        // autor_id: 1,
        autor_id: this.id_user,
      }).then((response) => {
        console.log(response);
        const status = JSON.parse(response.status);
        if (status == '201') {
             self.$router.push("/solicitud-detalle/" + this.$route.params.id_solicitud );
        }
      }).catch((error) => {
        console.log(error);
      });
    },
  },
};
</script>


<style> 
textarea {
  width: 100%;
  height: 150px;
  padding: 12px 20px;
  box-sizing: border-box;
  border: 2px solid #ccc;
  border-radius: 4px;
  background-color: #f8f8f8;
  font-size: 16px;
  resize: none;
}
</style>