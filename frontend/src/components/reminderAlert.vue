<template>
    <div 
        :id="'alert-' + section.replace(/\s/g, '-')" 
        class="p-4 mb-4 rounded-xl bg-[#F9ECEC] dark:text-black border border-purple-600 shadow-md flex justify-between items-center w-full max-w-lg hover:shadow-xl hover:shadow-purple-200 transition-all duration-300 cursor-pointer" 
        role="alert"
    >   
    <!--TextoRecordatorio-->
        <div class="flex-grow pr-4"> 
            
            <div class="flex items-start mb-1">
                <svg class="shrink-0 w-4 h-4 mt-0.5 me-2 text-purple-700" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
                </svg>
                <h3 class="text-base font-semibold text-gray-900 truncate">
                    {{ section }} - {{ description }}
                </h3>
            </div>
            
            <p class="mt-1 ml-6 text-sm text-red-600 font-medium">
                Vence: {{ formattedDueDate }}
            </p>
        </div>
        
    <!--ImagenCampana-->   
        <div class="flex-shrink-0">
            <img
              :src="iconoCampana"
              alt= "Icono Campana"
              class="w-8 h-8" />
        </div>

    </div>
</template>

<script setup>
import { defineProps, computed } from 'vue';
import iconoCampana from '../assets/IconoCampana.png'

const props = defineProps({
    section: {
        type: String,
        required: true,
        default: 'General'
    },
    description: {
        type: String,
        required: true,
        default: 'Recordatorio sin descripción'
    },
    dueDate: {
        type: [String, Date], 
        required: true
    }
});

const formattedDueDate = computed(() => {
    if (props.dueDate instanceof Date) {
        return props.dueDate.toLocaleDateString('es-ES', { 
            year: 'numeric', month: 'short', day: 'numeric' 
        });
    }
    return props.dueDate;
});
</script>