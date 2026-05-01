<template>
  <div class="flex min-h-screen">
    
    <AppSidebar />

    <main class="flex-grow p-8 bg-white overflow-y-auto">
     
    <div class="flex-1 flex flex-col p-8 mt-4">

    <!--título-->
        <div
            class="text-center inline-block text-6xl font-bold text-transparent bg-clip-text bg-linear-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 transition-all duration-300">
            Bienvenido a Chronos ({{ nombreUsuario }})
        </div>

    <!--texto-->       
        <div
        class="inline-block text-2xl font-bold text-black mt-8 mb-8 text-center text-shadow-lg"
      >
        Llevas {{ diasSeguidos }} días seguidos cumpliendo tus rutinas. ¡Excelente trabajo!
        </div>

    <!--texto-->       
        <div class="text-left inline-block mt-4">
            <span
                class="text-lg font-semibold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 transition-all duration-300">
                Páginas recientes
            </span>
        </div>

    <!--tarjetas-->   
        <div class="grid grid-cols-4 gap-32 mt-8">
            <Card 
                v-for="card in tarjetasOrdenadas"
                :key="card.title"
                :title="card.title" 
                :imageSrc="card.imageSrc" 
                :to="card.to" 
            />  
        </div>

    <!--texto-->       
        <div class="text-left inline-block mt-16 mb-4">
            <span
                class="text-lg font-semibold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 transition-all duration-300">
                Recordatorios
            </span>
        </div>

    <!--recordatorios--> 
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            <div
                v-for="(reminder, index) in proximosRecordatorios"
                :key="reminder.id"
                class="border rounded-lg p-4 shadow-sm hover:shadow-md transition-shadow cursor-pointer"
                :class="reminder.completed ? 'bg-green-50 border-green-200' : 'bg-white border-gray-200'"
                @click="verRecordatorio(reminder)"
            >
                <!-- Header con ícono y título -->
                <div class="flex items-start gap-3 mb-3">
                    <div class="w-8 h-8 rounded-lg flex items-center justify-center text-sm flex-shrink-0"
                        :class="reminder.completed ? 'bg-green-100' : categoriaInfo(reminder.categoria).iconBg">
                        {{ reminder.completed ? '✅' : categoriaInfo(reminder.categoria).icono }}
                    </div>
                    <div class="flex-1 min-w-0">
                        <h4 class="font-medium text-sm leading-tight"
                            :class="reminder.completed ? 'text-green-800 line-through' : 'text-gray-900'">
                            {{ reminder.titulo }}
                        </h4>
                        <div class="flex items-center gap-2 mt-1">
                            <span class="text-xs font-medium px-2 py-0.5 rounded-full inline-block"
                                :class="reminder.completed ? 'bg-green-100 text-green-700' : categoriaInfo(reminder.categoria).badge">
                                {{ reminder.completed ? 'Completada' : categoriaInfo(reminder.categoria).label }}
                            </span>
                            <span v-if="reminder.completed" class="text-xs text-green-600 font-medium">
                                Completada {{ formatDate(reminder.completedAt) }}
                            </span>
                        </div>
                    </div>
                </div>

                <!-- Fecha de vencimiento -->
                <div class="flex items-center justify-between text-xs">
                    <span class="font-medium"
                        :class="reminder.completed ? 'text-green-600' : 'text-gray-500'">
                        {{ reminder.completed ? 'Completada el:' : 'Fecha de vencimiento:' }}
                    </span>
                    <div class="flex items-center gap-1 px-2 py-1 rounded-md font-semibold"
                        :class="reminder.completed ? 'bg-green-100 text-green-700' : 'bg-blue-50 text-blue-700'">
                        <span>📅</span>
                        <span>{{ formatDate(reminder.fecha) }}</span>
                    </div>
                </div>
            </div>
        </div>

    </div>

    <!-- Modal: Ver recordatorio -->
    <Teleport to="body">
    <div v-if="modalVerAbierto" class="fixed inset-0 z-50 flex items-center justify-center">

      <!-- Fondo oscuro -->
      <div class="absolute inset-0 bg-black/50" @click="modalVerAbierto = false"></div>

      <!-- Caja del modal -->
    <div class="relative bg-white rounded-2xl shadow-2xl w-full max-w-md mx-4 p-6 z-10" v-if="recordatorioSeleccionado">
        
      <!-- Header con ícono y categoría -->
      <div class="flex items-start gap-3 mb-4">

            <div class="w-10 h-10 rounded-xl flex items-center justify-center text-xl flex-shrink-0"
            :class="categoriaInfo(recordatorioSeleccionado.categoria).iconBg">
            {{ categoriaInfo(recordatorioSeleccionado.categoria).icono }}
            </div>

            <div class="flex-1">

            <h3 class="font-bold text-lg leading-tight text-gray-800">{{ recordatorioSeleccionado.titulo }}</h3>
            <span class="text-xs font-medium px-2 py-0.5 rounded-full mt-1 inline-block"
                :class="categoriaInfo(recordatorioSeleccionado.categoria).badge">
                {{ categoriaInfo(recordatorioSeleccionado.categoria).label }}
            </span>

            </div>
      </div>

      <!-- Detalle -->
      <div class="grid grid-cols-2 gap-3 text-sm mt-2">

          <p class="flex items-center gap-2 text-gray-500">
                    <span>📅</span> {{ formatearFechaLarga(recordatorioSeleccionado.fecha) }}
          </p>

          <p class="flex items-center gap-2 text-gray-500" v-if="recordatorioSeleccionado.hora">
                    <span>🕐</span> {{ recordatorioSeleccionado.hora }}
          </p>

          <p class="flex items-center gap-2" v-if="recordatorioSeleccionado.prioridad">
                    <span>🚩</span>
                    <span class="text-xs font-semibold px-2 py-0.5 rounded-full border"
                        :class="getPriorityClass(recordatorioSeleccionado.prioridad)">
                        {{ recordatorioSeleccionado.prioridad }}
                    </span>
          </p>

          <p class="flex items-center gap-2 text-gray-500" v-if="recordatorioSeleccionado.tipo">
                    <span>🏷️</span> {{ recordatorioSeleccionado.tipo }}
          </p>

          <p class="flex items-center gap-2 text-gray-500" v-if="recordatorioSeleccionado.materia">
                    <span>📖</span> {{ recordatorioSeleccionado.materia }}
          </p>

          <p class="flex items-center gap-2 text-gray-500" v-if="recordatorioSeleccionado.frecuencia">
                    <span>🔁</span> {{ recordatorioSeleccionado.frecuencia }}
          </p>

          <p class="flex items-center gap-2 text-gray-500" v-if="recordatorioSeleccionado.montoNumerico">
                    <span>💰</span> {{ recordatorioSeleccionado.monto }}
          </p>

      </div>

      <p class="flex items-start gap-2 text-gray-500 text-sm mt-3" v-if="recordatorioSeleccionado.descripcion">
            <span>📝</span> {{ recordatorioSeleccionado.descripcion }}
      </p>

      <!-- Acciones -->
      <div class="flex justify-end gap-2 mt-6">

        <button 
            class="px-4 py-2 text-sm font-semibold rounded-lg border-2 border-red-400 text-red-500 hover:bg-red-50 transition-colors duration-200"
            @click="eliminarRecordatorio(recordatorioSeleccionado.id)">
            Eliminar
        </button>

        <button 
            class="px-4 py-2 text-sm font-semibold rounded-lg border-2 border-green-500 text-green-600 hover:bg-green-50 transition-colors duration-200"
            @click="completarRecordatorio(recordatorioSeleccionado.id)">
            Completar
        </button>

        <button 
            class="px-4 py-2 text-sm font-semibold rounded-lg border-2 border-blue-500 text-blue-600 hover:bg-blue-50 transition-colors duration-200"
            @click="irAEditar(recordatorioSeleccionado)">
            Editar
        </button>

        <button 
            class="px-4 py-2 text-sm font-semibold rounded-lg bg-gradient-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 text-white transition-all duration-300"
            @click="modalVerAbierto = false">
            Cerrar
        </button>

      </div>

    </div>

    </div>
    </Teleport>

    <!-- Modal de Edición -->
    <Teleport to="body">
    <div v-if="modalEditarAbierto" class="fixed inset-0 z-50 flex items-center justify-center">
      <!-- Fondo oscuro -->
      <div class="absolute inset-0 bg-black/50" @click="cancelarEdicion"></div>
      
      <!-- Caja del modal -->
      <div class="relative bg-white rounded-2xl shadow-2xl w-full max-w-2xl mx-4 p-6 z-10" v-if="recordatorioEditando">
        <!-- Header -->
        <div class="flex items-start gap-3 mb-6">
          <div class="w-10 h-10 rounded-xl flex items-center justify-center text-xl flex-shrink-0"
            :class="categoriaInfo(recordatorioEditando.categoria).iconBg">
            {{ categoriaInfo(recordatorioEditando.categoria).icono }}
          </div>
          <div class="flex-1">
            <h3 class="font-bold text-lg leading-tight text-gray-800">Editar Recordatorio</h3>
            <span class="text-xs font-medium px-2 py-0.5 rounded-full mt-1 inline-block"
              :class="categoriaInfo(recordatorioEditando.categoria).badge">
              {{ categoriaInfo(recordatorioEditando.categoria).label }}
            </span>
          </div>
          <button @click="cancelarEdicion" class="text-gray-400 hover:text-gray-600">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>

        <!-- Formulario de edición -->
        <form @submit.prevent="guardarEdicion" class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Título</label>
            <input v-model="recordatorioEditando.titulo" type="text" class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500" required>
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Fecha</label>
            <input v-model="recordatorioEditando.fecha" type="date" class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500" required>
          </div>
          
          <!-- Campos específicos por categoría -->
          <div v-if="recordatorioEditando.categoria === 'estudio'">
            <label class="block text-sm font-medium text-gray-700 mb-1">Materia</label>
            <input v-model="recordatorioEditando.materia" type="text" class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
          </div>
          
          <div v-if="recordatorioEditando.categoria === 'estudio'">
            <label class="block text-sm font-medium text-gray-700 mb-1">Tipo</label>
            <select v-model="recordatorioEditando.tipo" class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
              <option value="tarea">Tarea</option>
              <option value="examen">Examen</option>
              <option value="proyecto">Proyecto</option>
            </select>
          </div>
          
          <div v-if="recordatorioEditando.categoria === 'salud'">
            <label class="block text-sm font-medium text-gray-700 mb-1">Tipo</label>
            <select v-model="recordatorioEditando.tipo" class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
              <option value="cita-medica">Cita Médica</option>
              <option value="medicamento">Medicamento</option>
              <option value="ejercicio">Ejercicio</option>
            </select>
          </div>
          
          <div v-if="recordatorioEditando.categoria === 'finanzas'">
            <label class="block text-sm font-medium text-gray-700 mb-1">Tipo</label>
            <select v-model="recordatorioEditando.tipo" class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
              <option value="gasto">Gasto</option>
              <option value="ingreso">Ingreso</option>
              <option value="inversion">Inversión</option>
            </select>
          </div>
          
          <div v-if="recordatorioEditando.categoria === 'tiempo-libre'">
            <label class="block text-sm font-medium text-gray-700 mb-1">Tipo</label>
            <select v-model="recordatorioEditando.tipo" class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
              <option value="entretenimiento">Entretenimiento</option>
              <option value="deporte">Deporte</option>
              <option value="social">Social</option>
            </select>
          </div>
          
          <div v-if="recordatorioEditando.categoria === 'finanzas'">
            <label class="block text-sm font-medium text-gray-700 mb-1">Monto</label>
            <input v-model="recordatorioEditando.montoNumerico" type="number" step="0.01" class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
          </div>
          
          <div v-if="recordatorioEditando.categoria === 'tiempo-libre'">
            <label class="block text-sm font-medium text-gray-700 mb-1">Frecuencia</label>
            <select v-model="recordatorioEditando.frecuencia" class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
              <option value="diario">Diario</option>
              <option value="semanal">Semanal</option>
              <option value="mensual">Mensual</option>
            </select>
          </div>
          
          <div v-if="recordatorioEditando.categoria !== 'finanzas'">
            <label class="block text-sm font-medium text-gray-700 mb-1">Prioridad</label>
            <select v-model="recordatorioEditando.prioridad" class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500">
              <option value="Baja">Baja</option>
              <option value="Media">Media</option>
              <option value="Alta">Alta</option>
            </select>
          </div>
          
          <div class="col-span-2">
            <label class="block text-sm font-medium text-gray-700 mb-1">Descripción</label>
            <textarea v-model="recordatorioEditando.descripcion" rows="3" class="w-full border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500" required></textarea>
          </div>
          
          <div class="col-span-2 flex justify-end space-x-3 mt-4">
            <button type="button" @click="cancelarEdicion" class="px-4 py-2 border border-gray-300 rounded-md shadow-sm text-gray-700 hover:bg-gray-50">
              Cancelar
            </button>
            <button type="submit" class="px-4 py-2 bg-blue-600 border border-transparent rounded-md shadow-sm text-white hover:bg-blue-700">
              Guardar Cambios
            </button>
          </div>
        </form>
      </div>
    </div>
    </Teleport>

      </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'; 
