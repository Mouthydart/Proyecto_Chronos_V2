/**
 * @vitest-environment jsdom
 */
import { describe, test, expect } from 'vitest'
import { mount } from '@vue/test-utils'

// Importamos los componentes subiendo un nivel desde 'tests'
import AcademyForm from '../AcademyForm.vue'
import FinanceForm from '../FinanceForm.vue'
import HealthForm from '../HealthForm.vue'
import LeisureForm from '../LeisureForm.vue'

describe('Suite de Validación de Formularios - Chronos V2', () => {

  test('Validar AcademyForm', async () => {
    const wrapper = mount(AcademyForm)
    await wrapper.find('#title').setValue('Laboratorio Vue')
    await wrapper.find('#subject').setValue('Sistemas')
    await wrapper.find('#priority').setValue('alta')
    await wrapper.find('form').trigger('submit.prevent')
    expect(wrapper.emitted()).toHaveProperty('save')
  })

  test('Validar FinanceForm', async () => {
    const wrapper = mount(FinanceForm)
    await wrapper.find('#title').setValue('Gastos')
    await wrapper.find('#amount').setValue(500)
    await wrapper.find('form').trigger('submit.prevent')
    expect(wrapper.emitted()).toHaveProperty('save')
  })

  test('Validar HealthForm', async () => {
    const wrapper = mount(HealthForm)
    await wrapper.find('#title').setValue('Cita Médica')
    await wrapper.find('#date').setValue('2026-06-01')
    await wrapper.find('form').trigger('submit.prevent')
    expect(wrapper.emitted()).toHaveProperty('save')
  })

  test('Validar LeisureForm', async () => {
    const wrapper = mount(LeisureForm)
    await wrapper.find('#title').setValue('Cine')
    await wrapper.find('#duration').setValue(2)
    await wrapper.find('form').trigger('submit.prevent')
    expect(wrapper.emitted()).toHaveProperty('save')
  })
})