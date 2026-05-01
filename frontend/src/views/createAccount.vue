<template>
   <div class="flex flex-col w-full min-h-screen bg-base-100 items-center mb-8 mt-8">

    <!--título-->
      <div
        class="inline-block text-8xl font-bold text-transparent bg-clip-text bg-linear-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 transition-all duration-300"
      >
        Chronos
      </div>

   <!--texto-->
      <div
        class="text-2xl font-bold text-black mt-4 mb-4 text-center text-shadow-lg"
      >
        Organiza tu vida en un solo lugar. <br>
        Planifica tus tareas, rutinas, finanzas y calendario fácilmente. <br>
        Todo bajo control, todos los días.
      </div>

    <!--línea-->
      <div class="h-1 bg-linear-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 w-full max-w-2xl mx-auto"></div>

    <!--Subtitulo-->
      <div
        class="mb-4 mt-8 inline-block text-4xl font-bold text-transparent bg-clip-text bg-linear-to-r from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400 transition-all duration-300"
      >
        Crear cuenta
      </div>

    <!--inputCorreo -->
      <form class="max-w-sm mt-6 mb-4">
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

      <!-- Campos adicionales -->
      <form class="max-w-sm mt-6 mb-4">
        <div class="relative mb-4">
          <input
            v-model="username"
            type="text"
            class="bg-gray-50 border-2 border-purple-600 text-gray-900 text-sm rounded-lg block w-full ps-4 p-2.5"
            placeholder="Nombre de usuario"
          />
        </div>
        <div class="relative">
          <input
            v-model="fullName"
            type="text"
            class="bg-gray-50 border-2 border-purple-600 text-gray-900 text-sm rounded-lg block w-full ps-4 p-2.5"
            placeholder="Nombre completo"
          />
        </div>
      </form>

    <!--alerta-->
      <div 
      :class="{'hidden': isInstitutionalEmail || email.length === 0}"
      class="flex items-center p-4  text-sm dark:bg-blue-600 dark:text-yellow-300 rounded-xl" role="alert">
          <svg class="shrink-0 inline w-4 h-4 me-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
            <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
          </svg>
          <span class="sr-only">Info</span>
          <div>
            <span class="font-medium">Advertencia! el correo debe ser de dominio (@estudiante.ibero.edu.co).</span>
          </div>
      </div>

    <!--inputContraseñas-->
      <div>
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

        <div class="max-w-sm mt-6">
            <div class="relative">
                <input
                    :type="showPassword ? 'text' : 'password'"
                    v-model="confirmPassword"
                    class="py-2.5 sm:py-3 ps-4 pe-10 block w-full border-2 border-purple-600 rounded-lg sm:text-sm"
                    placeholder="Confirme su contraseña"
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

   <!--alerta-->
        <div 
            v-if="password && confirmPassword && !passwordsMatch"
            class="flex items-center p-4 text-sm bg-red-100 text-red-800 dark:bg-red-300 rounded-xl mt-4" 
            role="alert"
            >
            <svg class="shrink-0 inline w-4 h-4 me-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
            </svg>
            <span class="sr-only">Advertencia</span>
            <div>
                <span class="font-medium">Error: Las contraseñas no coinciden.</span>
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
        
      </div>

    <!--botonesDeInicio-->  
      <div class="flex w-full">
        <div class="card bg-base-300 rounded-box grid grow place-items-center">
         <button
              type="button"
              :disabled="!canSubmit"
              @click="handleRegistration" 
              class="mt-16 inline-flex items-center justify-center text-white font-medium rounded-lg text-sm px-8 py-2.5 text-center w-64 transition-all duration-300"
              :class="{
                  'bg-gray-400 cursor-not-allowed shadow-none': !canSubmit,
                  'bg-gradient-to-br from-blue-600 to-purple-600 shadow-blue-500/50 hover:from-blue-700 hover:to-purple-700': canSubmit
              }"
          >
              <span v-if="loading" class="loading loading-spinner loading-md"></span>
              <span v-else>Registrarse</span>
        </button>

    <!--modalDeExito -->
        <el-dialog v-if="showSuccessModal"> 
          <dialog id="dialog" aria-labelledby="dialog-title" class="fixed inset-0 size-auto max-h-none max-w-none overflow-y-auto bg-transparent backdrop:bg-transparent" open> 
              <el-dialog-backdrop class="fixed inset-0 bg-gray-900/50 transition-opacity data-closed:opacity-0 data-enter:duration-300 data-enter:ease-out data-leave:duration-200 data-leave:ease-in"></el-dialog-backdrop>

                <div tabindex="0" class="flex min-h-full items-end justify-center p-4 text-center focus:outline-none sm:items-center sm:p-0">
                    <!--panel-->
                    <el-dialog-panel class="relative transform overflow-hidden rounded-lg bg-blue-600 text-left shadow-xl outline -outline-offset-1 outline-white/10 transition-all data-closed:translate-y-4 data-closed:opacity-0 data-enter:duration-300 data-enter:ease-out data-leave:duration-200 data-leave:ease-in sm:my-8 sm:w-full sm:max-w-lg data-closed:sm:translate-y-0 data-closed:sm:scale-95">
                        
                    <!--contenido-->
                        <div class="bg-blue-600 px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                            <div class="sm:flex sm:items-start">
                                
                    <!--iconoDeExito-->
                                <div class="mx-auto flex size-12 shrink-0 items-center justify-center rounded-full bg-teal-500/20 sm:mx-0 sm:size-10">
                                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true" class="size-6 text-teal-300">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75 11.25 15 15 9.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                                    </svg>
                                </div>

                     <!--texto-->
                                <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                                    <h3 id="dialog-title" class="text-base font-semibold text-white">¡Cuenta creada con éxito!</h3>
                                    <div class="mt-2">
                                        <p class="text-sm text-blue-200">Ya puedes iniciar sesión con tu correo y contraseña.</p>
                                    </div>
                                </div>
                            </div>
                        </div>

                    <!--pieDialogo-->
                        <div class="bg-blue-800 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6">
                    <!--botonIniciarSesion-->
                            <button type="button" @click="closeModalAndNavigate" command="close" commandfor="dialog" class="inline-flex w-full justify-center rounded-md bg-teal-500 px-3 py-2 text-sm font-semibold text-white hover:bg-teal-400 sm:ml-3 sm:w-auto">Iniciar sesión</button>
                        </div>
                    </el-dialog-panel>
                </div>
            </dialog>
        </el-dialog>
        </div>
        
        <div class="card bg-base-300 rounded-box grid grow place-items-center">
          <button
            type="button"
            @click="handleLogin" 
            class="mt-16 inline-flex items-center justify-center text-white font-medium rounded-lg text-sm px-8 py-2.5 text-center w-64 transition-all duration-300 bg-gradient-to-br from-blue-600 to-purple-600 hover:from-orange-600 hover:to-pink-400">
            Iniciar sesión
          </button>
        </div>
      </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import PasswordValidator from '../components/passwordValidator.vue'
