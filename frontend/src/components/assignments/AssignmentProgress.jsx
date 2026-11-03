
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
  const [newEstimate, setNewEstimate] = useState('')
  const [estimateDrafts, setEstimateDrafts] = useState({})
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

          setEstimateDrafts(
            Object.fromEntries(
              data.map((subtask) => [
                subtask.id,
                subtask.estimated_minutes ?? '',
              ])
            )
          )
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

  const estimatedSubtasks = subtasks.filter(
    (subtask) => subtask.estimated_minutes !== null &&
      subtask.estimated_minutes !== undefined
  )

  const totalEstimatedMinutes = estimatedSubtasks.reduce(
    (total, subtask) => total + subtask.estimated_minutes,
    0
  )

  const completedEstimatedMinutes = estimatedSubtasks
    .filter((subtask) => subtask.is_completed)
    .reduce(
      (total, subtask) => total + subtask.estimated_minutes,
      0
    )

  const remainingEstimatedMinutes =
    totalEstimatedMinutes - completedEstimatedMinutes

  function formatWorkload(minutes) {
    const hours = Math.floor(minutes / 60)
    const remainingMinutes = minutes % 60

    if (hours === 0) return `${remainingMinutes} min`
    if (remainingMinutes === 0) return `${hours} hr`

    return `${hours} hr ${remainingMinutes} min`
  }

  async function handleAddSubtask(event) {
    event.preventDefault()

    const title = newTitle.trim()

    if (!title || isAdding) return

    const estimatedMinutes = newEstimate.trim()
      ? Number(newEstimate)
      : null

    if (
      estimatedMinutes !== null &&
      (!Number.isInteger(estimatedMinutes) || estimatedMinutes < 1)
    ) {
      setError('Estimate must be a positive whole number.')
      return
    }

    setIsAdding(true)
    setError('')

    try {
      const created = await createSubtask(
        assignmentId,
        title,
        estimatedMinutes
      )

      setSubtasks((current) => [...current, created])

      setEstimateDrafts((current) => ({
        ...current,
        [created.id]: created.estimated_minutes ?? '',
      }))

      setNewTitle('')
      setNewEstimate('')
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

  async function handleSaveEstimate(subtask) {
    if (busyIds.includes(subtask.id)) return

    const rawValue = estimateDrafts[subtask.id]
    const estimate = rawValue === '' ? null : Number(rawValue)

    if (
      estimate !== null &&
      (!Number.isInteger(estimate) || estimate < 1)
    ) {
      setError('Estimate must be a positive whole number.')
      return
    }

    if (estimate === (subtask.estimated_minutes ?? null)) return

    setBusyIds((current) => [...current, subtask.id])
    setError('')

    try {
      const updated = await updateSubtask(subtask.id, {
        estimated_minutes: estimate,
      })

      setSubtasks((current) =>
        current.map((item) =>
          item.id === subtask.id ? updated : item
        )
      )

      setEstimateDrafts((current) => ({
        ...current,
        [subtask.id]: updated.estimated_minutes ?? '',
      }))
    } catch (err) {
      console.error('Failed to update estimate:', err)
      setError('Unable to update the estimate. Please try again.')

      setEstimateDrafts((current) => ({
        ...current,
        [subtask.id]: subtask.estimated_minutes ?? '',
      }))
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

      setEstimateDrafts((current) => {
        const updated = { ...current }
        delete updated[subtaskId]
        return updated
      })
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

      {estimatedSubtasks.length > 0 ? (
        <div className="workload-summary">
          <strong>Estimated workload</strong>

          <div className="workload-details">
            <span>
              Total: {formatWorkload(totalEstimatedMinutes)}
            </span>

            <span>
              Completed: {formatWorkload(completedEstimatedMinutes)}
            </span>

            <span>
              Remaining: {formatWorkload(remainingEstimatedMinutes)}
            </span>
          </div>
        </div>
      ) : (
        <p className="no-workload-estimate">
          No workload estimates yet.
        </p>
      )}

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

              <input
                type="number"
                min="1"
                step="1"
                value={estimateDrafts[subtask.id] ?? ''}
                onChange={(event) =>
                  setEstimateDrafts((current) => ({
                    ...current,
                    [subtask.id]: event.target.value,
                  }))
                }
                onBlur={() => handleSaveEstimate(subtask)}
                onKeyDown={(event) => {
                  if (event.key === 'Enter') {
                    event.currentTarget.blur()
                  }
                }}
                placeholder="Minutes"
                aria-label={`Estimated minutes for ${subtask.title}`}
                disabled={busyIds.includes(subtask.id)}
              />

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

        <input
          type="number"
          min="1"
          step="1"
          value={newEstimate}
          onChange={(event) => setNewEstimate(event.target.value)}
          placeholder="Minutes"
          aria-label="Estimated minutes"
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
