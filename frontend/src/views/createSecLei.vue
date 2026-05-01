<template>
    <div class="p-2 sm:p-4">
    <!--encabezado-->  
        <div class="flex items-start justify-center relative">    
                <button 
                    @click="goBack" 
                    class="absolute left-0 top-0 text-blue-600 hover:text-purple-600 transition-colors duration-300 p-2 rounded-full text-5xl z-10"
                    aria-label="Volver atrás"
                >
                    &#x2190;
                </button>

                <div
                    class="mt-8 text-center text-6xl font-bold text-transparent bg-clip-text bg-linear-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 transition-all duration-300 mx-auto pt-2 pb-2" style="line-height: 1.25;">
                    Crear registro
                </div>
        </div>

    <!--formulario-->
        <div class="grid grid-cols-2 gap-x-8 gap-y-4 p-4 mt-8 max-w-xl mx-auto">
            
            <div>
                <label for="titulo" class="block mb-1 text-sm font-medium text-black">Título de la actividad</label>
                <input 
                    v-model="form.tiempoLibre.titulo"
                    type="text" 
                    id="titulo"
                    name="titulo"
                    class="bg-gray-50 border-2 border-purple-600 text-gray-900 text-sm rounded-lg p-2.5 w-full" 
                    required 
                />
            </div>

            <div>
                <label for="tipo" class="block mb-1 text-sm font-medium text-black">Tipo</label>
                <select 
                    v-model="form.tiempoLibre.tipo"
                    id="tipo"
                    name="tipo"
                    class="bg-gray-50 border-2 border-purple-600 text-gray-900 text-sm rounded-lg p-2.5 w-full appearance-none">
                    <option disabled value="">Selecciona una opción</option>
                    <option value="deportes">Deportes</option>
                    <option value="lectura">Lectura</option>
                    <option value="videojuegos">Videojuegos</option>
                    <option value="social">Social</option>
                    <option value="viajes">Viajes</option>
                    <option value="otros">Otros</option>
                </select>
            </div>

            <div>
                <label for="fecha" class="block mb-1 text-sm font-medium text-black">Fecha</label>
                <input 
                    v-model="form.tiempoLibre.fecha"
                    type="date" 
                    id="fecha"
                    name="fecha"
                    class="bg-gray-50 border-2 border-purple-600 text-gray-900 text-sm rounded-lg p-2.5 w-full appearance-none"
                />
            </div>

            <div>
                <label for="hora" class="block mb-1 text-sm font-medium text-black">Hora</label>
                <input 
                    v-model="form.tiempoLibre.hora"
                    type="time" 
                    id="hora"
                    name="hora"
                    class="bg-gray-50 border-2 border-purple-600 text-gray-900 text-sm rounded-lg p-2.5 w-full appearance-none"
                />
            </div>

            <div>
                <label for="frecuencia" class="block mb-1 text-sm font-medium text-black">Frecuencia</label>
                <select 
                    v-model="form.tiempoLibre.frecuencia"
                    id="frecuencia"
                    name="frecuencia"
                    class="bg-gray-50 border-2 border-purple-600 text-gray-900 text-sm rounded-lg p-2.5 w-full appearance-none">
                    <option disabled value="">Selecciona una opción</option>
                    <option value="diaria">Diaria</option>
                    <option value="dia-por-medio">Día de por medio</option>
                    <option value="semanal">Semanal</option>
                    <option value="quincenal">Quincenal</option>
                    <option value="mensual">Mensual</option>
                </select>
            </div>
            
            <div>
                <label for="prioridad" class="block mb-1 text-sm font-medium text-black">Prioridad</label>
                <select 
                    v-model="form.tiempoLibre.prioridad"
                    id="prioridad"
                    name="prioridad"
                    class="bg-gray-50 border-2 border-purple-600 text-gray-900 text-sm rounded-lg p-2.5 w-full appearance-none">
                    <option disabled value="">Selecciona una opción</option>
                    <option value="baja">Baja</option>
                    <option value="media">Media</option>
                    <option value="alta">Alta</option>
                </select>
            </div>
            
            <div class="col-span-2"> 
                <label for="descripcion" class="block mb-1 text-sm font-medium text-black">Descripción de la actividad</label>
                <textarea
                    v-model="form.tiempoLibre.descripcion"
                    id="descripcion"
                    name="descripcion"
                    class="block bg-gray-50 border-2 border-purple-600 text-gray-900 text-sm rounded-lg p-2.5 w-full h-32"
                    required
                ></textarea>
            </div>

            <div class="col-span-2 flex justify-center pt-4"> 
                <div class="w-80">
                    <label for="notificaciones" class="block mb-1 text-sm font-medium text-gray-700 text-center">
                        ¿Deseas activar las notificaciones?
                    </label>
                    <div class="flex items-center justify-center space-x-6 mt-2">
                        <label class="inline-flex items-center cursor-pointer">
                            <input 
                                v-model="form.tiempoLibre.notificaciones"
                                type="checkbox" 
                                id="notificaciones"
                                name="notificaciones"
                                class="sr-only peer"
                            >
                            <div class="relative w-11 h-6 bg-gray-200 rounded-full peer peer-focus:ring-4 peer-focus:ring-purple-300 dark:peer-focus:ring-purple-800 dark:bg-gray-700 peer-checked:after:translate-x-full rtl:peer-checked:after:-translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-0.5 after:start-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-purple-600"></div>
                        </label>
                        <div class="w-8 h-8"> 
                            <img :src="iconoCampana" alt="Icono Campana" class="w-full h-full" />
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-span-2 flex justify-center pt-8">
                <!-- Mensaje de error -->
                <div v-if="errorMessage" class="alert alert-error mb-4">
                    <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    <span>{{ errorMessage }}</span>
                </div>
                
                <button 
                    @click="navigateToSectionLeisure"
                    :disabled="loading"
                    class="bg-gradient-to-br from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 text-white font-bold py-2 w-full rounded-lg shadow-lg transition duration-300 transform"
                    :class="{
                        'bg-gray-400 cursor-not-allowed': loading,
                        'hover:scale-105': !loading
                    }"
                >
                    <span v-if="loading" class="loading loading-spinner loading-md"></span>
                    <span v-else>Agregar</span>
                </button>
            </div>
            
            <ModalBase 
                v-if="showSuccessModal" 
                title-prop="Registro agregado con éxito"
                confirm-button-text="Aceptar"
                icon-type="success" 
                @confirm="handleSuccessConfirm" 
                @cancel="handleSuccessConfirm"
            />
            
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import iconoCampana from '../assets/IconoCampana.png';
import ModalBase from '../components/modalBase.vue';
import { leisureService } from '../services/leisureService.js';

