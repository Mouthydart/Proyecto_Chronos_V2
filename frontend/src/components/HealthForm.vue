<template>
  <div class="form-container">
    <h2>Registro de Salud</h2>
    <form @submit.prevent="handleSubmit" aria-label="form-salud">
      <div>
        <label for="title">Actividad/Síntoma:</label>
        <input id="title" v-model="form.title" type="text" required />
      </div>
      <div>
        <label for="date">Fecha:</label>
        <input id="date" v-model="form.date" type="date" required />
      </div>
      <button type="submit">Guardar Registro</button>
    </form>
  </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue'
const emit = defineEmits(['save'])
const form = ref({ title: '', date: '', description: 'Salud registrada' })
const handleSubmit = () => emit('save', { ...form.value })
</script>