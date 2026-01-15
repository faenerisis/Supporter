<script setup>
import HealthCheck from './components/HealthCheck.vue'
</script>

<template>
  <div id="app">
    <header>
      <h1>🚀 Supporter Application</h1>
      <p>Frontend ↔️ Backend Connection Demo</p>
    </header>
    
    <HealthCheck />
  </div>
</template>

<style scoped>
#app {
  min-height: 100vh;
  background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
  padding: 2rem;
}

header {
  text-align: center;
  color: white;
  margin-bottom: 2rem;
}

header h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

header p {
  font-size: 1.2rem;
  opacity: 0.9;
}
</style>