const router = useRouter();
const showSuccessModal = ref(false);
const loading = ref(false);
const errorMessage = ref('');

// Objeto del formulario — conectar al backend con form.value.tiempoLibre
const form = ref({
    tiempoLibre: {
        titulo: '',
        tipo: '',       
        fecha: '',
        hora: '',
        frecuencia: '',   
        prioridad: '',    
        descripcion: '',
        notificaciones: true,
    }
})

const goBack = () => {
    router.back();
};

const navigateToSectionLeisure = async () => {
    if (!form.value.tiempoLibre.titulo || !form.value.tiempoLibre.tipo || !form.value.tiempoLibre.prioridad) {
        errorMessage.value = 'Por favor completa los campos obligatorios';
        return;
    }
    
    loading.value = true;
    errorMessage.value = '';
    
    try {
        // Preparar datos para el backend
        const leisureData = {
            title: form.value.tiempoLibre.titulo,
            category: form.value.tiempoLibre.tipo,
            frequency: form.value.tiempoLibre.frecuencia,
            priority: form.value.tiempoLibre.prioridad,
            description: form.value.tiempoLibre.descripcion,
            due_date: form.value.tiempoLibre.fecha ? new Date(form.value.tiempoLibre.fecha).toISOString() : null
        };
        
        await leisureService.create(leisureData);
        showSuccessModal.value = true;
    } catch (error) {
        errorMessage.value = error.detail || 'Error al crear registro de tiempo libre';
        console.error('Error:', error);
    } finally {
        loading.value = false;
    }
};

const handleSuccessConfirm = () => {
    showSuccessModal.value = false;
    router.push('/tiempo-libre'); 
};
</script>