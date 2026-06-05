import axios from 'axios'

// URL base del backend
const API_URL =
  import.meta.env.VITE_API_URL || "https://chronos-2xg1.onrender.com";


// Crear instancia de Axios
const api = axios.create({
  baseURL: `${API_URL}/api`,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Interceptor JWT
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')

    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }

    return config
  },
  (error) => Promise.reject(error)
)

// Manejo errores autenticación
api.interceptors.response.use(
  (response) => response,
  (error) => {

    if (error.response?.status === 401) {

      localStorage.removeItem('token')
      localStorage.removeItem('user')

      window.location.href = '/'
    }

    return Promise.reject(error)
  }
)

export default api