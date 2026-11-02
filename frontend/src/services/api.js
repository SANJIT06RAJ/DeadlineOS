
import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
})

export async function getAssignments() {
  const response = await api.get('/assignments')
  return response.data
}

export async function getAssignmentSummary() {
  const response = await api.get('/assignments/summary')
  return response.data
}

export async function createAssignment(assignmentData) {
  const response = await api.post('/assignments', assignmentData)
  return response.data
}

export default api