import { useRouter } from 'vue-router';

import AppSidebar from '../components/appSideBar.vue'; 
import Card from '../components/card.vue';
import seccionEstudio from '../assets/SeccionEstudio.jpg';
import seccionFinanzas from '../assets/SeccionFinanzas.jpg';
import seccionSalud from '../assets/SeccionSalud.jpg';
import seccionTiempoLibre from '../assets/SeccionTiempoLibre.jpg';
import { authService } from '../services/authService.js';
import { academyService } from '../services/academyService.js';
import { healthService } from '../services/healthService.js';
import { financeService } from '../services/financeService.js';
import { leisureService } from '../services/leisureService.js';

const router = useRouter();

const nombreUsuario = ref('Estudiante Ibero');
const diasSeguidos = ref(3);

// Cargar datos del usuario autenticado
const loadUserData = () => {
    const user = authService.getCurrentUser();
    if (user) {
        nombreUsuario.value = user.full_name || user.username || 'Usuario';
    }
};

// Cargar datos al montar el componente
onMounted(() => {
    loadUserData();
    loadRecordatorios();
});

const tarjetas = ref([
    { 
        title: 'Estudio', 
        imageSrc: seccionEstudio, 
        to: '/estudio', 
        lastAccess: new Date('2025-10-25') 
    },
    { 
        title: 'Salud', 
        imageSrc: seccionSalud, 
        to: '/salud', 
        lastAccess: new Date('2025-10-31') 
    },
    { 
        title: 'Finanzas', 
        imageSrc: seccionFinanzas, 
        to: '/finanzas', 
        lastAccess: new Date('2025-10-15') 
    },
    { 
        title: 'Tiempo Libre', 
        imageSrc: seccionTiempoLibre, 
        to: '/tiempo-libre', 
        lastAccess: new Date('2025-10-01') 
    },
]);

