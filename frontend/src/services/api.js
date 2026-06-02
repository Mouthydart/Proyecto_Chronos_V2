import axios from 'axios'

const API_BASE_URL = 'https://chronos-2xg1.onrender.com'
//const API_BASE_URL = 'http://localhost:8000/api'
// BIEN (Detecta automáticamente si estás en producción o en local)
const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";


// Crear instancia de Axios con configuración base
const api = axios.create({
  //baseURL: API_BASE_URL,
  baseURL:`${API_URL}/api`,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Interceptor para añadir token JWT a las peticiones
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Interceptor para manejar errores de autenticación
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      const detail = error.response?.data?.detail;
      console.log('Error 401 detectado:', detail);
      
      // Limpiar datos de autenticación
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      
      // Mostrar mensaje específico según el error
      if (detail === 'Could not validate credentials') {
        alert('Tu sesión ha expirado. Por favor inicia sesión nuevamente.');
      } else {
        alert('Error de autenticación. Por favor inicia sesión nuevamente.');
      }
      
      // Redirigir al login
      window.location.href = '/';
    }
    return Promise.reject(error)
  }
)

export default api
