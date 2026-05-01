<template>
  <div class="w-full min-h-screen relative flex flex-col items-center pt-8"> 
    
    <breadCrumbs class="absolute top-0 left-0 p-4" /> 
    
    <div
      class=" mt-16 inline-block text-6xl font-bold text-transparent bg-clip-text bg-linear-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 transition-all duration-300">
      Chronos
    </div>

  <section class="bg-white w-full flex justify-center">
      <div class="max-w-screen-xl w-full px-6 py-12 mx-auto">
          <div class="text-center mt-8">

              <h1 class="text-3xl md:text-4xl font-bold text-gray-800">Ponte en contacto con nosotros</h1>

              <p class="text-sm md:text-base text-gray-500 mt-4 mb-16">Nuestro equipo siempre está aquí para charlar.</p>
          </div>

          <div class="grid grid-cols-1 gap-12 mt-10 md:grid-cols-2 lg:grid-cols-3">
              
              <div class="bg-gray-50 p-6 rounded-xl shadow-lg transition duration-300 hover:shadow-xl items-start border border-gray-200 ">
                  <span class="inline-block p-3 text-purple-600 rounded-full bg-purple-100/80">
                      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                          stroke="currentColor" class="w-6 h-6">
                          <path stroke-linecap="round" stroke-linejoin="round"
                              d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75" />
                      </svg>
                  </span>

                  <h2 class="mt-4 text-lg font-medium text-gray-800 ">Email</h2>
                  <p class="mt-2 text-gray-500 ">Nuestro equipo está aquí para ayudar.</p>
                  <p class="mt-2 text-blue-600 ">jgueva22@estudiante.ibero.edu.co</p>
                  <p class="mt-2 text-blue-600 ">enunezhe@estudiante.ibero.edu.co</p>
              </div>

              <div class="bg-gray-50 p-6 rounded-xl shadow-lg transition duration-300 hover:shadow-xl items-start border border-gray-200 ">
                <span class="inline-block p-3 text-purple-600 rounded-full bg-purple-100/80 ">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                        stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z" />
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z" />
                    </svg>
                </span>

                <h2 class="mt-4 text-lg font-medium text-gray-800">Sede Central</h2>
                <p class="mt-2 text-gray-500 ">Nuestro centro de operaciones digitales.</p>
                <p class="mt-2 text-blue-600 ">Chronos App</p>
              </div>

              <div class="bg-gray-50 p-6 rounded-xl shadow-lg transition duration-300 hover:shadow-xl items-start border border-gray-200 ">
                  <span class="inline-block p-3 text-purple-600 rounded-full bg-purple-100/80 ">
                      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                          stroke="currentColor" class="w-6 h-6">
                          <path stroke-linecap="round" stroke-linejoin="round"
                              d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z" />
                      </svg>
                  </span>

                  <h2 class="mt-4 text-lg font-medium text-gray-800 ">Telefono</h2>
                  <p class="mt-2 text-gray-500 ">Lunes-viernes Desde 8am hasta 5pm.</p>
                  <p class="mt-2 text-blue-600 ">+57 311-234-6442</p>
                  <p class="mt-2 text-blue-600 ">+57 313-367-6162</p>
              </div>
          </div>
      </div>
  </section>

  </div>
</template>

<script setup>
import breadCrumbs from '../components/breadCrumbs.vue'
</script>