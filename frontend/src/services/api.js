import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
})

// Assignments

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

// Subtasks

export async function getSubtasks(assignmentId) {
  const response = await api.get(
    `/assignments/${assignmentId}/subtasks`
  )
  return response.data
}

export async function createSubtask(
  assignmentId,
  title,
  estimatedMinutes = null
) {
  const response = await api.post(
    `/assignments/${assignmentId}/subtasks`,
    {
      title,
      estimated_minutes: estimatedMinutes,
    }
  )

  return response.data
}

export async function updateSubtask(subtaskId, updates) {
  const response = await api.patch(
    `/subtasks/${subtaskId}`,
    updates
  )
  return response.data
}

export async function deleteSubtask(subtaskId) {
  const response = await api.delete(`/subtasks/${subtaskId}`)
  return response.data
}


export async function previewDocument(file) {
  const formData = new FormData()
  formData.append('file', file)

  const response = await api.post('/documents/preview', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  })

  return response.data
}

export async function extractAssignmentDetails(documentText) {
  const response = await api.post('/documents/extract', {
    document_text: documentText,
  })

  return response.data
}

export default api
