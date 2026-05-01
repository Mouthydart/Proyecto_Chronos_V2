<template>
  <div class="flex min-h-screen">
    <AppSidebar />

    <main class="flex-grow px-2 py-8 bg-white overflow-y-auto">

    <div class="min-h-screen bg-base-200 px-2 md:px-4 py-4 font-sans">

    <!-- Header del calendario -->
    <div class="max-w-7xl mx-auto">
    
        <div class="flex items-center justify-between mb-6">
            <div>
                <h1 
                    class="text-5xl font-bold text-transparent bg-clip-text bg-linear-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 transition-all duration-300">Mi Calendario
                </h1>
                <p 
                   class="text-sm font-medium text-transparent bg-clip-text bg-linear-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 transition-all duration-300">Gestiona tus recordatorios
                </p>
            </div>

        <!-- Navegación mes -->
            <div class="flex items-center gap-3">

            <button class= "rounded-full w-8 h-8 flex items-center justify-center bg-blue-600 hover:bg-blue-700 text-white transition-colors duration-200" @click="mesAnterior">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2.5" stroke="currentColor" class="size-[1.2em]"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7"  />
                </svg>
            </button>

            <h2 
                class="text-3xl font-semibold text-transparent bg-clip-text bg-linear-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 transition-all duration-300">
                    {{ nombreMes }} {{ anioActual }}
            </h2>

            <button class= "rounded-full w-8 h-8 flex items-center justify-center bg-blue-600 hover:bg-blue-700 text-white transition-colors duration-200" @click="mesSiguiente">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2.5" stroke="currentColor" class="size-[1.2em]"><path stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"  />
                </svg>
            </button>

            </div>
        </div>

        <!-- Leyenda de categorías -->
        <div class="flex flex-wrap items-center justify-between gap-3 mb-4">

            <div class="flex flex-wrap gap-3">
                <span v-for="cat in categorias" :key="cat.id"
                class="flex items-center gap-1.5 text-xs font-medium px-3 py-1 rounded-full"
                :class="cat.badge">
                <span class="w-2 h-2 rounded-full" :class="cat.dot"></span>
                {{ cat.label }}
                </span>
            </div>

            <button 
                   @click="abrirModalNuevo"
                    class="bg-gradient-to-br from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 text-white font-bold py-2 px-4 rounded-lg shadow-lg transition duration-300 transform ">
                    Nuevo +
            </button>

        </div>

        <!-- Grid del calendario -->
        <div class="rounded-2xl shadow-xl overflow-hidden border border-blue-100">

        <!-- Días de la semana -->
        <div class="grid grid-cols-7 bg-gradient-to-r from-blue-600 to-purple-600 ">
            <div v-for="dia in diasSemana" :key="dia"
            class="py-3 text-center text-xs font-bold text-white uppercase tracking-widest">
            {{ dia }}
            </div>
        </div>

        <!-- Días del mes -->
        <div class="grid grid-cols-7">
            <div
            v-for="(celda, idx) in celdasCalendario"
            :key="idx"
            class="min-h-[110px] border-b border-r border-blue-100 p-1.5 transition-colors duration-150 relative group bg-white"
            :class="{
                'bg-blue-50/40': !celda.esDelMes,
                'bg-gradient-to-br from-blue-50 to-purple-50 ring-2 ring-inset ring-blue-500': celda.esHoy,
                'hover:bg-blue-50/60 cursor-pointer': celda.esDelMes,
            }"
            @click="celda.esDelMes && abrirModalNuevo(celda.fecha)"
            >
            <!-- Número del día -->
            <div class="flex justify-between items-start mb-1">
                <span
                class="text-sm font-medium w-7 h-7 flex items-center justify-center rounded-full transition-colors"
                :class="{
                    'text-gray-300': !celda.esDelMes,
                    'bg-gradient-to-r from-blue-600 to-purple-600 text-white font-bold': celda.esHoy,
                    'text-gray-700': celda.esDelMes && !celda.esHoy,
                }"
                >
                {{ celda.dia }}
                </span>
            </div>

            <!-- Recordatorios del día -->
            <div class="flex flex-col gap-0.5 overflow-hidden">
                <template v-for="(rec, i) in recordatoriosDia(celda.fecha)" :key="rec.id">
                <div
                    v-if="i < 3"
                    class="text-[11px] px-1.5 py-0.5 rounded font-medium truncate cursor-pointer hover:opacity-80 transition-opacity"
                    :class="categoriaInfo(rec.categoria).chip"
                    @click.stop="verRecordatorio(rec)"
                    :title="rec.titulo"
                >
                    <span v-if="rec.completed" class="mr-1">✅</span>{{ rec.titulo }}
                </div>
                <div
                    v-if="i === 3"
                    class="text-[10px] text-blue-400 pl-1 cursor-pointer hover:text-blue-600 hover:underline transition-colors"
                    @click.stop="verTodosDelDia(celda.fecha)"
                >
                    +{{ recordatoriosDia(celda.fecha).length - 3 }} más
                </div>
                </template>
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
            :class="[
                'px-4 py-2 text-sm font-semibold rounded-lg border-2 transition-colors duration-200',
                recordatorioSeleccionado.completed 
                    ? 'border-gray-500 text-gray-600 hover:bg-gray-50' 
                    : 'border-green-500 text-green-600 hover:bg-green-50'
            ]"
            @click="completarRecordatorio(recordatorioSeleccionado.id)">
            {{ recordatorioSeleccionado.completed ? 'Deshacer' : 'Completar' }}
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

    <!-- Modal: Crear recordatorio -->
    <Teleport to="body">
    <div v-if="modalNuevoAbierto" class="fixed inset-0 z-50 flex items-center justify-center">

        <div class="absolute inset-0 bg-black/50" @click="modalNuevoAbierto = false"></div>

        <!-- Caja del modal -->
        <div class="relative bg-white rounded-2xl shadow-2xl w-full max-w-md mx-4 p-6 z-10">
        
            <h3 class="text-xl mb-8 font-semibold text-transparent bg-clip-text bg-linear-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 transition-all duration-300">
                ¿Qué tipo de recordatorio quieres crear? 
            </h3>

           <div class="grid grid-cols-2 gap-8">

                <button
                    v-for="cat in categorias" :key="cat.id"
                    type="button"
                    class="flex flex-col items-center justify-center gap-2 p-4 rounded-2xl text-white font-semibold text-sm shadow-md hover:scale-105 hover:shadow-lg transition-all duration-200"
                    :class="cat.btnActive"
                    @click="irACrear(cat.id)"
                >
                    <span class="text-2xl">{{ cat.icono }}</span>
                    <span>{{ cat.label }}</span>
                </button>

            </div>

            <div class="flex justify-end mt-4">
                <button class= "flex-1 px-4 py-2 text-sm font-semibold rounded-lg border-2 border-red-400 text-red-500 hover:bg-red-50 transition-colors duration-200" 
                @click="modalNuevoAbierto = false">
                    Cancelar
                </button>
            </div>

        </div>

    </div>
    </Teleport>

    <!-- Modal: Lista de recordatorios del día -->
    <Teleport to="body">
    <div v-if="modalDiaAbierto" class="fixed inset-0 z-50 flex items-center justify-center">
      
      <!-- Fondo oscuro -->
      <div class="absolute inset-0 bg-black/50" @click="modalDiaAbierto = false"></div>

      <!-- Caja del modal -->
      <div class="relative bg-white rounded-2xl shadow-2xl w-full max-w-md mx-4 p-6 z-10" v-if="diaSeleccionado">
        
        <h3 class="font-bold text-lg mb-4 text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600  hover:from-orange-600 hover:to-pink-400 transition-all duration-300">
          {{ formatearFechaLarga(diaSeleccionado) }}
        </h3>

        <div class="flex flex-col gap-2">
          <div
            v-for="rec in recordatoriosDia(diaSeleccionado)"
            :key="rec.id"
            class="flex items-center gap-3 p-2 rounded-lg cursor-pointer hover:bg-gray-50 transition-colors"
            @click="abrirDesdeListaDia(rec)"
          >
            <div class="w-8 h-8 rounded-lg flex items-center justify-center text-base flex-shrink-0"
              :class="categoriaInfo(rec.categoria).iconBg">
              {{ categoriaInfo(rec.categoria).icono }}
            </div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-medium text-gray-800 truncate">
                <span v-if="rec.completed" class="mr-1">✅</span>{{ rec.titulo }}
              </p>
              <p class="text-xs text-gray-400" v-if="rec.hora">🕐 {{ rec.hora }}</p>
            </div>
            <span class="text-xs px-2 py-0.5 rounded-full flex-shrink-0" :class="categoriaInfo(rec.categoria).chip">
              {{ categoriaInfo(rec.categoria).label }}
            </span>
          </div>
        </div>

        <div class="flex justify-end mt-4">
          
          <button 
            class="px-4 py-2 text-sm font-semibold rounded-lg bg-gradient-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 text-white transition-all duration-300"
            @click="modalDiaAbierto = false">
            Cerrar
          </button>

        </div>

      </div>
    </div>
    </Teleport>

    </div>

    </main>
  </div>

