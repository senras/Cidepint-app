<script>
export default {
  name: "SolicitudesDataTable",
  props: {
    solicitudes: {
      type: Array,
      required: true,
    },
  },
};
</script>

<template>
  <div class="d-flex flex-column w-50 m-auto">
    <div class="card">
      <div class="card-body">
        <div class="table-responsive">
          <table class="table table-hover">
            <thead>
              <tr class="align-middle">
                <th>Nombre</th>
                <th>Fecha inicio</th>
                <th>Estado de solicitud</th>
                <th>Notas</th>
              </tr>
            </thead>
            <tbody>
              <tr
                class="align-middle"
                v-for="solicitud in solicitudes"
                :key="solicitud.id"
              >
                <td>{{ solicitud.title }}</td>
                <td>{{ solicitud.creation_date }}</td>
                <td>{{ solicitud.status }}</td>
                <td>
                  <router-link
                    :to="{
                      name: 'SolicitudDetalle',
                      params: { id: solicitud.id },
                    }"
                    >Ver notas</router-link
                  >
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>
