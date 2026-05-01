<template> 
<section class="fixed inset-0 bg-purple-300/50 flex items-center justify-center z-50">
    <div class="w-full p-6 bg-white rounded-lg sm:max-w-xs sm:p-8 shadow-2xl bg-gradient-to-br from-blue-600 to-purple-600 dark:border-white">
        
        <div v-if="iconType === 'success'" class="mb-6 text-center">
             
             <img src="../assets/Success.png" 
                  alt="Éxito" 
                  class="w-20 h-20 mx-auto" 
             />
        </div>
    
    <!--texto-->      
        <h1 class="mb-5 text-xl font-bold leading-tight tracking-tight text-white md:text-2xl text-center">
            {{ titleProp }}
        </h1>
        
        <slot name="content-area"></slot>

    <!--botones-->  
        <div class="mt-4 space-y-4 lg:mt-5 md:space-y-5">
            
            <button 
                type="button" 
                @click="handleConfirm" 
                :class="confirmButtonClass"
            >
                {{ confirmButtonText }}
            </button>
            
            <button 
                v-if="cancelButtonText"
                type="button" 
                @click="handleCancel" 
                class="w-full text-black bg-white hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-400 font-medium rounded-lg text-sm px-5 py-2.5 text-center border border-gray-400"
            >
                {{ cancelButtonText }}
            </button>
        </div>
    </div>
</section>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
    titleProp: {
        type: String,
        required: true,
    },
    confirmButtonText: {
        type: String,
        default: 'Aceptar',
    },
    cancelButtonText: {
        type: String,
        default: '', 
    },
    confirmButtonClass: {
        type: String,
        default: 'w-full text-white bg-blue-600 hover:bg-blue-700 focus:ring-4 focus:outline-none focus:ring-blue-400 font-medium rounded-lg text-sm px-5 py-2.5 text-center transition duration-300', 
    },
    iconType: {
        type: String,
        default: '',
    }
});

const emit = defineEmits(['confirm', 'cancel']);

const handleConfirm = () => {
    emit('confirm'); 
};

const handleCancel = () => {
    emit('cancel'); 
};
</script>