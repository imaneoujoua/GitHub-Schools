import { defineConfig } from 'vite';

export default defineConfig({
  root: 'src',
  server: {
    host: '0.0.0.0',
    port: 5173,
    open: false,
  },
  preview: {
    host: '0.0.0.0',
    port: 4173,
  },
  build: {
    outDir: '../dist',
    emptyOutDir: true,
  },
});
