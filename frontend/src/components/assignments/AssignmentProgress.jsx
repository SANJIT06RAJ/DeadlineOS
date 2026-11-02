import { useEffect, useState } from 'react'
import {
  CheckCircle2,
  LoaderCircle,
  Plus,
  Trash2,
} from 'lucide-react'
import {
  getSubtasks,
  createSubtask,
  updateSubtask,
  deleteSubtask,
} from '../../services/api'

function AssignmentProgress({ assignmentId }) {
  const [subtasks, setSubtasks] = useState([])
  const [newTitle, setNewTitle] = useState('')
  const [isLoading, setIsLoading] = useState(true)
  const [isAdding, setIsAdding] = useState(false)
  const [busyIds, setBusyIds] = useState([])
  const [error, setError] = useState('')

  useEffect(() => {
    let isMounted = true

    async function loadSubtasks() {
      try {
        const data = await getSubtasks(assignmentId)

        if (isMounted) {
          setSubtasks(data)
        }
      } catch (err) {
        console.error('Failed to load subtasks:', err)

        if (isMounted) {
          setError('Unable to load progress. Please try again.')
        }
      } finally {
        if (isMounted) {
          setIsLoading(false)
        }
      }
    }

    loadSubtasks()

    return () => {
      isMounted = false
    }
  }, [assignmentId])

  const completedCount = subtasks.filter(
    (subtask) => subtask.is_completed
  ).length

  const progress = subtasks.length > 0
    ? Math.round((completedCount / subtasks.length) * 100)
    : 0

  async function handleAddSubtask(event) {
    event.preventDefault()

    const title = newTitle.trim()

    if (!title || isAdding) return

    setIsAdding(true)
    setError('')

    try {
      const created = await createSubtask(assignmentId, title)

      setSubtasks((current) => [...current, created])
      setNewTitle('')
    } catch (err) {
      console.error('Failed to create subtask:', err)
      setError('Unable to add this task. Please try again.')
    } finally {
      setIsAdding(false)
    }
  }

  async function handleToggleSubtask(subtask) {
    if (busyIds.includes(subtask.id)) return

    setBusyIds((current) => [...current, subtask.id])
    setError('')

    try {
      const updated = await updateSubtask(subtask.id, {
        is_completed: !subtask.is_completed,
      })

      setSubtasks((current) =>
        current.map((item) =>
          item.id === subtask.id ? updated : item
        )
      )
    } catch (err) {
      console.error('Failed to update subtask:', err)
      setError('Unable to update progress. Please try again.')
    } finally {
      setBusyIds((current) =>
        current.filter((id) => id !== subtask.id)
      )
    }
  }

  async function handleDeleteSubtask(subtaskId) {
    if (busyIds.includes(subtaskId)) return

    setBusyIds((current) => [...current, subtaskId])
    setError('')

    try {
      await deleteSubtask(subtaskId)

      setSubtasks((current) =>
        current.filter((item) => item.id !== subtaskId)
      )
    } catch (err) {
      console.error('Failed to delete subtask:', err)
      setError('Unable to delete this task. Please try again.')
    } finally {
      setBusyIds((current) =>
        current.filter((id) => id !== subtaskId)
      )
    }
  }

  if (isLoading) {
    return (
      <div className="progress-loading">
        <LoaderCircle className="loading-spinner" size={16} />
        Loading progress...
      </div>
    )
  }

  return (
    <div className="assignment-progress">
      <div className="progress-heading">
        <strong>Assignment progress</strong>
        <span>
          {completedCount}/{subtasks.length} completed
        </span>
      </div>

      <div
        className="assignment-progress-track"
        role="progressbar"
        aria-label="Assignment progress"
        aria-valuenow={progress}
        aria-valuemin={0}
        aria-valuemax={100}
      >
        <div
          className="assignment-progress-fill"
          style={{ width: `${progress}%` }}
        />
      </div>

      <span className="progress-percentage">
        {progress}% complete
      </span>

      {subtasks.length === 0 ? (
        <p className="no-subtasks">
          No subtasks yet. Add smaller tasks to track your progress.
        </p>
      ) : (
        <ul className="subtask-list">
          {subtasks.map((subtask) => (
            <li className="subtask-item" key={subtask.id}>
              <label>
                <input
                  type="checkbox"
                  checked={subtask.is_completed}
                  disabled={busyIds.includes(subtask.id)}
                  onChange={() => handleToggleSubtask(subtask)}
                />

                <span
                  className={
                    subtask.is_completed
                      ? 'subtask-completed'
                      : ''
                  }
                >
                  {subtask.title}
                </span>
              </label>

              <button
                type="button"
                className="subtask-delete-button"
                aria-label={`Delete ${subtask.title}`}
                disabled={busyIds.includes(subtask.id)}
                onClick={() => handleDeleteSubtask(subtask.id)}
              >
                <Trash2 size={15} />
              </button>
            </li>
          ))}
        </ul>
      )}

      <form className="subtask-form" onSubmit={handleAddSubtask}>
        <input
          type="text"
          value={newTitle}
          onChange={(event) => setNewTitle(event.target.value)}
          placeholder="Add a subtask..."
          maxLength={200}
          aria-label="New subtask title"
        />

        <button
          type="submit"
          disabled={!newTitle.trim() || isAdding}
        >
          <Plus size={16} />
          Add
        </button>
      </form>

      {error && (
        <p className="subtask-error" role="alert">
          {error}
        </p>
      )}

      {progress === 100 && subtasks.length > 0 && (
        <p className="subtask-success">
          <CheckCircle2 size={15} />
          All subtasks completed!
        </p>
      )}
    </div>
  )
}

export default AssignmentProgress