const tarjetasOrdenadas = computed(() => {
    const sortedArray = [...tarjetas.value];
    sortedArray.sort((a, b) => b.lastAccess.getTime() - a.lastAccess.getTime());
    return sortedArray;
});

const recordatorios = ref([]);
const loadingRecordatorios = ref(false);

// Cargar recordatorios desde el backend
const loadRecordatorios = async () => {
    loadingRecordatorios.value = true;
    try {
        // Cargar datos de todas las secciones
        const [academyData, healthData, financeData, leisureData] = await Promise.all([
            academyService.getAll().catch(() => []),
            healthService.getAll().catch(() => []),
            financeService.getAll().catch(() => []),
            leisureService.getAll().catch(() => [])
        ]);

        // Convertir datos al formato de recordatorios
        const allRecordatorios = [
            ...academyData.map(item => ({
                id: item._id,
                titulo: item.title,
                categoria: 'estudio',
                fecha: item.due_date ? new Date(item.due_date).toISOString().split('T')[0] : new Date().toISOString().split('T')[0],
                hora: '',
                tipo: item.type || 'tarea',
                materia: item.subject || '',
                prioridad: item.priority || 'Media',
                descripcion: item.description || '',
                notificaciones: true,
                completed: item.completed || false,
                completedAt: item.completedAt || null
            })),
            ...healthData.map(item => ({
                id: item._id,
                titulo: item.title,
                categoria: 'salud',
                fecha: item.appointment_date ? new Date(item.appointment_date).toISOString().split('T')[0] : new Date().toISOString().split('T')[0],
                hora: '',
                tipo: item.type || 'cita-medica',
                materia: '',
                prioridad: item.priority || 'Media',
                descripcion: item.description || '',
                notificaciones: true,
                completed: item.completed || false,
                completedAt: item.completedAt || null
            })),
            ...financeData.map(item => ({
                id: item._id,
                titulo: item.title,
                categoria: 'finanzas',
                fecha: item.due_date ? new Date(item.due_date).toISOString().split('T')[0] : new Date().toISOString().split('T')[0],
                hora: '',
                tipo: item.type || 'gasto',
                materia: '',
                prioridad: 'Media',
                descripcion: item.description || '',
                notificaciones: true,
                completed: item.completed || false,
                completedAt: item.completedAt || null,
                montoNumerico: item.amount || 0,
                monto: new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP', minimumFractionDigits: 0 }).format(item.amount || 0)
            })),
            ...leisureData.map(item => ({
                id: item._id,
                titulo: item.title,
                categoria: 'tiempo-libre',
                fecha: item.scheduled_date ? new Date(item.scheduled_date).toISOString().split('T')[0] : new Date().toISOString().split('T')[0],
                hora: '',
                tipo: item.type || 'entretenimiento',
                materia: '',
                prioridad: item.priority || 'Media',
                descripcion: item.description || '',
                notificaciones: true,
                completed: item.completed || false,
                completedAt: item.completedAt || null,
                frecuencia: item.frequency || 'semanal'
            }))
        ];

        // Filtrar tareas completadas hace más de 2 días
        const twoDaysAgo = new Date();
        twoDaysAgo.setDate(twoDaysAgo.getDate() - 2);
        
        const filteredRecordatorios = allRecordatorios.filter(recordatorio => {
            // Si está completado, verificar si hace menos de 2 días
            if (recordatorio.completed && recordatorio.completedAt) {
                const completedDate = new Date(recordatorio.completedAt);
                return completedDate > twoDaysAgo;
            }
            // Si no está completado, mostrarlo
            return !recordatorio.completed;
        });

        // Ordenar por fecha
        recordatorios.value = filteredRecordatorios.sort((a, b) => new Date(a.fecha) - new Date(b.fecha));
    } catch (error) {
        console.error('Error al cargar recordatorios:', error);
    } finally {
        loadingRecordatorios.value = false;
    }
};

