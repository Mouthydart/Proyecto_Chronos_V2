import { authService } from '../services/authService.js'

export const requireAuth = (to, from, next) => {
  // Verificar si el usuario está autenticado
  if (!authService.isAuthenticated()) {
    // Redirigir al login si no está autenticado
    next('/')
  } else {
    // Continuar a la ruta solicitada
    next()
  }
}

export const redirectIfAuthenticated = (to, from, next) => {
  // Si ya está autenticado, redirigir al home
  if (authService.isAuthenticated()) {
    next('/home')
  } else {
    next()
  }
}
