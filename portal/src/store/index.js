// store/index.js
import Vuex from 'vuex';
export default new Vuex.Store({
  state: {
    isLoggedIn: (localStorage.getItem('token') !== null) ? true : false,
    idFromToken: (localStorage.getItem('token') !== null) ? JSON.parse(atob(localStorage.getItem('token').split('.')[1])).sub : -1,
  },
  mutations: {
    login(state) {
      state.isLoggedIn = true;
      state.idFromToken = JSON.parse(atob(localStorage.getItem('token').split('.')[1])).sub;
    },
    logout(state) {
      state.isLoggedIn = false;
      state.idFromToken = -1;
    },
  },
  actions: {
    loginUser({ commit }) {
      // Perform login actions, e.g., authenticate user
      // After successful login, commit the 'login' mutation
      commit('login');
      // additional login actions...
    },
    logoutUser({ commit }) {
      // Perform logout actions, e.g., clear authentication
      // After successful logout, commit the 'logout' mutation
      commit('logout');
      // additional logout actions...
    },
  },
  getters: {
    isLoggedIn: state => state.isLoggedIn,
    idFromToken: state => state.idFromToken,
  },
});

