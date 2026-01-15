<template>
  <div class="health-check">
    <h2>🔗 Backend Connection Status</h2>
    
    <div v-if="loading" class="status loading">
      <span class="spinner">⏳</span>
      <p>Checking backend connection...</p>
    </div>
    
    <div v-else-if="error" class="status error">
      <span class="icon">❌</span>
      <p>{{ error }}</p>
    </div>
    
    <div v-else-if="healthData" class="status success">
      <span class="icon">✅</span>
      <h3>Backend Connected!</h3>
      <div class="details">
        <div class="detail-item">
          <strong>Status:</strong> {{ healthData.status }}
        </div>
        <div class="detail-item">
          <strong>Environment:</strong> <span class="env-badge">{{ healthData.env }}</span>
        </div>
        <div class="detail-item">
          <strong>Service:</strong> {{ healthData.service }}
        </div>
        <div class="detail-item">
          <strong>API URL:</strong> <code>{{ apiBaseUrl }}</code>
        </div>
      </div>
    </div>
    
    <button @click="checkHealth" class="refresh-btn">
      🔄 Refresh Connection
    </button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'
const healthData = ref(null)
const loading = ref(false)
const error = ref(null)

const checkHealth = async () => {
  loading.value = true
  error.value = null
  healthData.value = null
  
  try {
    console.log('🔍 Checking backend health at:', `${apiBaseUrl}/health`)
    const response = await axios.get(`${apiBaseUrl}/health`)
    healthData.value = response.data
    console.log('✅ Backend health check successful:', response.data)
  } catch (err) {
    error.value = `Failed to connect to backend: ${err.message}`
    console.error('❌ Backend health check failed:', err)
  } finally {
    loading.value = false
  }
}

// Check health on component mount
onMounted(() => {
  checkHealth()
})
</script>

<style scoped>
.health-check {
  max-width: 600px;
  margin: 2rem auto;
  padding: 2rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 16px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  color: white;
}

h2 {
  text-align: center;
  margin-bottom: 2rem;
  font-size: 1.8rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.status {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 12px;
  padding: 2rem;
  margin-bottom: 1.5rem;
  color: #333;
  text-align: center;
}

.status .icon,
.status .spinner {
  font-size: 3rem;
  display: block;
  margin-bottom: 1rem;
}

.status.loading {
  background: rgba(255, 255, 255, 0.9);
}

.status.error {
  background: rgba(255, 107, 107, 0.1);
  border: 2px solid #ff6b6b;
  color: #c92a2a;
}

.status.success {
  background: rgba(255, 255, 255, 0.95);
}

h3 {
  color: #2ecc71;
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
}

.details {
  text-align: left;
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  margin-top: 1rem;
}

.detail-item {
  padding: 0.75rem 0;
  border-bottom: 1px solid #e9ecef;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.detail-item:last-child {
  border-bottom: none;
}

.detail-item strong {
  color: #495057;
  min-width: 120px;
}

.env-badge {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-weight: bold;
  text-transform: uppercase;
  font-size: 0.85rem;
}

code {
  background: #e9ecef;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-family: 'Courier New', monospace;
  font-size: 0.9rem;
  color: #495057;
}

.refresh-btn {
  width: 100%;
  padding: 1rem;
  background: white;
  color: #667eea;
  border: none;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.refresh-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
  background: #f8f9fa;
}

.refresh-btn:active {
  transform: translateY(0);
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.loading .spinner {
  animation: spin 1s linear infinite;
}
</style>
