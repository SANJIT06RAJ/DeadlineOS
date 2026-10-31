
import { useState } from 'react'
import { X } from 'lucide-react'

function AssignmentForm({
  initialData,
  onSubmit,
  onCancel,
  isEditing = false,
}) {
  const [formData, setFormData] = useState(() => ({
    title: initialData?.title ?? '',
    description: initialData?.description ?? '',
    due_date: initialData?.due_date ?? '',
    status: initialData?.status ?? 'pending',
  }))

  const [errors, setErrors] = useState({})

  function handleChange(event) {
    const { name, value } = event.target

    setFormData((current) => ({
      ...current,
      [name]: value,
    }))

    setErrors((current) => ({
      ...current,
      [name]: '',
    }))
  }

  function validateForm() {
    const newErrors = {}
    const trimmedTitle = formData.title.trim()

    if (!trimmedTitle) {
      newErrors.title = 'Assignment title is required.'
    } else if (trimmedTitle.length > 200) {
      newErrors.title = 'Title cannot exceed 200 characters.'
    }

    if (!['pending', 'in_progress', 'completed'].includes(formData.status)) {
      newErrors.status = 'Please select a valid status.'
    }

    setErrors(newErrors)

    return Object.keys(newErrors).length === 0
  }

  function handleSubmit(event) {
    event.preventDefault()

    if (!validateForm()) {
      return
    }

    onSubmit({
      title: formData.title.trim(),
      description: formData.description.trim() || null,
      due_date: formData.due_date || null,
      status: formData.status,
    })
  }

  return (
    <div className="assignment-form-overlay">
      <section
        className="assignment-form-modal"
        role="dialog"
        aria-modal="true"
        aria-labelledby="assignment-form-title"
      >
        <div className="assignment-form-header">
          <div>
            <h2 id="assignment-form-title">
              {isEditing ? 'Edit Assignment' : 'Create Assignment'}
            </h2>
            <p>
              {isEditing
                ? 'Update your assignment details.'
                : 'Add a new task to your academic workspace.'}
            </p>
          </div>

          <button
            type="button"
            className="form-close-button"
            onClick={onCancel}
            aria-label="Close form"
          >
            <X size={20} />
          </button>
        </div>

        <form onSubmit={handleSubmit} noValidate>
          <div className="form-field">
            <label htmlFor="title">
              Assignment Title <span>*</span>
            </label>

            <input
              id="title"
              name="title"
              type="text"
              value={formData.title}
              onChange={handleChange}
              maxLength={200}
              placeholder="e.g. Software Engineering Project"
              aria-invalid={Boolean(errors.title)}
              aria-describedby={errors.title ? 'title-error' : undefined}
            />

            {errors.title && (
              <small id="title-error" className="form-error">
                {errors.title}
              </small>
            )}
          </div>

          <div className="form-field">
            <label htmlFor="description">Description</label>

            <textarea
              id="description"
              name="description"
              value={formData.description}
              onChange={handleChange}
              rows={4}
              placeholder="Add assignment details or instructions..."
            />
          </div>

          <div className="form-field">
            <label htmlFor="due_date">Due Date</label>

            <input
              id="due_date"
              name="due_date"
              type="date"
              value={formData.due_date}
              onChange={handleChange}
            />
          </div>

          <div className="form-field">
            <label htmlFor="status">Status</label>

            <select
              id="status"
              name="status"
              value={formData.status}
              onChange={handleChange}
              aria-invalid={Boolean(errors.status)}
            >
              <option value="pending">Pending</option>
              <option value="in_progress">In Progress</option>
              <option value="completed">Completed</option>
            </select>

            {errors.status && (
              <small className="form-error">{errors.status}</small>
            )}
          </div>

          <div className="assignment-form-actions">
            <button
              type="button"
              className="form-cancel-button"
              onClick={onCancel}
            >
              Cancel
            </button>

            <button type="submit" className="form-submit-button">
              {isEditing ? 'Save Changes' : 'Create Assignment'}
            </button>
          </div>
        </form>
      </section>
    </div>
  )
}

export default AssignmentForm
