import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// Detect environment variable for network access
const isNetwork = process.env.VITE_NETWORK === 'true'
console.log(isNetwork)

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    host: isNetwork ? '0.0.0.0' : 'localhost', // Allow network access if the environment variable is set
    port: 3000 // Use the port you prefer
  }
})