const proximosRecordatorios = computed(() => {
    const sorted = [...recordatorios.value].sort((a, b) => new Date(a.fecha) - new Date(b.fecha));
    return sorted.slice(0, 6); // Mostrar más recordatorios en horizontal
});

// Categorías para recordatorios
const categorias = [
  {
    id: 'estudio',
    label: 'Estudio',
    icono: '📚',
    badge: 'bg-blue-100 text-blue-700',
    chip: 'bg-blue-100 text-blue-700',
    iconBg: 'bg-blue-100',
    dot: 'bg-blue-500',
  },
  {
    id: 'salud',
    label: 'Salud',
    icono: '🩺',
    badge: 'bg-emerald-100 text-emerald-700',
    chip: 'bg-emerald-100 text-emerald-700',
    iconBg: 'bg-emerald-100',
    dot: 'bg-emerald-500',
  },
  {
    id: 'finanzas',
    label: 'Finanzas',
    icono: '💰',
    badge: 'bg-amber-100 text-amber-700',
    chip: 'bg-amber-100 text-amber-700',
    iconBg: 'bg-amber-100',
    dot: 'bg-amber-500',
  },
  {
    id: 'tiempo-libre',
    label: 'Tiempo Libre',
    icono: '🎉',
    badge: 'bg-purple-100 text-purple-700',
    chip: 'bg-purple-100 text-purple-700',
    iconBg: 'bg-purple-100',
    dot: 'bg-purple-500',
  },
  {
    id: 'general',
    label: 'General',
    icono: '📅',
    badge: 'bg-gray-100 text-gray-700',
    chip: 'bg-gray-100 text-gray-700',
    iconBg: 'bg-gray-100',
    dot: 'bg-gray-500',
  },
]

