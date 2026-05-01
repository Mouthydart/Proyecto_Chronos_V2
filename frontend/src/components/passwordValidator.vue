<template>
  <div class=" mb-8 space-y-2">

    <!--barra-->
    <div class="h-1.5 bg-gray-200 rounded-full overflow-hidden mt-4">
      <div
        class="h-full transition-all duration-500"
        :class="barColor"
        :style="{ width: `${(Object.values(validations).filter(v => v).length / 5) * 100}%` }"
      ></div>
    </div>

    <!--nivel-->
    <div class="text-sm font-semibold mt-2">
      Nivel de seguridad:
      <span :class="textColor">
        {{ strengthLabel }}
      </span>
    </div>

    <!--listaDeValidaciones-->
    <div
      v-for="(ok, rule) in validations"
      :key="rule"
      class="flex items-center gap-2 text-sm transition-all duration-300"
      :class="ok ? 'text-green-600' : 'text-gray-400'"
    >
      <span
        class="flex h-5 w-5 items-center justify-center rounded-full border transition-all duration-300"
        :class="ok ? 'bg-green-100 border-green-500 text-green-600' : 'bg-gray-100 border-gray-300 text-gray-400'"
      >
        <svg
          v-if="ok"
          xmlns="http://www.w3.org/2000/svg"
          class="h-3.5 w-3.5"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          stroke-width="3"
        >
          <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
        </svg>
        <svg
          v-else
          xmlns="http://www.w3.org/2000/svg"
          class="h-3.5 w-3.5"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          stroke-width="3"
        >
          <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </span>

      <span>
        {{
          rule === 'minLength' ? 'Al menos 10 caracteres' :
          rule === 'lowercase' ? 'Al menos una letra minúscula' :
          rule === 'uppercase' ? 'Al menos una letra mayúscula' :
          rule === 'number' ? 'Al menos un número' :
          'Al menos un carácter especial (ej. ! @ # ?)'
        }}
      </span>
    </div>

  </div>
</template>

<script setup>
import { computed } from 'vue'

// Recibe la contraseña desde el componente padre
const props = defineProps({
  password: {
    type: String,
    required: true
  }
})

// Validaciones
const validations = computed(() => ({
  minLength: props.password.length >= 10,
  lowercase: /[a-z]/.test(props.password),
  uppercase: /[A-Z]/.test(props.password),
  number: /\d/.test(props.password),
  special: /[!@#\$%\^&\*\?\.\,\;\:\(\)\-\_]/.test(props.password)
}))

// Nivel de seguridad
const strengthLabel = computed(() => {
  const count = Object.values(validations.value).filter(v => v).length
  if (count <= 2) return 'Débil'
  if (count === 3 || count === 4) return 'Medio'
  return 'Fuerte'
})

// Colores dinámicos
const barColor = computed(() => {
  if (strengthLabel.value === 'Débil') return 'bg-red-500'
  if (strengthLabel.value === 'Medio') return 'bg-yellow-400'
  return 'bg-green-500'
})

const textColor = computed(() => {
  if (strengthLabel.value === 'Débil') return 'text-red-500'
  if (strengthLabel.value === 'Medio') return 'text-yellow-500'
  return 'text-green-600'
})
</script>