</template>

<script setup>

import { ref, computed, onMounted } from 'vue'; 
import { useRouter } from 'vue-router';

import AppSidebar from '../components/appSideBar.vue'; 
import { academyService } from '../services/academyService.js';
import { healthService } from '../services/healthService.js';
import { financeService } from '../services/financeService.js';
import { leisureService } from '../services/leisureService.js'; 


const router = useRouter();

// ─── Fecha actual ───────────────────────────────────────────────
const hoy = new Date()
const mesActual = ref(hoy.getMonth())
const anioActual = ref(hoy.getFullYear())

// ─── Categorías ─────────────────────────────────────────────────
const categorias = [
  {
    id: 'estudio',
    label: 'Estudio',
    icono: '📚',
    badge: 'bg-blue-100 text-blue-700',
    dot: 'bg-blue-600',
    chip: 'bg-blue-100 text-blue-700',
    iconBg: 'bg-blue-100',
    btnActive: 'bg-blue-600 text-white border-none',
  },
  {
    id: 'salud',
    label: 'Salud',
    icono: '🩺',
    badge: 'bg-emerald-100 text-emerald-700',
    dot: 'bg-emerald-500',
    chip: 'bg-emerald-100 text-emerald-700',
    iconBg: 'bg-emerald-100',
    btnActive: 'bg-emerald-500 text-white border-none',
  },
  {
    id: 'finanzas',
    label: 'Finanzas',
    icono: '💰',
    badge: 'bg-amber-100 text-amber-700',
    dot: 'bg-amber-500',
    chip: 'bg-amber-100 text-amber-700',
    iconBg: 'bg-amber-100',
    btnActive: 'bg-amber-500 text-white border-none',
  },
  {
    id: 'tiempo-libre',
    label: 'Tiempo libre',
    icono: '🎮',
    badge: 'bg-rose-100 text-rose-700',
    dot: 'bg-rose-500',
    chip: 'bg-rose-100 text-rose-700',
    iconBg: 'bg-rose-100',
    btnActive: 'bg-rose-500 text-white border-none',
  },
]

