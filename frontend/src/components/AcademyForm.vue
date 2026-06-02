/**
 * @vitest-environment jsdom
 */
import { describe, test, expect } from 'vitest'

<template>
  <div class="form-container">
    <h2>Registro Académico (Chronos V2)</h2>
    <form @submit.prevent="handleSubmit" aria-label="form-academia">
      <div>
        <label for="title">Título:</label>
        <input id="title" v-model="form.title" type="text" required />
      </div>

      <div>
        <label for="subject">Materia:</label>
        <input id="subject" v-model="form.subject" type="text" required />
      </div>

      <div>
        <label for="priority">Prioridad:</label>
        <select id="priority" v-model="form.priority">
          <option value="baja">Baja</option>
          <option value="media">Media</option>
          <option value="alta">Alta</option>
        </select>
      </div>

      <button type="submit">Guardar Registro</button>
    </form>
  </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue'

const emit = defineEmits(['save'])

const form = ref({
  title: '',
  subject: '',
  priority: 'media',
  description: 'Creado desde interfaz Vue'
})

const handleSubmit = () => {
  // Dispara el evento hacia el componente padre o el servicio de API
  emit('save', { ...form.value })
}
</script>