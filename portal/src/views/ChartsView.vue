<script>
import EstadosSolicitudes from "../components/ChartsComponents/EstadosSolicitudes.vue";
import TopInstituciones from "../components/ChartsComponents/TopInstituciones.vue";
import TopServicios from "../components/ChartsComponents/TopServicios.vue";

export default {
  name: "ChartsView",
  components: {
    EstadosSolicitudes,
    TopInstituciones,
    TopServicios,
  },
};
</script>

<template>
  <div class="ChartsView">
    <div class="d-flex justify-content-around mt-5 px-1">
      <TopServicios />
      <EstadosSolicitudes />
      <TopInstituciones />
    </div>
  </div>
</template>
