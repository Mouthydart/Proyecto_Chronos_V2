<template>
  <div class="flex w-full min-h-screen bg-base-100">
    
    <div class="flex-1 flex flex-col relative">

      <breadCrumbs class="absolute top-0 left-0 p-4" />
      
      <div class="flex-1 flex flex-col items-center p-8 mt-16">

        <div
          class="inline-block text-6xl font-bold text-transparent bg-clip-text bg-linear-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 transition-all duration-300"
        >
          Chronos
        </div>

        <div
          class="inline-block text-2xl font-bold text-black mt-8 mb-8 text-center text-shadow-lg"
        >
          Organiza tu vida en un solo lugar. Planifica tus tareas, rutinas, finanzas y calendario fácilmente.
          Todo bajo control, todos los días.
        </div>

        <div class="h-1 bg-linear-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 w-full max-w-xl mx-auto"></div>

        <form class="max-w-2xl mx-auto mt-16 mb-4">
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

        <div class="max-w-sm mt-6">
          <div class="relative">
            <input
              :type="showPassword ? 'text' : 'password'"
              v-model="password"
              class="py-2.5 sm:py-3 ps-4 pe-10 block w-full border-2 border-purple-600 rounded-lg sm:text-sm"
              placeholder="Ingrese su contraseña"
            />
            <button
              type="button"
              @click="showPassword = !showPassword"
              class="absolute inset-y-0 end-0 flex items-center z-20 px-3 text-blue-600 focus:outline-none"
            >
              <svg
                v-if="!showPassword"
                class="size-4"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                viewBox="0 0 24 24"
              >
                <path
                  d="M2 2l20 20M9.88 9.88a3 3 0 1 0 4.24 4.24M10.73 5.08A10.43 10.43 0 0 1 12 5c7 0 10 7 10 7a13.16 13.16 0 0 1-1.67 2.68M6.61 6.61A13.526 13.526 0 0 0 2 12s3 7 10 7a9.74 9.74 0 0 0 5.39-1.61"
                />
              </svg>
              <svg
                v-else
                class="size-4"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                viewBox="0 0 24 24"
              >
                <path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z" />
                <circle cx="12" cy="12" r="3" />
              </svg>
            </button>
          </div>
        </div>

        <PasswordValidator :password="password" />

        <!-- Mensaje de error -->
        <div v-if="errorMessage" class="alert alert-error mt-4 max-w-md mx-auto">
          <svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <span>{{ errorMessage }}</span>
        </div>

        <div class="flex w-full mt-6">
          <div class="card bg-base-300 rounded-box grid grow place-items-center">
            <router-link to="/createAccount" class="link hover:underline text-[#2A00FF] font-semibold">
              Crear Cuenta
            </router-link>
          </div>
          <div class="card bg-base-300 rounded-box grid grow place-items-center">
            <router-link to="/forgotPassword" class="link hover:underline text-[#2A00FF] font-semibold">
              Recuperar Contraseña
            </router-link>
          </div>
        </div>

        <button
        type="button"
        :disabled="!canSubmit"
        
        @click="login" 
        
        class="mt-16 inline-flex items-center justify-center text-white font-medium rounded-lg text-sm px-8 py-2.5 text-center w-64 transition-all duration-300"
        :class="{
          'bg-gray-400 cursor-not-allowed': !canSubmit,
          'bg-gradient-to-br from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400': canSubmit
        }"
      >
        <span v-if="loading" class="loading loading-spinner loading-md"></span>
        <span v-else>Ingresar</span>
        <svg
          v-if="!loading"
          class="w-3.5 h-3.5 ms-2"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 14 10"
        >
          <path
            stroke="currentColor"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M1 5h12m0 0L9 1m4 4L9 9"
          />
        </svg>
        </button>
      </div>

    </div>

    <div class="flex-1 relative bg-gray-200">
      <img
        :src="imagenLogin"
        alt="Logo Chronos"
        class="absolute inset-0 w-full h-full object-cover"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router' 
import imagenLogin from '../assets/ImagenLogin.jpg'
import PasswordValidator from '../components/passwordValidator.vue'
import breadCrumbs from '../components/breadCrumbs.vue'
import { authService } from '../services/authService.js'

const showPassword = ref(false)
const password = ref('')
const email = ref('') 
const loading = ref(false)
const errorMessage = ref('')

const isInstitutionalEmail = computed(() => {
    if (!email.value) return false; 
    const regex = /^[\w.-]+@estudiante\.ibero\.edu\.co$/i
    return regex.test(email.value)
})

const validations = computed(() => ({
    minLength: password.value.length >= 8,
    lowercase: /[a-z]/.test(password.value),
    uppercase: /[A-Z]/.test(password.value),
    number: /\d/.test(password.value),
    special: /[!@#\$%\^&\*\?\.\,\;\:\(\)\-\_]/.test(password.value)
}))

const allPasswordValid = computed(() => {
    return Object.values(validations.value).every(isValid => isValid)
})

const canSubmit = computed(() => {
    return isInstitutionalEmail.value && allPasswordValid.value && !loading.value
})

const router = useRouter() 

const login = async () => {
    if (!canSubmit.value) return
    
    loading.value = true
    errorMessage.value = ''
    
    try {
        await authService.login({
            email: email.value,
            password: password.value
        })
        
        // Redirigir al home después del login exitoso
        router.push('/home')
    } catch (error) {
        errorMessage.value = error.detail || 'Error al iniciar sesión. Verifica tus credenciales.'
        console.error('Error de login:', error)
    } finally {
        loading.value = false
    }
}
</script>