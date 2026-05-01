<template>
  <div class="w-full min-h-screen relative flex flex-col items-center pt-8"> 
    
    <breadCrumbs class="absolute top-0 left-0 p-4" /> 
    
    <div
      class=" mt-16 mb-16 inline-block text-6xl font-bold text-transparent bg-clip-text bg-linear-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 transition-all duration-300">
      Chronos
    </div>

    <div class="max-w-5xl mx-auto mb-16 px-4 "> 
        <div
            class="text-3xl md:text-2xl font-bold text-gray-800">
            La plataforma integral de gestión personal diseñada para sincronizar todos los aspectos de tu vida en un único lugar.
        </div>
        <div
            class="text-sm md:text-base text-gray-500 mt-4">
            Su objetivo principal es transformar el caos en control, ofreciendo herramientas unificadas para dominar la organización personal, la planificación de tareas y la estabilidad financiera.
        </div>
    </div>

    <div class="flex justify-center w-full max-w-6xl px-4 gap-16">
      
      <div class="flex flex-col  w-1/3 p-6 bg-gray-50 rounded-xl shadow-lg mx-2 mb-8 transition duration-300 hover:shadow-xl items-start border border-gray-200"> 
        <div class="flex items-center justify-center w-full h-48 border-2 border-gray-300 rounded-lg bg-white">
          <img :src="knowUs1" alt="Imagen 1" class="w-full h-full rounded-lg" />
        </div>
        
        <div class="mt-4 text-center">
          <h3 class="text-xl font-semibold text-gray-800">Organización Avanzada</h3>
          <p class="mt-2 text-gray-500">
            Categoriza y prioriza todas tus tareas y proyectos de manera eficiente, creando una visión clara de tus metas.
          </p>
        </div>
      </div>
    <div class="flex flex-col  w-1/3 p-6 bg-gray-50 rounded-xl shadow-lg mx-2 mb-8 transition duration-300 hover:shadow-xl items-start border border-gray-200"> 
        <div class="flex items-center justify-center w-full h-48 border-2 border-gray-300 rounded-lg bg-white">
            <img :src="knowUs2" alt="Imagen 2" class="w-full h-full rounded-lg" />
        </div>
        
        <div class="mt-4 text-center">
          <h3 class="text-xl font-semibold  text-gray-800">Gestión de Tiempo</h3>
          <p class="mt-2 text-gray-500">
            Sincroniza tu calendario y finanzas para tener una visión 360° de tu día y tus metas a largo plazo.
          </p>
        </div>
      </div>
      
    <div class="flex flex-col  w-1/3 p-6 bg-gray-50 rounded-xl shadow-lg mx-2 mb-8 transition duration-300 hover:shadow-xl items-start border border-gray-200"> 
        <div class="flex items-center justify-center w-full h-48 border-2 border-gray-300 rounded-lg bg-white">
            <img :src="knowUs3" alt="Imagen 3" class="w-full h-full rounded-lg " />
        </div>
        
        <div class="mt-4 text-center">
          <h3 class="text-xl font-semibold  text-gray-800">Enfoque y Productividad</h3>
          <p class="mt-2 text-gray-500">
            Herramienta diseñada para ayudarte a mantener la concentración y maximizar tu rendimiento diario.
          </p>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>

import breadCrumbs from '../components/breadCrumbs.vue'
import knowUs1 from '../assets/KnowUs1.jpg';
import knowUs2 from '../assets/KnowUs2.jpg';
import knowUs3 from '../assets/KnowUs3.jpg';

</script>