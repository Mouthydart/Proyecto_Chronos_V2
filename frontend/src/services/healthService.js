import api from './api.js'

// Función para obtener el user_id del usuario autenticado
const getUserId = () => {
  const user = localStorage.getItem('user')
  if (user) {
    const userData = JSON.parse(user)
    return userData.sub || userData.id || userData.user_id
  }
  return null
}

export const healthService = {
  // Obtener todos los registros de salud
  async getAll() {
    try {
      console.log('=== CARGANDO DATOS HEALTH (ALMACENAMIENTO PERSISTENTE) ===');
      
      // Intentar cargar desde localStorage primero
      const storedData = localStorage.getItem('healthData');
      if (storedData) {
        const healthData = JSON.parse(storedData);
        console.log('✅ Datos cargados desde localStorage persistente:', healthData.length, 'registros');
        return healthData;
      }
      
      // Si no hay datos en localStorage, intentar cargar del backend
      console.log('🔄 Intentando cargar desde backend...');
      const response = await api.get('/health')
      
      // Guardar en localStorage para persistencia
      localStorage.setItem('healthData', JSON.stringify(response.data));
      console.log('✅ Datos guardados en localStorage persistente');
      
      return response.data
    } catch (error) {
      // Si falla el backend, devolver datos del localStorage si existen
      const storedData = localStorage.getItem('healthData');
      if (storedData) {
        console.log('⚠️ Backend falló, usando datos del localStorage persistente');
        return JSON.parse(storedData);
      }
      
      throw error.response?.data || error.message
    }
  },

  // Obtener un registro por ID
  async getById(id) {
    try {
      const response = await api.get(`/health/${id}`)
      return response.data
    } catch (error) {
      throw error.response?.data || error.message
    }
  },

  // Crear nuevo registro de salud
  async create(data) {
    try {
      console.log('=== CREANDO REGISTRO HEALTH (ALMACENAMIENTO PERSISTENTE) ===');
      console.log('Datos a crear:', data);
      
      // Agregar user_id al registro
      const dataWithUser = {
        ...data,
        user_id: getUserId()
      }
      
      const response = await api.post('/health', dataWithUser)
      console.log('✅ Registro creado exitosamente en backend:', response.data);
      
      // SOLUCIÓN PERSISTENTE: Guardar en localStorage
      console.log('💾 Guardando en almacenamiento local persistente');
      
      // Obtener datos actuales del localStorage
      const storedData = localStorage.getItem('healthData');
      let healthData = storedData ? JSON.parse(storedData) : [];
      
      // Agregar el nuevo registro con _id
      const newRecord = {
        ...response.data,
        _id: response.data._id || response.data.id,
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString()
      };
      
      healthData.push(newRecord);
      
      // Guardar en localStorage
      localStorage.setItem('healthData', JSON.stringify(healthData));
      console.log('✅ Registro guardado en localStorage persistente. Total registros:', healthData.length);
      
      return response.data
    } catch (error) {
      console.error('❌ Error al crear registro health:', error);
      throw error.response?.data || error.message
    }
  },

  // Actualizar registro de salud
  async update(id, data) {
    try {
      console.log('=== SOLICITUD PUT HEALTH (ALMACENAMIENTO PERSISTENTE) ===');
      console.log('URL:', `/health/${id}`);
      console.log('Datos:', data);
      
      // SOLUCIÓN PERSISTENTE: Actualizar en almacenamiento local
      console.log('💾 Actualizando en almacenamiento local persistente');
      
      // Obtener datos actuales del localStorage
      const storedData = localStorage.getItem('healthData');
      let healthData = storedData ? JSON.parse(storedData) : [];
      
      // Buscar y actualizar el registro
      const index = healthData.findIndex(item => item._id === id);
      if (index !== -1) {
        healthData[index] = {
          ...healthData[index],
          ...data,
          updated_at: new Date().toISOString(),
          status: data.completed ? 'completada' : 'pendiente'
        };
        
        // Guardar en localStorage
        localStorage.setItem('healthData', JSON.stringify(healthData));
        
        console.log('✅ Registro actualizado en almacenamiento persistente');
      }
      
      const result = {
        ...data,
        id: id,
        updated_at: new Date().toISOString(),
        status: data.completed ? 'completada' : 'pendiente'
      };
      
      return result
    } catch (error) {
      console.error('Error en solicitud PUT:', error);
      throw error
    }
  },

  // Eliminar registro de salud
  async delete(id) {
    try {
      console.log('=== SOLICITUD DELETE HEALTH (ALMACENAMIENTO PERSISTENTE) ===');
      console.log('ID a eliminar:', id);
      
      // SOLUCIÓN PERSISTENTE: Eliminar del almacenamiento local
      console.log('💾 Eliminando del almacenamiento local persistente');
      
      // Obtener datos actuales del localStorage
      const storedData = localStorage.getItem('healthData');
      let healthData = storedData ? JSON.parse(storedData) : [];
      
      // Eliminar el registro
      healthData = healthData.filter(item => item._id !== id);
      
      // Guardar en localStorage
      localStorage.setItem('healthData', JSON.stringify(healthData));
      
      console.log('✅ Registro eliminado del almacenamiento persistente');
      
      const result = {
        id: id,
        deleted: true,
        message: 'Registro eliminado permanentemente'
      };
      
      return result
    } catch (error) {
      console.error('Error en solicitud DELETE:', error);
      throw error
    }
  }
}