const categoriaInfo = (id) => categorias.find((c) => c.id === id) || categorias[4]

const getPriorityClass = (priority) => {
    switch (priority) {
        case 'Alta': return 'bg-red-100 text-red-800 border-red-300';
        case 'Media': return 'bg-yellow-100 text-yellow-800 border-yellow-300';
        case 'Baja': return 'bg-green-100 text-green-800 border-green-300';
        default: return 'bg-gray-100 text-gray-800 border-gray-300';
    }
};

// ─── Modales ─────────────────────────────────────────────────────
const modalVerAbierto = ref(false)
const recordatorioSeleccionado = ref(null)
const modalEditarAbierto = ref(false)
const recordatorioEditando = ref(null)

function verRecordatorio(rec) {
  recordatorioSeleccionado.value = rec
  modalVerAbierto.value = true
}

async function guardarEdicion() {
  if (!recordatorioEditando.value) return
  
  try {
    console.log('Guardando edición:', recordatorioEditando.value)
    
    // Determinar el servicio según la categoría
    let updateData = {}
    let service = null
    
    switch (recordatorioEditando.value.categoria) {
      case 'estudio':
        service = academyService
        updateData = {
          title: recordatorioEditando.value.titulo,
          description: recordatorioEditando.value.descripcion,
          subject: recordatorioEditando.value.materia,
          priority: recordatorioEditando.value.prioridad,
          due_date: recordatorioEditando.value.fecha,
          type: recordatorioEditando.value.tipo
        }
        break
      case 'salud':
        service = healthService
        updateData = {
          title: recordatorioEditando.value.titulo,
          description: recordatorioEditando.value.descripcion,
          type: recordatorioEditando.value.tipo,
          priority: recordatorioEditando.value.prioridad,
          appointment_date: recordatorioEditando.value.fecha
        }
        break
      case 'finanzas':
        service = financeService
        updateData = {
          title: recordatorioEditando.value.titulo,
          description: recordatorioEditando.value.descripcion,
          type: recordatorioEditando.value.tipo,
          amount: recordatorioEditando.value.montoNumerico || 0,
          due_date: recordatorioEditando.value.fecha
        }
        break
      case 'tiempo-libre':
        service = leisureService
        updateData = {
          title: recordatorioEditando.value.titulo,
          description: recordatorioEditando.value.descripcion,
          type: recordatorioEditando.value.tipo,
          priority: recordatorioEditando.value.prioridad,
          scheduled_date: recordatorioEditando.value.fecha,
          frequency: recordatorioEditando.value.frecuencia
        }
        break
    }
    
    if (service) {
      await service.update(recordatorioEditando.value.id, updateData)
      console.log('Recordatorio actualizado')
      
      // Forzar recarga de datos para sincronizar todo
      await loadRecordatorios()
      
      alert('Recordatorio actualizado correctamente')
      modalEditarAbierto.value = false
      recordatorioEditando.value = null
    }
  } catch (error) {
    console.error('Error al guardar edición:', error)
    alert('Error al actualizar el recordatorio: ' + (error.message || 'Error desconocido'))
  }
}

