import axios from "axios";



 const estados = await axios.get("https://admin-grupo06.proyecto2023.linti.unlp.edu.ar/api/charts/solicitudes_por_estado").then((response) => { return (response.data.data)}).catch((error) => {console.log(error)}) 

//const estados = await axios.get("http://127.0.0.1:5000/api/charts/solicitudes_por_estado").then((response) => { return (response.data.data)}).catch((error) => {console.log(error)}) 


export const data = {
    estados: estados,
    labels: ['Aceptadas', 'Canceladas', 'En proceso', 'Finalizadas','Rechazadas'],
    datasets: [
      {
        backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16', '#FFCE56'],
        data: [estados.Aceptada, estados.Cancelada, estados.En_proceso, estados.Finalizada, estados.Rechazada]
      }
    ]
  }
  
  export const options = {
    responsive: true,
    maintainAspectRatio: false
  }
  