<template>
  <div class="form-container">
    <h2>Registro de Finanzas</h2>
    <form @submit.prevent="handleSubmit" aria-label="form-finanzas">
      <div>
        <label for="title">Título:</label>
        <input id="title" v-model="form.title" type="text" required />
      </div>
      <div>
        <label for="amount">Monto:</label>
        <input id="amount" v-model="form.amount" type="number" required />
      </div>
      <button type="submit">Guardar Registro</button>
    </form>
  </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue'
const emit = defineEmits(['save'])
const form = ref({ title: '', amount: 0, description: 'Finanza registrada' })
const handleSubmit = () => emit('save', { ...form.value })
</script>