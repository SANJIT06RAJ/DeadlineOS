
import { useEffect, useState } from 'react'
import { Plus, ClipboardList } from 'lucide-react'
import Header from '../components/layout/Header'
import AssignmentForm from '../components/assignments/AssignmentForm'
import {
  getAssignments,
  createAssignment,
} from '../services/api'

function AssignmentsPage() {
  const [isFormOpen, setIsFormOpen] = useState(false)
  const [assignments, setAssignments] = useState([])
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    async function loadAssignments() {
      try {
        setError('')
        const data = await getAssignments()
        setAssignments(data)
      } catch (error) {
        console.error('Failed to load assignments:', error)
        setError('Unable to load assignments. Please try again.')
      } finally {
        setIsLoading(false)
      }
    }

    loadAssignments()
  }, [])

  async function handleCreateAssignment(formData) {
    try {
      setError('')

      const newAssignment = await createAssignment(formData)

      setAssignments((current) => [...current, newAssignment])
      setIsFormOpen(false)
    } catch (error) {
      console.error('Failed to create assignment:', error)
      setError('Unable to create assignment. Please try again.')
    }
  }

  return (
    <>
      <Header
        title="Assignments"
        description="Manage your academic tasks and deadlines."
      />

      <div className="assignments-toolbar">
        <p>Keep track of your academic tasks.</p>

        <button
          type="button"
          className="create-assignment-button"
          onClick={() => setIsFormOpen(true)}
        >
          <Plus size={18} />
          Create Assignment
        </button>
      </div>

      {error && (
        <p className="form-error" role="alert">
          {error}
        </p>
      )}

      {isLoading ? (
        <p role="status">Loading assignments...</p>
      ) : assignments.length === 0 ? (
        <section className="empty-state">
          <div className="empty-state-icon">
            <ClipboardList size={30} />
          </div>

          <h2>Your assignments will appear here</h2>

          <p>
            Create your first assignment to start organizing your work.
          </p>
        </section>
      ) : (
        <section className="assignment-list">
          {assignments.map((assignment) => (
            <article className="assignment-card" key={assignment.id}>
              <div>
                <h3>{assignment.title}</h3>
                {assignment.description && <p>{assignment.description}</p>}
                <small>
                  Due date: {assignment.due_date || 'Not set'}
                </small>
              </div>

              <span className={`status-badge status-${assignment.status}`}>
                {assignment.status.replace('_', ' ')}
              </span>
            </article>
          ))}
        </section>
      )}

      {isFormOpen && (
        <AssignmentForm
          onSubmit={handleCreateAssignment}
          onCancel={() => setIsFormOpen(false)}
        />
      )}
    </>
  )
}

export default AssignmentsPage
