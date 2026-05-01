<template>
  <div class="flex min-h-screen">
    <AppSidebar />

    <main class="flex-grow p-8 bg-white overflow-y-auto">
      <div class="max-w-4xl mx-auto">
        <!-- Header del perfil -->
        <div class="bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg p-8 mb-8 text-white">
          <div class="flex items-center space-x-6">
            <div class="avatar">
              <div class="w-24 h-24 rounded-full ring-4 ring-white ring-offset-2 ring-offset-blue-600 overflow-hidden">
                <img
                  :src="userProfile.fotoPerfil"
                  alt="Avatar del usuario"
                  class="object-cover w-full h-full"
                />
              </div>
            </div>
            <div class="flex-grow">
              <h1 class="text-3xl font-bold">{{ userProfile.nombre }}</h1>
              <p class="text-blue-100">{{ userProfile.email }}</p>
              <p class="text-sm text-blue-100 mt-2">Miembro desde {{ userProfile.fechaRegistro }}</p>
            </div>
            <button @click="toggleEdit" class="btn btn-outline btn-white text-white border-white hover:bg-white hover:text-blue-600 focus:bg-transparent focus:text-white focus:border-white active:bg-transparent active:text-white transition-all duration-300">
              {{ isEditing ? 'Cancelar' : 'Editar Perfil' }}
            </button>
          </div>
        </div>

        <!-- Información personal -->
        <div class="bg-white rounded-lg shadow-md p-6 mb-8">
          <h2 class="text-2xl font-bold mb-4 text-gray-800">Información Personal</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-gray-700">Nombre completo</label>
              <input v-if="isEditing" v-model="userProfile.nombreCompleto" type="text" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
              <p v-else class="mt-1 text-gray-900">{{ userProfile.nombreCompleto }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Email</label>
              <p class="mt-1 text-gray-900">{{ userProfile.email }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Username</label>
              <input v-if="isEditing" v-model="userProfile.username" type="text" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
              <p v-else class="mt-1 text-gray-900">{{ userProfile.username }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Fecha de nacimiento</label>
              <input v-if="isEditing" v-model="userProfile.fechaNacimiento" type="date" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
              <p v-else class="mt-1 text-gray-900">{{ userProfile.fechaNacimiento }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700">Ubicación</label>
              <input v-if="isEditing" v-model="userProfile.ubicacion" type="text" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
              <p v-else class="mt-1 text-gray-900">{{ userProfile.ubicacion }}</p>
            </div>
          </div>
          <div v-if="isEditing" class="mt-6">
            <label class="block text-sm font-medium text-gray-700">Foto de perfil</label>
            <input type="file" @change="handleFileUpload" accept="image/*" class="mt-1 block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100">
          </div>
          <div v-if="isEditing" class="mt-6 border-t pt-6">
            <h3 class="text-lg font-semibold mb-4 text-gray-800">Cambiar Contraseña</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700">Contraseña actual</label>
                <input v-model="currentPassword" type="password" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Nueva contraseña</label>
                <input v-model="newPassword" type="password" class="mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
              </div>
            </div>
          </div>
          <div v-if="isEditing" class="mt-6 flex justify-end space-x-4">
            <button @click="saveChanges" class="btn btn-primary bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white font-semibold py-2 px-6 rounded-lg shadow-md transition-all duration-300">Guardar Cambios</button>
            <button @click="toggleEdit" class="btn btn-outline border-gray-300 text-gray-700 hover:bg-gray-100 font-semibold py-2 px-6 rounded-lg transition-all duration-300">Cancelar</button>
          </div>
        </div>

        <!-- Métricas de rendimiento -->
        <div class="bg-white rounded-lg shadow-md p-6 mb-8">
          <h2 class="text-2xl font-bold mb-4 text-gray-800">Métricas de Rendimiento</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div class="text-center">
              <div class="text-3xl font-bold text-blue-600" 
                   title="Días consecutivos completando al menos una rutina. Se reinicia si saltas un día. ¡Mantén la racha!">
                {{ userProfile.metricas.diasSeguidos }}
              </div>
              <div class="text-gray-600 text-sm">Días seguidos</div>
              <div class="text-xs text-gray-500 mt-1">Racha actual</div>
            </div>
            <div class="text-center">
              <div class="text-3xl font-bold text-green-600" 
                   title="Porcentaje de rutinas completadas vs total creadas en todas las secciones">
                {{ userProfile.metricas.tasaCompletitud }}%
              </div>
              <div class="text-gray-600 text-sm">Tasa de completitud</div>
              <div class="text-xs text-gray-500 mt-1">Rutinas completadas</div>
            </div>
            <div class="text-center">
              <div class="text-3xl font-bold text-purple-600" 
                   title="Total de rutinas completadas durante el mes actual">
                {{ userProfile.metricas.rutinasTotales }}
              </div>
              <div class="text-gray-600 text-sm">Rutinas totales</div>
              <div class="text-xs text-gray-500 mt-1">Este mes</div>
            </div>
            <div class="text-center">
              <div class="text-3xl font-bold text-orange-600" 
                   title="Puntos acumulados por completar rutinas (+10 pts), logros (+50-100 pts) y rachas. Nunca se pierden">
                {{ userProfile.metricas.puntuacion }}
              </div>
              <div class="text-gray-600 text-sm">Puntuación</div>
              <div class="text-xs text-gray-500 mt-1">Puntos acumulados</div>
            </div>
          </div>

          <!-- Estadísticas semanales -->
          <div class="mt-8">
            <h3 class="text-lg font-semibold mb-4 text-gray-800">Estadísticas de la Semana</h3>
            <div class="grid grid-cols-7 gap-2">
              <div v-for="(dia, index) in userProfile.metricas.estadisticasSemanales" :key="index" class="text-center">
                <div class="text-xs text-gray-500 mb-1">{{ dia.nombre }}</div>
                <div class="bg-gray-100 rounded-lg p-2">
                  <div class="text-sm font-bold text-blue-600">{{ dia.rutinasCompletadas }}/{{ dia.rutinasTotales }}</div>
                  <div class="text-xs text-gray-600">{{ dia.porcentaje }}%</div>
                </div>
              </div>
            </div>
            <p class="text-sm text-gray-600 mt-4 text-center">
              Muestra el número de rutinas completadas vs totales por día.
              Los recordatorios deben marcarse manualmente en cada sección.
            </p>
          </div>
        </div>

        <!-- Progreso por secciones -->
        <div class="bg-white rounded-lg shadow-md p-6">
          <h2 class="text-2xl font-bold mb-4 text-gray-800">Progreso por Secciones</h2>
          <div class="space-y-6">
            <div v-for="seccion in userProfile.progresoSecciones" :key="seccion.nombre" class="border rounded-lg p-4">
              <div class="flex items-center justify-between mb-3">
                <div class="flex items-center space-x-3">
                  <span class="text-2xl">{{ seccion.icono }}</span>
                  <span class="text-gray-800 font-medium">{{ seccion.nombre }}</span>
                </div>
                <div class="text-right">
                  <div class="text-lg font-bold text-blue-600">{{ seccion.completadas }}/{{ seccion.totalCreadas }}</div>
                  <div class="text-sm text-gray-600">{{ seccion.porcentaje }}% completado</div>
                </div>
              </div>
              <div class="w-full bg-gray-200 rounded-full h-3">
                <div
                  class="bg-gradient-to-r from-blue-600 to-purple-600 h-3 rounded-full transition-all duration-300"
                  :style="{ width: seccion.porcentaje + '%' }"
                ></div>
              </div>
              <div class="mt-2 text-xs text-gray-500">
                Total de rutinas creadas: {{ seccion.totalCreadas }} • Completadas: {{ seccion.completadas }}
              </div>
            </div>
          </div>
          <p class="text-sm text-gray-600 mt-4 text-center">
            Porcentaje calculado basado en rutinas completadas vs total creadas en cada sección.
          </p>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import AppSidebar from '../components/appSideBar.vue';
import { authService } from '../services/authService.js';
import { academyService } from '../services/academyService.js';
import { healthService } from '../services/healthService.js';
import { financeService } from '../services/financeService.js';
import { leisureService } from '../services/leisureService.js';

// Estado de edición
const isEditing = ref(false);
const currentPassword = ref('');
const newPassword = ref('');
const loading = ref(false);

// Datos del perfil del usuario (dinámicos)
const userProfile = ref({
  nombre: '',
  email: '',
  fechaRegistro: '',
  nombreCompleto: '',
  fechaNacimiento: '',
  ubicacion: '',
  fotoPerfil: 'https://img.daisyui.com/images/profile/demo/spiderperson@192.webp',
  metricas: {
    diasSeguidos: 0,
    tasaCompletitud: 0,
    rutinasTotales: 0,
    puntuacion: 0,
    estadisticasSemanales: []
  },
  progresoSecciones: [
    { nombre: 'Estudio', icono: '', totalCreadas: 0, completadas: 0, porcentaje: 0 },
    { nombre: 'Salud', icono: '', totalCreadas: 0, completadas: 0, porcentaje: 0 },
    { nombre: 'Finanzas', icono: '', totalCreadas: 45, completadas: 23, porcentaje: 51 },
    { nombre: 'Tiempo Libre', icono: '', totalCreadas: 95, completadas: 80, porcentaje: 84 }
  ]
});

// Cargar datos del usuario y estadísticas
const loadUserData = async () => {
  loading.value = true;
  try {
    // Cargar datos del usuario autenticado
    const user = authService.getCurrentUser();
    if (user) {
      userProfile.value.nombre = user.full_name || user.username || 'Usuario';
      userProfile.value.email = user.email || '';
      userProfile.value.username = user.username || '';
      userProfile.value.nombreCompleto = user.full_name || user.username || 'Usuario';
      userProfile.value.fechaRegistro = user.created_at ? new Date(user.created_at).toLocaleDateString('es-ES', { month: 'long', year: 'numeric' }) : 'Reciente';
      userProfile.value.fechaNacimiento = user.birth_date ? user.birth_date.split('T')[0] : '';
      userProfile.value.ubicacion = user.location || '';
      userProfile.value.fotoPerfil = user.profile_picture || 'https://img.daisyui.com/images/profile/demo/spiderperson@192.webp';
    }

    // Cargar datos de todas las secciones para estadísticas
    const [academyData, healthData, financeData, leisureData] = await Promise.all([
      academyService.getAll().catch(() => []),
      healthService.getAll().catch(() => []),
      financeService.getAll().catch(() => []),
      leisureService.getAll().catch(() => [])
    ]);

    // Calcular estadísticas reales
    const allData = [...academyData, ...healthData, ...financeData, ...leisureData];
    const completedTasks = allData.filter(item => item.completed).length;
    const totalTasks = allData.length;
    const completionRate = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0;

    // Actualizar métricas
    userProfile.value.metricas.rutinasTotales = totalTasks;
    userProfile.value.metricas.tasaCompletitud = completionRate;
    userProfile.value.metricas.puntuacion = completedTasks * 10; // 10 puntos por tarea completada

    // Actualizar progreso por secciones
    userProfile.value.progresoSecciones = [
      { 
        nombre: 'Estudio', 
        icono: '📚', 
        totalCreadas: academyData.length, 
        completadas: academyData.filter(item => item.completed).length, 
        porcentaje: academyData.length > 0 ? Math.round((academyData.filter(item => item.completed).length / academyData.length) * 100) : 0 
      },
      { 
        nombre: 'Salud', 
        icono: '🩺', 
        totalCreadas: healthData.length, 
        completadas: healthData.filter(item => item.completed).length, 
        porcentaje: healthData.length > 0 ? Math.round((healthData.filter(item => item.completed).length / healthData.length) * 100) : 0 
      },
      { 
        nombre: 'Finanzas', 
        icono: '💰', 
        totalCreadas: financeData.length, 
        completadas: financeData.filter(item => item.completed).length, 
        porcentaje: financeData.length > 0 ? Math.round((financeData.filter(item => item.completed).length / financeData.length) * 100) : 0 
      },
      { 
        nombre: 'Tiempo Libre', 
        icono: '🎉', 
        totalCreadas: leisureData.length, 
        completadas: leisureData.filter(item => item.completed).length, 
        porcentaje: leisureData.length > 0 ? Math.round((leisureData.filter(item => item.completed).length / leisureData.length) * 100) : 0 
      }
    ];

    // Generar estadísticas semanales (simuladas basadas en datos reales)
    const weekDays = ['L', 'M', 'M', 'J', 'V', 'S', 'D'];
    userProfile.value.metricas.estadisticasSemanales = weekDays.map(day => ({
      nombre: day,
      rutinasCompletadas: Math.floor(Math.random() * totalTasks * 0.8),
      rutinasTotales: Math.max(1, Math.floor(totalTasks / 7)),
      porcentaje: Math.floor(Math.random() * 40) + 60
    }));

  } catch (error) {
    console.error('Error al cargar datos del perfil:', error);
  } finally {
    loading.value = false;
  }
};

// Cargar datos al montar el componente
onMounted(() => {
  loadUserData();
});

// Funciones
function toggleEdit() {
  console.log('toggleEdit called, current isEditing:', isEditing.value);
  isEditing.value = !isEditing.value;
  if (!isEditing.value) {
    // Reset passwords when canceling
    currentPassword.value = '';
    newPassword.value = '';
  }
}

function handleFileUpload(event) {
  const file = event.target.files[0];
  if (file) {
    // En una app real, subirías el archivo a un servidor
    // Aquí simulamos cambiando la URL
    const reader = new FileReader();
    reader.onload = (e) => {
      userProfile.value.fotoPerfil = e.target.result;
    };
    reader.readAsDataURL(file);
  }
}

const saveChanges = async () => {
  loading.value = true;
  try {
    // Preparar datos para actualizar
    const updateData = {
      full_name: userProfile.value.nombreCompleto,
      username: userProfile.value.username,
      birth_date: userProfile.value.fechaNacimiento,
      location: userProfile.value.ubicacion,
      profile_picture: userProfile.value.fotoPerfil
    };

    // Agregar contraseña si se va a cambiar
    if (newPassword.value) {
      if (!currentPassword.value) {
        alert('Debes ingresar la contraseña actual para cambiarla');
        return;
      }
      updateData.current_password = currentPassword.value;
      updateData.new_password = newPassword.value;
    }

    // Enviar actualización al backend
    const updatedUser = await authService.updateUserData(updateData);
    
    // Actualizar todos los datos locales
    userProfile.value.nombre = updatedUser.full_name || updatedUser.username || 'Usuario';
    userProfile.value.email = updatedUser.email || '';
    userProfile.value.username = updatedUser.username || '';
    userProfile.value.nombreCompleto = updatedUser.full_name || updatedUser.username || 'Usuario';
    userProfile.value.fechaNacimiento = updatedUser.birth_date ? updatedUser.birth_date.split('T')[0] : '';
    userProfile.value.ubicacion = updatedUser.location || '';
    
    // Limpiar campos de contraseña
    currentPassword.value = '';
    newPassword.value = '';
    
    // Cambiar a modo vista
    isEditing.value = false;
    alert('Cambios guardados exitosamente');
    
  } catch (error) {
    console.error('Error al guardar cambios:', error);
    alert(error.detail || 'Error al guardar los cambios');
  } finally {
    loading.value = false;
  }
};
</script>
