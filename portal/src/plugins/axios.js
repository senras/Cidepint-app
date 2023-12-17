import axios from 'axios';

const instance = axios.create({
  //baseURL: 'http://127.0.0.1:5000/api/auth/', 
  baseURL: 'https://admin-grupo06.proyecto2023.linti.unlp.edu.ar/api/auth/', 
  withCredentials: true,
});

export default instance;