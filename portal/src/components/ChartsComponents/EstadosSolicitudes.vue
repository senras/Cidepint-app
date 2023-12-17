<template>
  <div class="d-flex flex-column">
    <h1>Estado de solicitudes</h1>
    <div>
      <Doughnut :data="data" :options="options" />
    </div>
  </div>
</template>

<script>
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Doughnut } from "vue-chartjs";
import * as chartConfig from "./chartConfig.js";

ChartJS.register(ArcElement, Tooltip, Legend);

export default {
  name: "App",
  components: {
    Doughnut,
  },
  data() {
    return chartConfig;
  },
};
</script>
