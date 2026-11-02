
import { useEffect, useMemo, useState } from 'react'
import {
  Plus,
  ClipboardList,
  Search,
  LoaderCircle,
  X,
} from 'lucide-react'
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
  const [isSubmitting, setIsSubmitting] = useState(false)

  const [loadError, setLoadError] = useState('')
  const [createError, setCreateError] = useState('')
  const [successMessage, setSuccessMessage] = useState('')

  const [reloadKey, setReloadKey] = useState(0)
  const [searchQuery, setSearchQuery] = useState('')
  const [statusFilter, setStatusFilter] = useState('all')

  useEffect(() => {
    let isMounted = true

    async function loadAssignments() {
      setIsLoading(true)
      setLoadError('')

      try {
        const data = await getAssignments()

        if (isMounted) {
          setAssignments(data)
        }
      } catch (error) {
        console.error('Failed to load assignments:', error)

        if (isMounted) {
          setLoadError('Unable to load your assignments. Check your connection and try again.')
        }
      } finally {
        if (isMounted) {
          setIsLoading(false)
        }
      }
    }

    loadAssignments()

    return () => {
      isMounted = false
    }
  }, [reloadKey])

  async function handleCreateAssignment(formData) {
    setIsSubmitting(true)
    setCreateError('')
    setSuccessMessage('')

    try {
      const newAssignment = await createAssignment(formData)

      setAssignments((current) => [...current, newAssignment])
      setSearchQuery('')
      setStatusFilter('all')
      setIsFormOpen(false)
      setSuccessMessage('Assignment created successfully.')
    } catch (error) {
      console.error('Failed to create assignment:', error)
      setCreateError('Unable to create the assignment. Please try again.')
    } finally {
      setIsSubmitting(false)
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
          onClick={() => {
            setCreateError('')
            setIsFormOpen(true)
          }}
        >
          <Plus size={18} />
          Create Assignment
        </button>
      </div>

      {successMessage && (
        <div className="feedback-banner feedback-success" role="status">
          <span>{successMessage}</span>
          <button
            type="button"
            aria-label="Dismiss success message"
            onClick={() => setSuccessMessage('')}
          >
            <X size={18} />
          </button>
        </div>
      )}

      {!isLoading && !loadError && assignments.length > 0 && (
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
        <div className="loading-state" role="status" aria-live="polite">
          <LoaderCircle className="loading-spinner" size={24} />
          <span>Loading assignments...</span>
        </div>
      ) : loadError ? (
        <section className="empty-state error-state">
          <div className="empty-state-icon">
            <ClipboardList size={30} />
          </div>

          <h2>Couldn't load assignments</h2>
          <p>{loadError}</p>

          <button
            type="button"
            className="clear-filters-button"
            onClick={() => setReloadKey((current) => current + 1)}
          >
            Try again
          </button>
        </section>
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
          isSubmitting={isSubmitting}
          submissionError={createError}
        />
      )}
    </>
  )
}

export default AssignmentsPage
