<template>  
<section class="bg-gray-50 dark:bg-white">
  <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <div class="w-full p-6 bg-white rounded-lg dark:border md:mt-0 sm:max-w-md bg-gradient-to-br from-blue-600 to-purple-600 dark:border-white sm:p-8 shadow-lg">
        <!--título-->
          <h1 class="mb-1 text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white text-center">
              Se ha enviado el enlace de recuperación a tu correo
          </h1>
          <form class="mt-4 space-y-4 lg:mt-5 md:space-y-5" action="#">
        <!--iconoCandado-->
              <div>
                   <div class="flex-1 relative bg-transparent">
                        <img
                            :src="iconoContraRecuperada"
                            alt= "Icono Recuperar Contraseña"
                            class="mx-auto w-32 h-32 mb-4"
                        />
                    </div>
              </div>
        <!--botons-->     
              <button type="button" @click="handleLogin" class="w-full text-white bg-black hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center">Volver al sitio</button>
          </form>
      </div>
  </div>
</section>

</template>

<script setup>
import { useRouter } from 'vue-router' 
import iconoContraRecuperada from '../assets/IconoContraRecuperada.png'

const router = useRouter()

const handleLogin = () => {
    router.push('/')
}

</script>