import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  test: {
    globals: true,
    environment: 'jsdom',
  coverage: {
    provider: 'v8', 
    reporter: ['text', 'html', 'json-summary'],
    include: ['src/components/**/*.vue'],
      lean: true
  }
  }
  
})