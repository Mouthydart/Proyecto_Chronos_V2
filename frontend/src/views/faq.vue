<template>
  <div class="w-full min-h-screen relative flex flex-col items-center pt-8"> 
    
    <breadCrumbs class="absolute top-0 left-0 p-4" /> 
    
    <div
      class=" mt-16 inline-block text-6xl font-bold text-transparent bg-clip-text bg-linear-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 transition-all duration-300">
      Chronos
    </div>

  <section class="bg-white w-full flex justify-center">
      <div class="max-w-screen-xl w-full px-6 py-12 mx-auto">
          <div class="text-center mb-8">

              <h1 class="text-3xl md:text-4xl font-bold text-gray-800">Preguntas frecuentes</h1>

              <p class="text-sm md:text-base text-gray-500 mt-4 mb-8">Resuelve tus dudas sobre la gestión del tiempo y la plataforma.</p>
          </div>

          <section class="py-0"> <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">

                  <div class="space-y-4">

                      <details class="group border-b border-solid border-gray-200 py-4 px-6 rounded-lg transition-all duration-300 hover:bg-purple-50" open>
                          <summary class="flex justify-between items-center cursor-pointer text-gray-900 leading-8 transition duration-500 text-left group-open:text-purple-600 group-open:font-medium">
                              <h5>¿Qué metodología de gestión del tiempo utiliza Chronos?</h5>
                              <svg
                                  class="text-gray-500 transition duration-300 group-hover:text-purple-600 group-open:text-purple-600 group-open:rotate-180"
                                  width="22"
                                  height="22"
                                  viewBox="0 0 22 22"
                                  fill="none"
                                  xmlns="http://www.w3.org/2000/svg"
                              >
                                  <path
                                      d="M16.5 8.25L12.4142 12.3358C11.7475 13.0025 11.4142 13.3358 11 13.3358C10.5858 13.3358 10.2525 13.0025 9.58579 12.3358L5.5 8.25"
                                      stroke="currentColor"
                                      stroke-width="1.6"
                                      stroke-linecap="round"
                                      stroke-linejoin="round"
                                  ></path>
                              </svg>
                          </summary>
                          <div class="py-2 pl-4 pr-6">
                              <p class="text-base text-gray-700 leading-6 mt-2">
                                 Chronos se basa en la técnica Pomodoro, dividiendo tu estudio en bloques de enfoque profundo seguidos de breves descansos. Esto maximiza la concentración y previene el agotamiento mental.
                              </p>
                          </div>
                      </details>

                      <details class="group border-b border-solid border-gray-200 py-4 px-6 rounded-lg transition-all duration-300 hover:bg-purple-50">
                          <summary class="flex justify-between items-center cursor-pointer text-gray-900 leading-8 transition duration-500 text-left group-open:text-purple-600 group-open:font-medium">
                              <h5>¿Puedo usar Chronos para materias con diferentes niveles de dificultad?</h5>
                              <svg
                                  class="text-gray-500 transition duration-300 group-hover:text-purple-600 group-open:text-purple-600 group-open:rotate-180"
                                  width="22"
                                  height="22"
                                  viewBox="0 0 22 22"
                                  fill="none"
                                  xmlns="http://www.w3.org/2000/svg"
                              >
                                  <path
                                      d="M16.5 8.25L12.4142 12.3358C11.7475 13.0025 11.4142 13.3358 11 13.3358C10.5858 13.3358 10.2525 13.0025 9.58579 12.3358L5.5 8.25"
                                      stroke="currentColor"
                                      stroke-width="1.6"
                                      stroke-linecap="round"
                                      stroke-linejoin="round"
                                  ></path>
                              </svg>
                          </summary>
                          <div class="py-2 pl-4 pr-6">
                              <p class="text-base text-gray-700 leading-6 mt-2">
                                  Sí. Chronos te permite etiquetar y priorizar tareas por materia. Puedes asignar más bloques de tiempo Pomodoro a las asignaturas más complejas para asegurar una cobertura adecuada.
                              </p>
                          </div>
                      </details>

                      <details class="group border-b border-solid border-gray-200 py-4 px-6 rounded-lg transition-all duration-300 hover:bg-purple-50">
                          <summary class="flex justify-between items-center cursor-pointer text-gray-900 leading-8 transition duration-500 text-left group-open:text-purple-600 group-open:font-medium">
                              <h5>¿Chronos me ayuda a recordar fechas límite de exámenes y entregas?</h5>
                              <svg
                                  class="text-gray-500 transition duration-300 group-hover:text-purple-600 group-open:text-purple-600 group-open:rotate-180"
                                  width="22"
                                  height="22"
                                  viewBox="0 0 22 22"
                                  fill="none"
                                  xmlns="http://www.w3.org/2000/svg"
                              >
                                  <path
                                      d="M16.5 8.25L12.4142 12.3358C11.7475 13.0025 11.4142 13.3358 11 13.3358C10.5858 13.3358 10.2525 13.0025 9.58579 12.3358L5.5 8.25"
                                      stroke="currentColor"
                                      stroke-width="1.6"
                                      stroke-linecap="round"
                                      stroke-linejoin="round"
                                  ></path>
                              </svg>
                          </summary>
                          <div class="py-2 pl-4 pr-6">
                              <p class="text-base text-gray-700 leading-6 mt-2">
                                  Sí. Al crear una tarea o proyecto, puedes establecer una fecha límite (deadline). La aplicación te enviará notificaciones personalizadas para recordarte cuándo debes comenzar a trabajar y cuándo se acerca la fecha final.
                              </p>
                          </div>
                      </details>

                      <details class="group border-b border-solid border-gray-200 py-4 px-6 rounded-lg transition-all duration-300 hover:bg-purple-50">
                          <summary class="flex justify-between items-center cursor-pointer text-gray-900 leading-8 transition duration-500 text-left group-open:text-purple-600 group-open:font-medium">
                              <h5>¿Es mi información académica segura en Chronos?</h5>
                              <svg
                                  class="text-gray-500 transition duration-300 group-hover:text-purple-600 group-open:text-purple-600 group-open:rotate-180"
                                  width="22"
                                  height="22"
                                  viewBox="0 0 22 22"
                                  fill="none"
                                  xmlns="http://www.w3.org/2000/svg"
                              >
                                  <path
                                      d="M16.5 8.25L12.4142 12.3358C11.7475 13.0025 11.4142 13.3358 11 13.3358C10.5858 13.3358 10.2525 13.0025 9.58579 12.3358L5.5 8.25"
                                      stroke="currentColor"
                                      stroke-width="1.6"
                                      stroke-linecap="round"
                                      stroke-linejoin="round"
                                  ></path>
                              </svg>
                          </summary>
                          <div class="py-2 pl-4 pr-6">
                              <p class="text-base text-gray-700 leading-6 mt-2">
                                  Proteger tu información es nuestra prioridad número uno. Utilizamos cifrado de grado militar y servidores seguros para garantizar la privacidad total de tus datos.
                              </p>
                          </div>
                      </details>

                      <details class="group border-b border-solid border-gray-200 py-4 px-6 rounded-lg transition-all duration-300 hover:bg-purple-50">
                          <summary class="flex justify-between items-center cursor-pointer text-gray-900 leading-8 transition duration-500 text-left group-open:text-purple-600 group-open:font-medium">
                              <h5>¿Chronos está disponible para dispositivos móviles?</h5>
                              <svg
                                  class="text-gray-500 transition duration-300 group-hover:text-purple-600 group-open:text-purple-600 group-open:rotate-180"
                                  width="22"
                                  height="22"
                                  viewBox="0 0 22 22"
                                  fill="none"
                                  xmlns="http://www.w3.org/2000/svg"
                              >
                                  <path
                                      d="M16.5 8.25L12.4142 12.3358C11.7475 13.0025 11.4142 13.3358 11 13.3358C10.5858 13.3358 10.2525 13.0025 9.58579 12.3358L5.5 8.25"
                                      stroke="currentColor"
                                      stroke-width="1.6"
                                      stroke-linecap="round"
                                      stroke-linejoin="round"
                                  ></path>
                              </svg>
                          </summary>
                          <div class="py-2 pl-4 pr-6">
                              <p class="text-base text-gray-700 leading-6 mt-2">
                                Chronos está diseñado como una aplicación web de alto rendimiento accesible desde cualquier navegador moderno (Chrome, Firefox, Edge). Esto asegura que puedas acceder a tus datos y programar tu tiempo desde cualquier ordenador o dispositivo que soporte un navegador.
                              </p>
                          </div>
                      </details>
                      
                      <details class="group py-4 px-6 rounded-lg transition-all duration-300 hover:bg-purple-50">
                          <summary class="flex justify-between items-center cursor-pointer text-gray-900 leading-8 transition duration-500 text-left group-open:text-purple-600 group-open:font-medium">
                              <h5>¿Qué pasa si necesito soporte o ayuda con la planificación?</h5>
                              <svg
                                  class="text-gray-500 transition duration-300 group-hover:text-purple-600 group-open:text-purple-600 group-open:rotate-180"
                                  width="22"
                                  height="22"
                                  viewBox="0 0 22 22"
                                  fill="none"
                                  xmlns="http://www.w3.org/2000/svg"
                              >
                                  <path
                                      d="M16.5 8.25L12.4142 12.3358C11.7475 13.0025 11.4142 13.3358 11 13.3358C10.5858 13.3358 10.2525 13.0025 9.58579 12.3358L5.5 8.25"
                                      stroke="currentColor"
                                      stroke-width="1.6"
                                      stroke-linecap="round"
                                      stroke-linejoin="round"
                                  ></path>
                              </svg>
                          </summary>
                          <div class="py-2 pl-4 pr-6">
                              <p class="text-base text-gray-700 leading-6 mt-2">
                                  Nuestro equipo de soporte está disponible por correo electrónico de Lunes a Viernes. También tenemos una sección de guías y tutoriales dentro de la aplicación.
                              </p>
                          </div>
                      </details>

                  </div>
              </div>
          </section>


      </div>
  </section>

  </div>
</template>

<script setup>
import breadCrumbs from '../components/breadCrumbs.vue'
</script>