import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ChartsView from "../views/ChartsView.vue";
import SearchSolicitudesView from "../views/SearchSolicitudesView.vue";
import SolicitudDetalle from "../components/SearchSolicitudes/SolicitudDetalle.vue";
import AgregarNota from "../components/SearchSolicitudes/AgregarNota.vue";
import VisualizarServicios from '../views/VisualizarServicios.vue'
import Login from "../views/Login";


const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/charts",
    name: "charts",
    component: ChartsView,
  },
  {
    path: "/search-solicitudes",
    name: "search-solicitudes",
    component: SearchSolicitudesView,
  },
  {
    path: "/solicitud-detalle/:id",
    name: "SolicitudDetalle",
    component: SolicitudDetalle,
  },
  {
    path: "/solicitud-detalle/:id_solicitud/:id_user",
    name: "AgregarNota",
    component: AgregarNota,
  },
  {
    path: "/visualizar-servicios/:id",
    name: "VisualizarServicios",
    component: VisualizarServicios,
  },
  { path: "/login", component: Login },

];
  


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  const publicPages = ['/', '/login'];
  const authRequired = !publicPages.includes(to.path);
  const token = localStorage.getItem('token');

  if (authRequired && !token) {
    return next('/login');
  }

  next();
});

export default router
