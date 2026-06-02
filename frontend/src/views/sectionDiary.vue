<template>
    <div class="flex min-h-screen">
        <AppSidebar />
        <main class="flex-1 p-8 bg-white overflow-y-auto">
            <div class="flex flex-col">
                <div class="w-full flex justify-center items-center mb-6">
                    <div
                        class="text-5xl font-bold text-transparent bg-clip-text bg-linear-to-r from-blue-600 to-purple-600">
                        Mi Diario
                    </div>
                </div>

                <div class="flex flex-col lg:flex-row gap-6">

                    <!--diario-->
                    <div class="flex-1 flex flex-col border rounded-xl shadow p-4 bg-white">

                        <div class="flex mb-4">
                            <div class="bg-blue-100 text-gray-800 px-4 py-3 rounded-2xl max-w-md shadow">
                                ¿Cómo estuvo tu día?
                            </div>
                        </div>

                        <div class="flex-1 overflow-y-auto space-y-3 mb-4">
                            <div v-for="(entry, index) in diaryEntries" :key="index"
                                class="bg-gray-100 px-4 py-3 rounded-2xl max-w-md ml-auto text-right shadow">
                                {{ entry.text }}
                            </div>
                        </div>

                        <div class="flex gap-2">
                            <input v-model="newEntry" type="text" placeholder="Escribe tu respuesta..."
                                class="flex-1 border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
                                @keyup.enter="addEntry" />

                            <button @click="addEntry"
                                class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition">
                                Enviar
                            </button>
                        </div>

                    </div>

                    <!--calendario-->
                    <div class="w-full lg:w-96 bg-white border rounded-xl shadow-lg p-4 flex flex-col">

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

                            <button v-for="day in daysInMonth" :key="day" @click="selectDay(day)"
                                class="h-10 rounded-lg transition font-medium" :class="selectedDay === day
                                    ? 'bg-gradient-to-r from-blue-600 to-purple-600 text-white'
                                    : 'bg-gray-100 hover:bg-blue-100'">
                                {{ day }}
                            </button>
                        </div>

                        <div class="mt-6 border-t pt-4">
                            <h3 class="font-bold text-gray-700 mb-2">Mensaje del día</h3>

                            <div class="bg-gray-100 rounded-xl p-4 min-h-[140px] shadow-inner">
                                <p v-if="selectedDayMessage">
                                    {{ selectedDayMessage }}
                                </p>

                                <p v-else class="text-gray-400 italic">
                                    Haz clic en un día del calendario...
                                </p>
                            </div>
                        </div>

                    </div>

                </div>

            </div>

        </main>

    </div>
</template>



<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';

import AppSidebar from '../components/appSideBar.vue';
import DynamicTable from '../components/dynamicTable.vue';
import { healthService } from '../services/healthService.js';

const router = useRouter();
const healthColumns = ref([
    { key: 'title', label: 'Título', widthClass: 'w-58' },
    { key: 'type', label: 'Tipo', widthClass: 'w-24' },
    { key: 'description', label: 'Descripción', widthClass: 'w-96' },
    { key: 'date', label: 'Fecha', widthClass: 'w-32' },
    { key: 'priority', label: 'Prioridad', widthClass: 'w-28' },
]);

const healthData = ref([]);
const loading = ref(false);
const errorMessage = ref('');

// Cargar datos desde el backend
const loadHealthData = async () => {
    loading.value = true;
    errorMessage.value = '';

    try {
        const response = await healthService.getAll();
        healthData.value = response.map(item => ({
            id: item._id,
            title: item.title,
            type: getCategoryLabel(item.category) || 'General',
            description: item.description || '',
            date: item.due_date || new Date().toISOString(),
            priority: item.priority || 'Media',
            completed: item.completed || false
        }));
    } catch (error) {
        errorMessage.value = 'Error al cargar los datos de salud';
        console.error('Error:', error);
    } finally {
        loading.value = false;
    }
};

// Cargar datos al montar el componente
onMounted(() => {
    loadHealthData();
});

const getPriorityClass = (priority) => {
    switch (priority) {
        case 'Alta': return 'bg-red-100 text-red-800 border-red-300';
        case 'Media': return 'bg-yellow-100 text-yellow-800 border-yellow-300';
        case 'Baja': return 'bg-green-100 text-green-800 border-green-300';
        default: return 'bg-gray-100 text-gray-800 border-gray-300';
    }
};

const getCategoryLabel = (category) => {
    switch (category) {
        case 'consulta': return 'Cita médica';
        case 'medicacion': return 'Medicamento';
        case 'ejercicio': return 'Ejercicio';
        case 'nutricion': return 'Nutrición';
        case 'mental': return 'Salud mental';
        default: return category || 'General';
    }
};

const navigateToCreateHealth = () => {
    router.push('/createHealth');
};

const currentPage = ref(1);
const itemsPerPage = 10;


const totalPages = computed(() => {
    return Math.ceil(healthData.value.length / itemsPerPage);
});

const displayedTasks = computed(() => {
    const start = (currentPage.value - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    return healthData.value.slice(start, end);
});

const goToPage = (pageNumber) => {
    if (pageNumber >= 1 && pageNumber <= totalPages.value) {
        currentPage.value = pageNumber;
    }
};

const nextPage = () => {
    if (currentPage.value < totalPages.value) {
        currentPage.value++;
    }
};

const prevPage = () => {
    if (currentPage.value > 1) {
        currentPage.value--;
    }
};

const today = new Date();

const currentYear = ref(today.getFullYear());
const currentMonth = ref(today.getMonth());
const selectedDay = ref(null);

const weekDays = ['D', 'L', 'M', 'M', 'J', 'V', 'S'];

const currentMonthName = computed(() =>
    new Date(currentYear.value, currentMonth.value)
        .toLocaleString('es-ES', { month: 'long' })
);

const daysInMonth = computed(() =>
    new Date(currentYear.value, currentMonth.value + 1, 0).getDate()
);

const firstDayOfMonth = computed(() =>
    new Date(currentYear.value, currentMonth.value, 1).getDay()
);

// mensajes por día
const selectedDayMessage = computed(() => {
    if (!selectedDay.value) return null;
    return `Mensaje del día ${selectedDay.value}`;
});

const selectDay = (day) => {
    selectedDay.value = day;
};
</script>