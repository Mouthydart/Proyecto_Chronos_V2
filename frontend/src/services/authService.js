import api from './api.js'

export const authService = {
  // Registro de usuario
  async register(userData) {
    try {
      const response = await api.post('/auth/register', userData)
      return response.data
    } catch (error) {
      throw error.response?.data || error.message
    }
  },

  // Login de usuario
  async login(credentials) {
    try {
      const response = await api.post('/auth/login', credentials)
      const { access_token } = response.data
      
      // Guardar token
      localStorage.setItem('token', access_token)
      
      // Obtener datos completos del usuario desde el backend
      const userData = await this.getCurrentUserData()
      localStorage.setItem('user', JSON.stringify(userData))
      
      return response.data
    } catch (error) {
      throw error.response?.data || error.message
    }
  },

  // Logout
  logout() {
    localStorage.removeItem('token')
    localStorage.removeItem('user')
    window.location.href = '/'
  },

  // Decodificar token JWT
  decodeToken(token) {
    try {
      const base64Url = token.split('.')[1]
      const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/')
      const jsonPayload = decodeURIComponent(
        atob(base64)
          .split('')
          .map(c => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
          .join('')
      )
      return JSON.parse(jsonPayload)
    } catch (error) {
      return null
    }
  },

  // Verificar si está autenticado
  isAuthenticated() {
    const token = localStorage.getItem('token')
    if (!token) return false
    
    try {
      const decoded = this.decodeToken(token)
      const currentTime = Date.now() / 1000
      return decoded.exp > currentTime
    } catch (error) {
      return false
    }
  },

  // Obtener usuario actual
  getCurrentUser() {
    const user = localStorage.getItem('user')
    return user ? JSON.parse(user) : null
  },

  // Obtener token
  getToken() {
    return localStorage.getItem('token')
  },

  // Obtener datos del usuario desde el backend
  async getCurrentUserData() {
    try {
      const response = await api.get('/auth/me')
      return response.data
    } catch (error) {
      throw error.response?.data || error.message
    }
  },

  // Actualizar datos del usuario
  async updateUserData(userData) {
    try {
      const response = await api.put('/auth/me', userData)
      
      // Actualizar datos en localStorage
      const updatedUser = response.data
      localStorage.setItem('user', JSON.stringify(updatedUser))
      
      return response.data
    } catch (error) {
      throw error.response?.data || error.message
    }
  }
}
