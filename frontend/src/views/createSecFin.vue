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
                <label for="titulo" class="block mb-1 text-sm font-medium text-black">Título del registro</label>
                <input 
                    v-model="form.finanzas.titulo"
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
                    v-model="form.finanzas.tipo"
                    id="tipo"
                    name="tipo"
                    class="bg-gray-50 border-2 border-purple-600 text-gray-900 text-sm rounded-lg p-2.5 w-full appearance-none">
                    <option disabled value="">Selecciona una opción</option>
                    <option value="gasto">Gasto</option>
                    <option value="ingreso">Ingreso</option>
                    <option value="deuda">Deuda</option>
                    <option value="ahorro">Ahorro</option>
                </select>
            </div>

            <div>
                <label for="fecha" class="block mb-1 text-sm font-medium text-black">Fecha</label>
                <input 
                    v-model="form.finanzas.fecha"
                    type="date" 
                    id="fecha"
                    name="fecha"
                    class="bg-gray-50 border-2 border-purple-600 text-gray-900 text-sm rounded-lg p-2.5 w-full appearance-none"
                />
            </div>

            <div>
                <label for="hora" class="block mb-1 text-sm font-medium text-black">Hora</label>
                <input 
                    v-model="form.finanzas.hora"
                    type="time" 
                    id="hora"
                    name="hora"
                    class="bg-gray-50 border-2 border-purple-600 text-gray-900 text-sm rounded-lg p-2.5 w-full appearance-none"
                />
            </div>

            <div class="col-span-2">
                <label for="monto" class="block mb-1 text-sm font-medium text-black">Monto</label>
                <input 
                    type="text" 
                    id="monto"
                    name="monto"
                    class="bg-gray-50 border-2 border-purple-600 text-gray-900 text-sm rounded-lg p-2.5 w-full" 
                    required
                    v-model="amount" 
                    @input="formatCurrency" 
                    @blur="cleanForSubmit" 
                />
            </div>
            
            <div class="col-span-2"> 
                <label for="descripcion" class="block mb-1 text-sm font-medium text-black">Descripción del registro</label>
                <textarea
                    v-model="form.finanzas.descripcion"
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
                                v-model="form.finanzas.notificaciones"
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
                    @click="navigateToSectionFinance"
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
import { financeService } from '../services/financeService.js';

const router = useRouter();
const showSuccessModal = ref(false);
const loading = ref(false);
const errorMessage = ref('');

// Objeto del formulario — conectar al backend con form.value.finanzas
const form = ref({
    finanzas: {
        titulo: '',
        tipo: '',       
        fecha: '',
        hora: '',
        monto: 0,      
        descripcion: '',
        notificaciones: true,
    }
})

const amount = ref('');

const formatCurrency = () => {
    let value = amount.value.replace(/[^\d]/g, '');
    if (!value) {
        amount.value = '';
        return;
    }
    const numericValue = parseInt(value, 10) / 100;
    amount.value = new Intl.NumberFormat('es-CO', { 
        style: 'currency',
        currency: 'COP', 
        minimumFractionDigits: 2,
    }).format(numericValue);
};

const cleanForSubmit = () => {
    form.value.finanzas.monto = parseFloat(amount.value.replace(/[^\d]/g, '')) / 100;
};

const goBack = () => {
    router.back();
};

const navigateToSectionFinance = async () => {
    if (!form.value.finanzas.titulo || !form.value.finanzas.tipo || !amount.value) {
        errorMessage.value = 'Por favor completa los campos obligatorios';
        return;
    }
    
    loading.value = true;
    errorMessage.value = '';
    
    try {
        cleanForSubmit();
        
        // Preparar datos para el backend
        const financeData = {
            title: form.value.finanzas.titulo,
            type: form.value.finanzas.tipo,
            amount: form.value.finanzas.monto,
            category: 'otros', // Valor por defecto requerido por el backend
            priority: form.value.finanzas.prioridad || 'media', // Campo requerido
            description: form.value.finanzas.descripcion,
            due_date: form.value.finanzas.fecha ? new Date(form.value.finanzas.fecha).toISOString() : null
        };
        
        await financeService.create(financeData);
        showSuccessModal.value = true;
    } catch (error) {
        errorMessage.value = error.detail || 'Error al crear registro financiero';
        console.error('Error:', error);
    } finally {
        loading.value = false;
    }
};

const handleSuccessConfirm = () => {
    showSuccessModal.value = false;
    router.push('/finanzas'); 
};
</script>