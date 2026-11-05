
import { describe, it, expect, vi } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import AssignmentForm from './AssignmentForm'

describe('AssignmentForm', () => {
  it('renders the create assignment form', () => {
    render(
      <AssignmentForm
        onSubmit={vi.fn()}
        onCancel={vi.fn()}
      />,
    )

    expect(
      screen.getByRole('heading', { name: 'Create Assignment' }),
    ).toBeInTheDocument()

    expect(
      screen.getByLabelText(/assignment title/i),
    ).toBeInTheDocument()

    expect(
      screen.getByRole('button', { name: 'Create Assignment' }),
    ).toBeInTheDocument()
  })

  it('shows an error when the title is empty', async () => {
    const user = userEvent.setup()
    const onSubmit = vi.fn()

    render(
      <AssignmentForm
        onSubmit={onSubmit}
        onCancel={vi.fn()}
      />,
    )

    await user.click(
      screen.getByRole('button', { name: 'Create Assignment' }),
    )

    expect(
      screen.getByText('Assignment title is required.'),
    ).toBeInTheDocument()

    expect(onSubmit).not.toHaveBeenCalled()
  })

  it('trims and submits valid assignment data', async () => {
    const user = userEvent.setup()
    const onSubmit = vi.fn()

    render(
      <AssignmentForm
        onSubmit={onSubmit}
        onCancel={vi.fn()}
      />,
    )

    await user.type(
      screen.getByLabelText(/assignment title/i),
      '  Software Engineering Project  ',
    )

    await user.type(
      screen.getByLabelText(/description/i),
      '  Complete the project report  ',
    )

    await user.selectOptions(
      screen.getByLabelText('Status'),
      'in_progress',
    )

    await user.selectOptions(
      screen.getByLabelText('Priority'),
      'high',
    )

    await user.click(
      screen.getByRole('button', { name: 'Create Assignment' }),
    )

    expect(onSubmit).toHaveBeenCalledWith({
      title: 'Software Engineering Project',
      description: 'Complete the project report',
      due_date: null,
      status: 'in_progress',
      priority: 'high',
    })
  })

  it('renders existing assignment data in edit mode', () => {
    render(
      <AssignmentForm
        initialData={{
          title: 'Database Assignment',
          description: 'Complete SQL exercises',
          due_date: '2026-11-20',
          status: 'in_progress',
          priority: 'high',
        }}
        onSubmit={vi.fn()}
        onCancel={vi.fn()}
        isEditing
      />,
    )

    expect(
      screen.getByRole('heading', { name: 'Edit Assignment' }),
    ).toBeInTheDocument()

    expect(screen.getByLabelText(/assignment title/i))
      .toHaveValue('Database Assignment')

    expect(screen.getByLabelText(/description/i))
      .toHaveValue('Complete SQL exercises')

    expect(screen.getByLabelText('Due Date'))
      .toHaveValue('2026-11-20')

    expect(screen.getByLabelText('Status'))
      .toHaveValue('in_progress')

    expect(screen.getByLabelText('Priority'))
      .toHaveValue('high')
  })

  it('calls onCancel when the cancel button is clicked', async () => {
    const user = userEvent.setup()
    const onCancel = vi.fn()

    render(
      <AssignmentForm
        onSubmit={vi.fn()}
        onCancel={onCancel}
      />,
    )

    await user.click(
      screen.getByRole('button', { name: 'Cancel' }),
    )

    expect(onCancel).toHaveBeenCalledOnce()
  })

  it('disables form controls while submitting', () => {
    render(
      <AssignmentForm
        onSubmit={vi.fn()}
        onCancel={vi.fn()}
        isSubmitting
      />,
    )

    expect(screen.getByLabelText(/assignment title/i))
      .toBeDisabled()

    expect(screen.getByRole('button', { name: /creating/i }))
      .toBeDisabled()

    expect(screen.getByRole('dialog'))
      .toHaveAttribute('aria-busy', 'true')
  })

  it('displays submission errors', () => {
    render(
      <AssignmentForm
        onSubmit={vi.fn()}
        onCancel={vi.fn()}
        submissionError="Unable to create assignment."
      />,
    )

    expect(
      screen.getByRole('alert'),
    ).toHaveTextContent('Unable to create assignment.')
  })
})
