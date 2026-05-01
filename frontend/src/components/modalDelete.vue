<template> 
<section class="fixed inset-0 bg-purple-300/50 flex items-center justify-center z-50">
    <div class="w-full p-6 bg-white rounded-lg sm:max-w-xs sm:p-8 shadow-2xl bg-gradient-to-br from-blue-600 to-purple-600 dark:border-white">
        
    <!--texto-->    
        <h1 class="mb-5 text-xl font-bold leading-tight tracking-tight text-white md:text-2xl text-center">
            ¿Desea eliminar el registro seleccionado?
        </h1>

    <!--botones-->     
        <div class="mt-4 flex space-x-4">
            
            <button 
                type="button" 
                @click="cancelAction" 
                class="flex-1 text-gray-800 bg-white hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-400 font-medium rounded-lg text-sm px-5 py-2.5 text-center border border-gray-400 transition duration-300"
            >
                No
            </button>
            
            <button 
                type="button" 
                @click="confirmAction" 
                class="flex-1 text-white bg-red-600 hover:bg-red-700 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center transition duration-300"
            >
                Si
            </button>
        </div>
        
    </div>
</section>
</template>

<script setup>
import { defineEmits } from 'vue';

const emit = defineEmits(['confirm', 'cancel']); 

const confirmAction = () => {
    emit('confirm'); 
};

const cancelAction = () => {
    emit('cancel');
};
</script>