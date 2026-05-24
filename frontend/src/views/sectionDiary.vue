<template>
  <div class="flex min-h-screen">

    <AppSidebar />

    <main class="flex-1 bg-white flex flex-col">

      <div class="text-center py-8">
        <h1 class="text-5xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600">
          Mi Diario
        </h1>
      </div>

      <div class="flex flex-1 px-8 gap-8 items-start">

        <section class="flex-1 flex flex-col border rounded-xl shadow p-4 bg-white min-h-[70vh]">

          <div class="mb-4">
            <div class="bg-blue-100 text-gray-800 px-4 py-3 rounded-2xl max-w-md shadow">
              ¿Cómo estuvo tu día?
            </div>
          </div>

          <div class="flex-1 overflow-y-auto space-y-3 mb-4">
            <div
              v-for="(entry, index) in diaryEntries"
              :key="index"
              class="bg-gray-100 px-4 py-3 rounded-2xl max-w-md ml-auto text-right shadow"
            >
              {{ entry.text }}
            </div>
          </div>

          <div class="flex gap-2">
            <input
              v-model="newEntry"
              type="text"
              placeholder="Escribe tu respuesta..."
              class="flex-1 border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
              @keyup.enter="addEntry"
            />

            <button
              @click="addEntry"
              class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition"
            >
              Enviar
            </button>
          </div>

        </section>

        <aside class="w-96 border rounded-xl shadow-lg p-4 bg-white min-h-[70vh]">

          <h2 class="text-2xl font-bold text-center mb-4">
            {{ currentMonthName }} {{ currentYear }}
          </h2>

          <div class="grid grid-cols-7 gap-2 mb-2 text-center font-semibold text-gray-500">
            <div v-for="day in weekDays" :key="day">
              {{ day }}
            </div>
          </div>

          <div class="grid grid-cols-7 gap-2">

            <div v-for="blank in firstDayOfMonth" :key="'b-' + blank"></div>

            <button
              v-for="day in daysInMonth"
              :key="day"
              @click="selectDay(day)"
              class="h-10 rounded-lg font-medium transition"
              :class="selectedDay === day
                ? 'bg-gradient-to-r from-blue-600 to-purple-600 text-white shadow'
                : 'bg-gray-100 hover:bg-blue-100'"
            >
              {{ day }}
            </button>

          </div>

          <!-- MENSAJE -->
          <div class="mt-6 border-t pt-4">

            <h3 class="font-bold text-gray-700 mb-2">
              Mensaje del día
            </h3>

            <div class="bg-gray-100 rounded-xl p-4 min-h-[140px] shadow-inner">

              <p v-if="selectedDayMessage" class="text-gray-700">
                {{ selectedDayMessage }}
              </p>

              <p v-else class="text-gray-400 italic">
                Haz clic en un día del calendario...
              </p>

            </div>

          </div>

        </aside>

      </div>

    </main>
  </div>
</template>



<script setup>
import { ref, computed } from 'vue'
import AppSidebar from '../components/appSideBar.vue'
import { diaryService } from '../services/diaryService'

const diaryEntries = ref([])
const newEntry = ref('')

const selectedDay = ref(null)
const selectedDayMessage = ref('')

const addEntry = async () => {
  if (!newEntry.value.trim()) return

  try {

    const userText = newEntry.value

    // guardar en backend
    const response = await diaryService.saveEntry(userText)

    // agregar al chat
    diaryEntries.value.push({
      text: userText,
      ai_phrase: response.ai_phrase,
      date: new Date()
    })

    // mostrar mensaje IA
    selectedDayMessage.value = response.ai_phrase

    // limpiar input
    newEntry.value = ''

  } catch (error) {

    console.error('Error guardando entrada:', error)

  }
}

const today = new Date()

const currentMonthName = computed(() =>
  today.toLocaleString('es-ES', { month: 'long' })
)

const currentYear = computed(() => today.getFullYear())

const weekDays = ['L', 'M', 'X', 'J', 'V', 'S', 'D']

const daysInMonth = computed(() =>
  new Date(today.getFullYear(), today.getMonth() + 1, 0).getDate()
)

const firstDayOfMonth = computed(() =>
  new Date(today.getFullYear(), today.getMonth(), 1).getDay()
)

const selectDay = async (day) => {

  selectedDay.value = day

  const month = String(today.getMonth() + 1).padStart(2, '0')
  const formattedDay = String(day).padStart(2, '0')

  const fullDate = `${today.getFullYear()}-${month}-${formattedDay}`

  try {

    const response = await diaryService.getEntryByDate(fullDate)

    // mensaje del calendario
    selectedDayMessage.value = response.ai_phrase

    // cargar conversación en el chat
    diaryEntries.value = [
      {
        text: response.content,
        ai_phrase: response.ai_phrase,
        date: fullDate
      }
    ]

  } catch (error) {

    console.error('Error obteniendo entrada:', error)

    selectedDayMessage.value = 'Error cargando mensaje'

  }
}
</script>