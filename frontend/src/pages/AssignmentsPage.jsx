
import { useEffect, useMemo, useState } from 'react'
import { Plus, ClipboardList, Search } from 'lucide-react'
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
  const [searchQuery, setSearchQuery] = useState('')
  const [statusFilter, setStatusFilter] = useState('all')

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

  const filteredAssignments = useMemo(() => {
    const normalizedQuery = searchQuery.trim().toLowerCase()

    return assignments.filter((assignment) => {
      const matchesSearch =
        assignment.title.toLowerCase().includes(normalizedQuery) ||
        (assignment.description || '')
          .toLowerCase()
          .includes(normalizedQuery)

      const matchesStatus =
        statusFilter === 'all' || assignment.status === statusFilter

      return matchesSearch && matchesStatus
    })
  }, [assignments, searchQuery, statusFilter])

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

      {!isLoading && assignments.length > 0 && (
        <section className="assignment-filters">
          <div className="assignment-search">
            <Search size={18} />
            <input
              type="search"
              placeholder="Search assignments..."
              aria-label="Search assignments by title or description"
              value={searchQuery}
              onChange={(event) => setSearchQuery(event.target.value)}
            />
          </div>

          <select
            className="assignment-status-filter"
            aria-label="Filter assignments by status"
            value={statusFilter}
            onChange={(event) => setStatusFilter(event.target.value)}
          >
            <option value="all">All statuses</option>
            <option value="pending">Pending</option>
            <option value="in_progress">In Progress</option>
            <option value="completed">Completed</option>
          </select>
        </section>
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
      ) : filteredAssignments.length === 0 ? (
        <section className="empty-state">
          <div className="empty-state-icon">
            <Search size={30} />
          </div>

          <h2>No matching assignments</h2>

          <p>
            Try another search term or change the status filter.
          </p>

          <button
            type="button"
            className="clear-filters-button"
            onClick={() => {
              setSearchQuery('')
              setStatusFilter('all')
            }}
          >
            Clear filters
          </button>
        </section>
      ) : (
        <section className="assignment-list">
          {filteredAssignments.map((assignment) => (
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
