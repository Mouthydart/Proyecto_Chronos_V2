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
                    <option value="actividad-fisica">Actividad física</option>
                    <option value="entretenimiento">Entretenimiento</option>
                    <option value="lectura">Lectura</option>
                    <option value="social">Social</option>
                    <option value="bienestar">Bienestar</option>
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
                <label for="frecuencia" class="block mb-1 text-sm font-medium text-black">Frecuencia</label>
                <select 
                    v-model="formData.frecuencia"
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
    frecuencia: '',   
    prioridad: '',    
    descripcion: '',
    notificaciones: true, 
});

const leisureData = [
  { id: 1, titulo: 'Salir a caminar', tipo: 'actividad-fisica', descripcion: 'Caminar 30 minutos por el parque.', fecha: '2025-11-07', hora: '07:00', frecuencia: 'diaria', prioridad: 'media', notificaciones: true },
  { id: 2, titulo: 'Ver película pendiente', tipo: 'entretenimiento', descripcion: 'Ver la película que quedó a medias.', fecha: '2025-11-09', hora: '20:00', frecuencia: 'semanal', prioridad: 'baja', notificaciones: false },
  { id: 3, titulo: 'Jugar videojuegos', tipo: 'entretenimiento', descripcion: 'Disfrutar un rato libre jugando con amigos en línea.', fecha: '2025-11-10', hora: '19:00', frecuencia: 'semanal', prioridad: 'baja', notificaciones: false },
  { id: 4, titulo: 'Leer novela', tipo: 'lectura', descripcion: 'Avanzar un capítulo del libro antes de dormir.', fecha: '2025-11-08', hora: '22:00', frecuencia: 'dia-por-medio', prioridad: 'media', notificaciones: true },
  { id: 5, titulo: 'Tomar café con amigos', tipo: 'social', descripcion: 'Compartir un rato agradable con amigos.', fecha: '2025-11-11', hora: '15:00', frecuencia: 'quincenal', prioridad: 'alta', notificaciones: true },
  { id: 6, titulo: 'Ir al gimnasio', tipo: 'actividad-fisica', descripcion: 'Entrenamiento funcional durante una hora.', fecha: '2025-11-06', hora: '06:00', frecuencia: 'dia-por-medio', prioridad: 'alta', notificaciones: true },
  { id: 7, titulo: 'Meditar', tipo: 'bienestar', descripcion: 'Meditar 10 minutos en la mañana.', fecha: '2025-11-08', hora: '06:30', frecuencia: 'diaria', prioridad: 'alta', notificaciones: true },
  { id: 8, titulo: 'Día de desconexión', tipo: 'bienestar', descripcion: 'Pasar un día sin redes sociales ni trabajo.', fecha: '2025-11-16', hora: '', frecuencia: 'mensual', prioridad: 'alta', notificaciones: true },
];

onMounted(() => {
    const itemId = route.params.id;
    isEditing.value = !!itemId;

    if (itemId) {
        const numericId = parseInt(itemId);
        // Reemplazar con: const itemToEdit = await api.get(`/recordatorios/tiempo-libre/${numericId}`)
        const itemToEdit = leisureData.find(item => item.id === numericId);
        
        if (itemToEdit) {
            formData.value = { ...itemToEdit };
        } else {
            console.error(`Registro con ID ${itemId} no encontrado.`);
            router.push('/tiempo-libre'); 
        }
    } else {
        router.push('/tiempo-libre'); 
    }
});

const handleSubmit = () => {
    // Reemplazar con: await api.put(`/recordatorios/tiempo-libre/${formData.value.id}`, formData.value)
    console.log('Datos a actualizar:', formData.value)
    modalTitle.value = '¡Registro actualizado con éxito!';
    showSuccessModal.value = true;
};

const goBack = () => {
    router.back();
};

const handleSuccessConfirm = () => {
    showSuccessModal.value = false;
    router.push('/tiempo-libre'); 
};
</script>