import { authService } from '../services/authService.js'

const showPassword = ref(false)
const password = ref('')
const confirmPassword = ref('') 
const email = ref('')
const username = ref('')
const fullName = ref('')
const loading = ref(false)
const errorMessage = ref('')
const showSuccessModal = ref(false) 

const isInstitutionalEmail = computed(() => {
    if (!email.value) return false; 
    const regex = /^[\w.-]+@estudiante\.ibero\.edu\.co$/i
    return regex.test(email.value)
})

const passwordRequirementsValid = computed(() => ({
    minLength: password.value.length >= 8,
    lowercase: /[a-z]/.test(password.value),
    uppercase: /[A-Z]/.test(password.value),
    number: /\d/.test(password.value),
    special: /[!@#\$%\^&\*\?\.\,\;\:\(\)\-\_]/.test(password.value)
}))

const allPasswordValid = computed(() => {
    return Object.values(passwordRequirementsValid.value).every(isValid => isValid)
})

const passwordsMatch = computed(() => {
    return password.value === confirmPassword.value && password.value.length > 0;
})

const canSubmit = computed(() => {
    return isInstitutionalEmail.value && 
           allPasswordValid.value && 
           passwordsMatch.value && 
           username.value.trim() && 
           fullName.value.trim() &&
           !loading.value
})

const router = useRouter() 

const handleRegistration = async () => {
    if (!canSubmit.value) return
    
    loading.value = true
    errorMessage.value = ''
    
    try {
        await authService.register({
            email: email.value,
            username: username.value,
            full_name: fullName.value,
            password: password.value
        })
        
        showSuccessModal.value = true
    } catch (error) {
        errorMessage.value = error.detail || 'Error al crear cuenta. Intenta nuevamente.'
        console.error('Error de registro:', error)
    } finally {
        loading.value = false
    }
}

const handleLogin = () => {
    router.push('/')
}

const closeModalAndNavigate = () => {
    showSuccessModal.value = false; 
    router.push('/')
}
</script>