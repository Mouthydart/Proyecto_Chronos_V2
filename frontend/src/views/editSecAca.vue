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
                {{ isEditing ? 'Editar registro' : 'Agregar registro' }}
            </div>
        </div>

    <!--formulario-->
        <form @submit.prevent="handleSubmit" class="grid grid-cols-2 gap-x-8 gap-y-4 p-4 mt-8 max-w-xl mx-auto">
            
            <div>
                <label for="titulo" class="block mb-1 text-sm font-medium text-black">Título de la actividad</label>
                <input 
                    v-model="formData.titulo"
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
                    v-model="formData.tipo"
                    id="tipo"
                    name="tipo"
                    class="bg-gray-50 border-2 border-purple-600 text-gray-900 text-sm rounded-lg p-2.5 w-full appearance-none">
                    <option disabled value="">Selecciona una opción</option>
                    <option value="tarea">Tarea</option>
                    <option value="examen">Examen</option>
                    <option value="proyecto">Proyecto</option>
                </select>
            </div>

            <div>
                <label for="fecha" class="block mb-1 text-sm font-medium text-black">Fecha</label>
                <input 
                    v-model="formData.fecha"
                    type="date" 
                    id="fecha"
                    name="fecha"
                    class="bg-gray-50 border-2 border-purple-600 text-gray-900 text-sm rounded-lg p-2.5 w-full appearance-none"
                />
            </div>

            <div>
                <label for="hora" class="block mb-1 text-sm font-medium text-black">Hora</label>
                <input 
                    v-model="formData.hora"
                    type="time" 
                    id="hora"
                    name="hora"
                    class="bg-gray-50 border-2 border-purple-600 text-gray-900 text-sm rounded-lg p-2.5 w-full appearance-none"
                />
            </div>

            <div>
                <label for="materia" class="block mb-1 text-sm font-medium text-black">Materia</label>
                <input 
                    v-model="formData.materia"
                    type="text" 
                    id="materia"
                    name="materia"
                    class="bg-gray-50 border-2 border-purple-600 text-gray-900 text-sm rounded-lg p-2.5 w-full" 
                    required 
                />
            </div>
            
            <div>
                <label for="prioridad" class="block mb-1 text-sm font-medium text-black">Prioridad</label>
                <select 
                    v-model="formData.prioridad"
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
                    v-model="formData.descripcion"
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
                                v-model="formData.notificaciones"
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
                <button 
                    type="submit"
                    class="bg-gradient-to-br from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 text-white font-bold py-2 w-full rounded-lg shadow-lg transition duration-300 transform"
                >
                    {{ isEditing ? 'Guardar Cambios' : 'Agregar' }}
                </button>
            </div>
        </form>

    <!--modal-->
        <ModalBase 
            v-if="showSuccessModal" 
            :title-prop="modalTitle"
            icon-type="success"
            confirm-button-text="Aceptar"
            @confirm="handleSuccessConfirm" 
            @cancel="handleSuccessConfirm"
        />

    </div>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router';
import { ref, onMounted } from 'vue';
import { academyService } from '../services/academyService.js';

import ModalBase from '../components/modalBase.vue';
import iconoCampana from '../assets/IconoCampana.png';

const router = useRouter();
const route = useRoute();

const showSuccessModal = ref(false);
const modalTitle = ref('');
const isEditing = ref(true);

// Objeto del formulario — conectar al backend con formData.value
const formData = ref({
    id: null,
    titulo: '',
    tipo: '',       
    fecha: '',
    hora: '',
    materia: '',
    prioridad: '',   
    descripcion: '',
    notificaciones: true, 
});

onMounted(async () => {
    const itemId = route.params.id;
    if (itemId) {
        try {
            const itemToEdit = await academyService.getById(itemId);
            
            if (itemToEdit) {
                formData.value = { ...itemToEdit };
            } else {
                console.error(`Registro con ID ${itemId} no encontrado.`);
                router.push('/estudio'); 
            }
        } catch (error) {
            console.error('Error al cargar el registro:', error);
            router.push('/estudio'); 
        }
    } else {
        router.push('/estudio'); 
    }
});

const handleSubmit = async () => {
    try {
        await academyService.update(formData.value.id, formData.value);
        modalTitle.value = '¡Registro actualizado con éxito!';
        showSuccessModal.value = true;
    } catch (error) {
        console.error('Error al actualizar el registro:', error);
        alert('Error al actualizar el registro: ' + (error.detail || error.message));
    }
};

const goBack = () => {
    router.back();
};

const handleSuccessConfirm = () => {
    showSuccessModal.value = false;
    router.push('/estudio'); 
};
</script>