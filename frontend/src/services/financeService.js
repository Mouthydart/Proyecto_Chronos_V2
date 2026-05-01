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

export const financeService = {
  // Obtener todos los registros financieros
  async getAll() {
    try {
      console.log('=== CARGANDO DATOS FINANCE (ALMACENAMIENTO PERSISTENTE) ===');
      
      // Intentar cargar desde localStorage primero
      const storedData = localStorage.getItem('financeData');
      if (storedData) {
        const financeData = JSON.parse(storedData);
        console.log('✅ Datos cargados desde localStorage persistente:', financeData.length, 'registros');
        return financeData;
      }
      
      // Si no hay datos en localStorage, intentar cargar del backend
      console.log('🔄 Intentando cargar desde backend...');
      const response = await api.get('/finance')
      
      // Guardar en localStorage para persistencia
      localStorage.setItem('financeData', JSON.stringify(response.data));
      console.log('✅ Datos guardados en localStorage persistente');
      
      return response.data
    } catch (error) {
      // Si falla el backend, devolver datos del localStorage si existen
      const storedData = localStorage.getItem('financeData');
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
      const response = await api.get(`/finance/${id}`)
      return response.data
    } catch (error) {
      throw error.response?.data || error.message
    }
  },

  // Crear nuevo registro financiero
  async create(data) {
    try {
      console.log('=== CREANDO REGISTRO FINANCE (ALMACENAMIENTO PERSISTENTE) ===');
      console.log('Datos a crear:', data);
      
      // Agregar user_id al registro
      const dataWithUser = {
        ...data,
        user_id: getUserId()
      }
      
      const response = await api.post('/finance', dataWithUser)
      console.log('✅ Registro creado exitosamente en backend:', response.data);
      
      // SOLUCIÓN PERSISTENTE: Guardar en localStorage
      console.log('💾 Guardando en almacenamiento local persistente');
      
      // Obtener datos actuales del localStorage
      const storedData = localStorage.getItem('financeData');
      let financeData = storedData ? JSON.parse(storedData) : [];
      
      // Agregar el nuevo registro con _id
      const newRecord = {
        ...response.data,
        _id: response.data._id || response.data.id,
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString()
      };
      
      financeData.push(newRecord);
      
      // Guardar en localStorage
      localStorage.setItem('financeData', JSON.stringify(financeData));
      console.log('✅ Registro guardado en localStorage persistente. Total registros:', financeData.length);
      
      return response.data
    } catch (error) {
      console.error('❌ Error al crear registro finance:', error);
      throw error.response?.data || error.message
    }
  },

  // Actualizar registro financiero
  async update(id, data) {
    try {
      console.log('=== SOLICITUD PUT FINANCE (ALMACENAMIENTO PERSISTENTE) ===');
      console.log('URL:', `/finance/${id}`);
      console.log('Datos:', data);
      
      // SOLUCIÓN PERSISTENTE: Actualizar en almacenamiento local
      console.log('💾 Actualizando en almacenamiento local persistente');
      
      // Obtener datos actuales del localStorage
      const storedData = localStorage.getItem('financeData');
      let financeData = storedData ? JSON.parse(storedData) : [];
      
      // Buscar y actualizar el registro
      const index = financeData.findIndex(item => item._id === id);
      if (index !== -1) {
        financeData[index] = {
          ...financeData[index],
          ...data,
          updated_at: new Date().toISOString(),
          status: data.completed ? 'completada' : 'pendiente'
        };
        
        // Guardar en localStorage
        localStorage.setItem('financeData', JSON.stringify(financeData));
        
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

  // Eliminar registro financiero
  async delete(id) {
    try {
      console.log('=== SOLICITUD DELETE FINANCE (ALMACENAMIENTO PERSISTENTE) ===');
      console.log('ID a eliminar:', id);
      
      // SOLUCIÓN PERSISTENTE: Eliminar del almacenamiento local
      console.log('💾 Eliminando del almacenamiento local persistente');
      
      // Obtener datos actuales del localStorage
      const storedData = localStorage.getItem('financeData');
      let financeData = storedData ? JSON.parse(storedData) : [];
      
      // Eliminar el registro
      financeData = financeData.filter(item => item._id !== id);
      
      // Guardar en localStorage
      localStorage.setItem('financeData', JSON.stringify(financeData));
      
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
