<template>
    <div class="relative overflow-x-auto shadow-xl sm:rounded-lg border border-purple-300">
        <table class="w-full text-sm text-left rtl:text-right text-gray-700">
            
            <!--columnas-->
            <thead class="text-xs text-white uppercase bg-blue-600">
                <tr>
                    <th scope="col" class="p-4 w-12"></th> 
                    
                    <th 
                        v-for="column in columns" 
                        :key="column.key" 
                        scope="col" 
                        class="px-6 py-3" 
                        :class="column.widthClass" 
                    >
                        {{ column.label }}
                    </th>

                    <th v-if="showActions" scope="col" class="px-6 py-3 text-center w-32">Acciones</th>
                </tr>
            </thead>
            
            <!--contenido-->
            <tbody>
                <tr 
                    v-for="item in data" 
                    :key="item.id" 
                    :class="[
                        'border-b border-gray-200 hover:bg-purple-100 transition duration-300',
                        item.completed ? 'bg-purple-50' : 'bg-white'
                    ]"
                >
                    <td class="w-4 p-4">
                        </td>

                    <td 
                        v-for="column in columns" 
                        :key="column.key" 
                        class="px-6 py-4"
                        :class="column.key === 'title' ? 'font-medium text-gray-900 whitespace-nowrap truncate max-w-xs' : ''"
                    >
                        <slot :name="`cell-${column.key}`" :item="item">
                            {{ item[column.key] }}
                        </slot>
                    </td>
                    
                    <td v-if="showActions" class="px-6 py-4 text-center space-x-6 whitespace-nowrap w-32">
                        <button @click="$emit('complete', item.id)" :class="[
                            'transition',
                            item.completed ? 'text-gray-600 hover:text-gray-800' : 'text-green-600 hover:text-green-800'
                        ]" :title="item.completed ? 'Desmarcar como completada' : 'Marcar como completada'">
                            <svg v-if="item.completed" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h10a8 8 0 018 8v2M3 10l6 6m-6-6l6-6"></path>
                            </svg>
                            <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                        </button>
                        <button v-if="!item.completed" @click="$emit('edit', item.id)" class="text-purple-600 hover:text-purple-800 transition ml-2" title="Editar">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path>
                            </svg>
                        </button>
                        <button v-if="!item.completed" @click="$emit('delete', item.id)" class="text-red-600 hover:text-red-800 transition ml-2" title="Eliminar">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                            </svg>
                        </button>
                    </td>
                </tr>
            </tbody>

        </table>
            <!--navegacion-->
            <nav class="flex items-center flex-wrap md:flex-row justify-between p-4 bg-white border-t border-gray-200" aria-label="Table navigation">
                <span class="text-sm font-normal text-gray-500 block w-full md:inline md:w-auto">
                    Página <span class="font-semibold text-gray-900">{{ currentPage }}</span> de <span class="font-semibold text-gray-900">{{ totalPages }}</span>
                </span>
                
                <ul class="inline-flex -space-x-px rtl:space-x-reverse text-sm h-8 mt-2 md:mt-0">
                    
                    <li>
                        <button 
                            @click="$emit('prev')"
                            :disabled="currentPage === 1"
                            class="flex items-center justify-center px-3 h-8 ms-0 leading-tight text-gray-500 bg-white border border-gray-300 rounded-s-lg hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed"
                        >
                            Anterior
                        </button>
                    </li>
                    
                    <li v-for="page in totalPages" :key="page">
                        <button 
                            @click="$emit('page-change', page)"
                            :aria-current="currentPage === page ? 'page' : undefined"
                            class="flex items-center justify-center px-3 h-8 leading-tight border border-gray-300 transition duration-150"
                            :class="{
                                'text-white bg-purple-600 hover:bg-purple-700 border-purple-600': currentPage === page,
                                'text-gray-500 bg-white hover:bg-gray-100': currentPage !== page
                            }"
                        >
                            {{ page }}
                        </button>
                    </li>
                    
                    <li>
                        <button 
                            @click="$emit('next')"
                            :disabled="currentPage === totalPages"
                            class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-e-lg hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed"
                        >
                            Siguiente
                        </button>
                    </li>
                </ul>
            </nav>

    </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

defineProps({
    data: { type: Array, required: true, default: () => [] },
    columns: { type: Array, required: true, default: () => [] },
    currentPage: { type: Number, required: true },
    totalPages: { type: Number, required: true },
    showActions: { type: Boolean, default: true },
});

defineEmits(['edit', 'delete', 'page-change', 'next', 'prev']);
</script>