function cancelarEdicion() {
  modalEditarAbierto.value = false
  recordatorioEditando.value = null
}

async function completarRecordatorio(id) {
  const recordatorio = recordatorios.value.find(r => r.id === id)
  if (!recordatorio) return
  
  try {
    console.log('Intentando completar recordatorio:', recordatorio)
    
    // Marcar como completado en el array local (para mostrar en verde)
    const index = recordatorios.value.findIndex(r => r.id === id)
    if (index !== -1) {
      recordatorios.value[index].completed = true
      recordatorios.value[index].completedAt = new Date().toISOString()
      console.log('Tarea marcada como completada localmente')
    }
    
    // Determinar el servicio según la categoría
    let updateData = {}
    let service = null
    
    switch (recordatorio.categoria) {
      case 'estudio':
        service = academyService
        updateData = {
          title: recordatorio.titulo,
          description: recordatorio.descripcion,
          subject: recordatorio.materia,
          priority: recordatorio.prioridad,
          due_date: recordatorio.fecha,
          completed: true,
          completedAt: new Date().toISOString()
        }
        break
      case 'salud':
        service = healthService
        updateData = {
          title: recordatorio.titulo,
          description: recordatorio.descripcion,
          type: recordatorio.tipo,
          priority: recordatorio.prioridad,
          appointment_date: recordatorio.fecha,
          completed: true,
          completedAt: new Date().toISOString()
        }
        break
      case 'finanzas':
        service = financeService
        updateData = {
          title: recordatorio.titulo,
          description: recordatorio.descripcion,
          type: recordatorio.tipo,
          amount: recordatorio.montoNumerico || 0,
          due_date: recordatorio.fecha,
          completed: true,
          completedAt: new Date().toISOString()
        }
        break
      case 'tiempo-libre':
        service = leisureService
        updateData = {
          title: recordatorio.titulo,
          description: recordatorio.descripcion,
          type: recordatorio.tipo,
          priority: recordatorio.prioridad,
          scheduled_date: recordatorio.fecha,
          frequency: recordatorio.frecuencia,
          completed: true,
          completedAt: new Date().toISOString()
        }
        break
    }
    
    if (service) {
      await service.update(id, updateData)
      console.log('Tarea marcada como completada en localStorage persistente')
    }
    
    alert('Tarea completada correctamente')
  } catch (error) {
    console.error('Error al completar recordatorio:', error)
    alert('Error al actualizar el recordatorio: ' + (error.message || 'Error desconocido'))
  }
  
  modalVerAbierto.value = false
}