const categoriaInfo = (id) => categorias.find((c) => c.id === id) || categorias[3]

// ─── Recordatorios desde backend ─────────────────────────────────────
const recordatorios = ref([])

// Cargar datos desde todos los servicios
const loadRecordatorios = async () => {
  try {
    console.log('📅 Cargando datos para calendario...');
    
    // Cargar datos de todos los módulos
    const [academyData, healthData, financeData, leisureData] = await Promise.all([
      academyService.getAll(),
      healthService.getAll(),
      financeService.getAll(),
      leisureService.getAll()
    ]);

    // Mapear datos al formato del calendario
    const todosLosRecordatorios = [
      // Estudio
      ...academyData.map(item => ({
        id: item._id,
        titulo: item.title,
        categoria: 'estudio',
        fecha: item.due_date ? new Date(item.due_date).toISOString().slice(0, 10) : new Date().toISOString().slice(0, 10),
        hora: item.due_date ? new Date(item.due_date).toTimeString().slice(0, 5) : '',
        tipo: 'tarea',
        materia: item.subject || '',
        prioridad: item.priority || 'Media',
        descripcion: item.description || '',
        completed: item.completed || false
      })),
      
      // Salud
      ...healthData.map(item => ({
        id: item._id,
        titulo: item.title,
        categoria: 'salud',
        fecha: item.due_date ? new Date(item.due_date).toISOString().slice(0, 10) : new Date().toISOString().slice(0, 10),
        hora: item.due_date ? new Date(item.due_date).toTimeString().slice(0, 5) : '',
        tipo: getCategoryLabel(item.category) || 'General',
        prioridad: item.priority || 'Media',
        descripcion: item.description || '',
        completed: item.completed || false
      })),
      
      // Finanzas
      ...financeData.map(item => ({
        id: item._id,
        titulo: item.title,
        categoria: 'finanzas',
        fecha: item.due_date ? new Date(item.due_date).toISOString().slice(0, 10) : new Date().toISOString().slice(0, 10),
        hora: item.due_date ? new Date(item.due_date).toTimeString().slice(0, 5) : '',
        tipo: item.type || 'General',
        montoNumerico: item.amount || 0,
        monto: item.amount ? new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP', minimumFractionDigits: 0 }).format(item.amount) : '',
        prioridad: item.priority || 'Media',
        descripcion: item.description || '',
        completed: item.completed || false
      })),
      
      // Tiempo libre
      ...leisureData.map(item => ({
        id: item._id,
        titulo: item.title,
        categoria: 'tiempo-libre',
        fecha: item.due_date ? new Date(item.due_date).toISOString().slice(0, 10) : new Date().toISOString().slice(0, 10),
        hora: item.due_date ? new Date(item.due_date).toTimeString().slice(0, 5) : '',
        tipo: getCategoryLabel(item.category) || 'General',
        frecuencia: item.frequency || 'Semanal',
        prioridad: item.priority || 'Media',
        descripcion: item.description || '',
        completed: item.completed || false
      }))
    ];

    recordatorios.value = todosLosRecordatorios;
    console.log(`✅ Calendario cargado: ${todosLosRecordatorios.length} recordatorios`);
  } catch (error) {
    console.error('❌ Error al cargar recordatorios para calendario:', error);
    recordatorios.value = [];
  }
};

