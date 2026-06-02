<template>
  <div class="flex min-h-screen">
    <AppSidebar />
    <main class="flex-grow p-8 bg-white overflow-y-auto relative">

    <div class="flex-1 flex flex-col p-4 ">
        <div class="flex items-center justify-between mb-16">

        <!--titulo-->
            <div class="w-32"></div> 
                <div class="flex items-center gap-4">
                    <div
                        class="text-5xl font-bold text-transparent bg-clip-text bg-linear-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 transition-all duration-300">
                        Módulo de salud
                    </div>
                </div>
        <!--boton-->   
                <button 
                    @click="navigateToCreateHealth"
                    class="bg-gradient-to-br from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 text-white font-bold py-2 px-4 rounded-lg shadow-lg transition duration-300 transform ">
                    Agregar registro
                </button>

        </div>

        <!--tabla-->
           <DynamicTable 
            :data="healthData" 
            :columns="healthColumns" 
            :currentPage="currentPage"
            :totalPages="totalPages"
            :showActions="false"
            @page-change="goToPage"
            @next="nextPage"
            @prev="prevPage"
        >
            <template #cell-priority="{ item }">
                <span :class="getPriorityClass(item.priority)" 
                      class="inline-flex items-center justify-center px-2 py-0.5 text-xs font-medium rounded-full border">
                    {{ item.priority }}
                </span>
            </template>
            
            <template #cell-date="{ item }">
                <span class="font-mono text-xs">{{ new Date(item.date).toLocaleDateString() }}</span>
            </template>

           </DynamicTable>

    </div>

      <!-- Icono de Inteligencia Artificial - Esquina inferior derecha -->
      <div @click="SectionDia" class="fixed bottom-8 right-8 text-2xl cursor-pointer hover:scale-110 transition-transform duration-200 bg-gradient-to-br from-blue-600 to-purple-600 text-white rounded-full w-12 h-12 flex items-center justify-center shadow-lg hover:shadow-xl" title="Inteligencia Artificial">
        🤖
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
import SectionDiary from './sectionDiary.vue';

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

const SectionDia = () => {
    router.push('/salud/diary')
}
</script>