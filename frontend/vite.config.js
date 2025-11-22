import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    watch: {
      usePolling: true, // ESSENCIAL para Docker no Windows
    },
    host: true, // Libera o acesso externo (0.0.0.0)
    strictPort: true,
    port: 5173,
  }
})