// Función auxiliar para obtener etiquetas de categorías
const getCategoryLabel = (category) => {
  switch (category) {
    case 'consulta': return 'Cita médica';
    case 'medicacion': return 'Medicamento';
    case 'ejercicio': return 'Ejercicio';
    case 'nutricion': return 'Nutrición';
    case 'mental': return 'Salud mental';
    case 'deportes': return 'Deportes';
    case 'lectura': return 'Lectura';
    case 'videojuegos': return 'Videojuegos';
    case 'social': return 'Social';
    case 'viajes': return 'Viajes';
    case 'otros': return 'Otros';
    default: return category || 'General';
  }
};

// Cargar datos al montar el componente
onMounted(() => {
  loadRecordatorios();
});

const getPriorityClass = (priority) => {
    switch (priority) {
        case 'Alta': return 'bg-red-100 text-red-800 border-red-300';
        case 'Media': return 'bg-yellow-100 text-yellow-800 border-yellow-300';
        case 'Baja': return 'bg-green-100 text-green-800 border-green-300';
        default: return 'bg-gray-100 text-gray-800 border-gray-300';
    }
};

function formatDate(base, offsetDays) {
  const d = new Date(base)
  d.setDate(d.getDate() + offsetDays)
  return d.toISOString().slice(0, 10)
}

