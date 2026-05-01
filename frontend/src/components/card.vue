<template>
    <router-link :to="to" 
        class="card bg-base-100 w-64 drop-shadow-2xl hover:ring-4 hover:ring-purple-600 transition-all duration-300 bg-purple-50 rounded-b-md"
    >
        <figure>
            <img
                :src="imageSrc"
                :alt="title + ' image'"
                class="w-full object-cover h-32" 
            />
        </figure>
        
        <div class="flex justify-center mt-4 mb-4">
            <h2 class="inline-block text-base font-semibold text-black text-shadow-2xl">{{ title }}</h2>
        </div>
    </router-link>
</template>

<script setup>
import { defineProps } from 'vue';

defineProps({
    title: {
        type: String,
        required: true
    },
    imageSrc: {
        type: String,
        required: true
    },
    to: {
        type: String,
        default: '#' // Ruta por defecto si no se especifica
    }
});
</script>