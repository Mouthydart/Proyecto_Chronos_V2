<template>  
<section class="bg-gray-50 dark:bg-white">
  <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <div class="w-full p-6 bg-white rounded-lg dark:border md:mt-0 sm:max-w-md bg-gradient-to-br from-blue-600 to-purple-600 dark:border-white sm:p-8 shadow-lg">
         <!--Titulo-->
          <h1 class="mb-1 text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
              ¿Olvidaste tu contraseña?
          </h1>
          <p class="font-light text-white">No te preocupes, ingresa tu correo para restablecerla</p>
          <form class="mt-4 space-y-4 lg:mt-5 md:space-y-5" action="#">
              <div>
                   <!--iconoCandado-->
                   <div class="flex-1 relative bg-transparent">
                        <img
                            :src="iconoRecuperarContra"
                            alt= "Icono Recuperar Contraseña"
                            class="mx-auto w-32 h-32 mb-4"
                        />
                    </div>
                  <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Correo registrado</label>
                    <!--inputCorreo-->
                   <form class="max-w-2xl mx-auto mb-4">
                        <div class="relative">
                            <div class="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none">
                                <svg
                                    class="w-4 h-4 text-blue-600"
                                    aria-hidden="true"
                                    xmlns="http://www.w3.org/2000/svg"
                                    fill="currentColor"
                                    viewBox="0 0 20 16"
                                    >
                                <path
                                    d="m10.036 8.278 9.258-7.79A1.979 1.979 0 0 0 18 0H2A1.987 1.987 0 0 0 .641.541l9.395 7.737Z"
                                />
                                <path
                                    d="M11.241 9.817c-.36.275-.801.425-1.255.427-.428 0-.845-.138-1.187-.395L0 2.6V14a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V2.5l-8.759 7.317Z"
                                />
                                </svg>
                            </div>
                            <input
                                v-model="email"
                                type="text"
                                id="email-address-icon"
                                class="bg-gray-50 border-2 border-purple-600 text-gray-900 text-sm rounded-lg block w-full ps-10 p-2.5"
                                placeholder="@estudiante.ibero.edu.co"
                            />
                        </div>
                    </form>
                     <!--alerta-->
                    <div 
                        :class="{'hidden': isInstitutionalEmail || email.length === 0}"
                        class="flex items-center p-4 mb-4 text-sm dark:bg-blue-600 dark:text-yellow-300 rounded-xl" role="alert">
                            <svg class="shrink-0 inline w-4 h-4 me-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                            <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
                            </svg>
                            <span class="sr-only">Info</span>
                            <div>
                            <span class="font-medium">Advertencia! el correo debe ser de dominio (@estudiante.ibero.edu.co).</span>
                            </div>
                    </div>
              </div>
              <!--botonRestablecerContra-->
              <button
                    type="submit"
                    @click="handleModal"
                    :disabled="!isInstitutionalEmail" 
                    class="w-full font-medium rounded-lg text-sm px-5 py-2.5 text-center transition-all duration-300"
                    :class="{
                        'bg-gray-400 text-white cursor-not-allowed shadow-none': !isInstitutionalEmail,  
                        'text-white bg-black hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300': isInstitutionalEmail
                    }"
                >
                    Restablecer contraseña
              </button>
              <!--botonVolver-->
              <button type="button" @click="handleLogin" class="w-full text-white bg-black hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center">Volver al sitio</button>
          </form>
      </div>
  </div>
</section>

</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router' 
import iconoRecuperarContra from '../assets/IconoRecuperarContra.png'

const email = ref('') 
const router = useRouter()
const isInstitutionalEmail = computed(() => {
    if (!email.value) return false; 
    const regex = /^[\w.-]+@estudiante\.ibero\.edu\.co$/i
    return regex.test(email.value)
})
const handleLogin = () => {
    router.push('/')
}
const handleModal = () => {
    router.push('/modalPassword')
}

</script>