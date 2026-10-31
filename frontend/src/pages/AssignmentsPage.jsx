import { useState } from 'react'
import { Plus, ClipboardList } from 'lucide-react'
import Header from '../components/layout/Header'
import AssignmentForm from '../components/assignments/AssignmentForm'

function AssignmentsPage() {
  const [isFormOpen, setIsFormOpen] = useState(false)
  const [assignments, setAssignments] = useState([])

  function handleCreateAssignment(formData) {
    const newAssignment = {
      ...formData,
      id: Date.now(),
    }

    setAssignments((current) => [...current, newAssignment])
    setIsFormOpen(false)
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

      {assignments.length === 0 ? (
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