// ─── Lógica del calendario ───────────────────────────────────────
const diasSemana = ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb']
const meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

const nombreMes = computed(() => meses[mesActual.value])

const celdasCalendario = computed(() => {
  const primero = new Date(anioActual.value, mesActual.value, 1)
  const ultimo = new Date(anioActual.value, mesActual.value + 1, 0)
  const celdas = []

  // Días del mes anterior
  for (let i = 0; i < primero.getDay(); i++) {
    const d = new Date(anioActual.value, mesActual.value, 1 - (primero.getDay() - i))
    celdas.push({ dia: d.getDate(), fecha: d.toISOString().slice(0, 10), esDelMes: false, esHoy: false })
  }

  // Días del mes actual
  for (let d = 1; d <= ultimo.getDate(); d++) {
    const fecha = new Date(anioActual.value, mesActual.value, d)
    const fechaStr = fecha.toISOString().slice(0, 10)
    const hoyStr = hoy.toISOString().slice(0, 10)
    celdas.push({ dia: d, fecha: fechaStr, esDelMes: true, esHoy: fechaStr === hoyStr })
  }

  // Completar hasta múltiplo de 7
  const restante = 7 - (celdas.length % 7)
  if (restante < 7) {
    for (let i = 1; i <= restante; i++) {
      const d = new Date(anioActual.value, mesActual.value + 1, i)
      celdas.push({ dia: d.getDate(), fecha: d.toISOString().slice(0, 10), esDelMes: false, esHoy: false })
    }
  }
  return celdas
})

const recordatoriosDia = (fecha) => recordatorios.value.filter((r) => r.fecha === fecha)

// ─── Navegación ──────────────────────────────────────────────────
function mesAnterior() {
  if (mesActual.value === 0) { mesActual.value = 11; anioActual.value-- }
  else mesActual.value--
}
function mesSiguiente() {
  if (mesActual.value === 11) { mesActual.value = 0; anioActual.value++ }
  else mesActual.value++
}

// ─── Modales ─────────────────────────────────────────────────────
const modalVerAbierto = ref(false)
const modalNuevoAbierto = ref(false)
const modalDiaAbierto = ref(false)
const recordatorioSeleccionado = ref(null)
const diaSeleccionado = ref(null)

function irACrear(categoriaId) {
  modalNuevoAbierto.value = false
  const rutas = {
    'estudio':      '/createAcademy',
    'salud':        '/createHealth',
    'finanzas':     '/createFinance',
    'tiempo-libre': '/createLeisure',
  }
  router.push(rutas[categoriaId])
}

function irAEditar(rec) {
    modalVerAbierto.value = false
    const rutas = {
        'estudio':      `/editAcademy/${rec.id}`,
        'salud':        `/editHealth/${rec.id}`,
        'finanzas':     `/editFinance/${rec.id}`,
        'tiempo-libre': `/editLeisure/${rec.id}`,
    }
    router.push(rutas[rec.categoria])
}

function verRecordatorio(rec) {
  recordatorioSeleccionado.value = rec
  modalVerAbierto.value = true
}

function abrirModalNuevo() {
  modalNuevoAbierto.value = true
}

function eliminarRecordatorio(id) {
  recordatorios.value = recordatorios.value.filter((r) => r.id !== id)
  modalVerAbierto.value = false
}

function completarRecordatorio(id) {
  const rec = recordatorios.value.find(r => r.id === id)
  if (rec) {
    rec.completed = !rec.completed
  }
}

function verTodosDelDia(fecha) {
    diaSeleccionado.value = fecha
    modalDiaAbierto.value = true
}

function abrirDesdeListaDia(rec) {
    modalDiaAbierto.value = false
    recordatorioSeleccionado.value = rec
    modalVerAbierto.value = true
}

function formatearFechaLarga(fechaStr) {
  const [y, m, d] = fechaStr.split('-')
  return `${parseInt(d)} de ${meses[parseInt(m) - 1]} de ${y}`
}


</script>