<template>
  <div class="form-container">
    <h2>Registro de Ocio</h2>
    <form @submit.prevent="handleSubmit" aria-label="form-ocio">
      <div>
        <label for="title">Actividad:</label>
        <input id="title" v-model="form.title" type="text" required />
      </div>
      <div>
        <label for="duration">Duración (horas):</label>
        <input id="duration" v-model="form.duration" type="number" />
      </div>
      <button type="submit">Guardar Registro</button>
    </form>
  </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue'
const emit = defineEmits(['save'])
const form = ref({ title: '', duration: 0, description: 'Ocio registrado' })
const handleSubmit = () => emit('save', { ...form.value })
</script>