async function eliminarRecordatorio(id) {
  const recordatorio = recordatorios.value.find(r => r.id === id)
  if (!recordatorio) return
  
  try {
    console.log('Intentando eliminar recordatorio:', recordatorio)
    
    // Eliminar inmediatamente del array local
    const index = recordatorios.value.findIndex(r => r.id === id)
    if (index !== -1) {
      recordatorios.value.splice(index, 1)
      console.log('Recordatorio eliminado del array local')
    }
    
    // Determinar el servicio según la categoría
    let service = null
    
    switch (recordatorio.categoria) {
      case 'estudio':
        service = academyService
        break
      case 'salud':
        service = healthService
        break
      case 'finanzas':
        service = financeService
        break
      case 'tiempo-libre':
        service = leisureService
        break
    }
    
    if (service) {
      await service.delete(id)
      console.log('Recordatorio eliminado del localStorage persistente')
      
      // Recargar datos para asegurar sincronización completa
      await loadRecordatorios()
      console.log('Datos recargados después de eliminación')
    }
    
    alert('Recordatorio eliminado correctamente')
  } catch (error) {
    console.error('Error al eliminar recordatorio:', error)
    alert('Error al eliminar el recordatorio: ' + (error.message || 'Error desconocido'))
  }
  
  modalVerAbierto.value = false
}

function irAEditar(recordatorio) {
  modalVerAbierto.value = false
  recordatorioEditando.value = { ...recordatorio }
  modalEditarAbierto.value = true
}

function formatearFechaLarga(fechaStr) {
  const [y, m, d] = fechaStr.split('-')
  return `${parseInt(d)} de ${['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'][parseInt(m) - 1]} de ${y}`
}

const formatDate = (dateStr) => {
    const date = new Date(dateStr);
    return date.toLocaleDateString('es-ES', { day: 'numeric', month: 'short' });
};

const irARuta = (ruta) => {
console.log(`Simulando navegación a la sección: ${ruta}`);
};

</script>