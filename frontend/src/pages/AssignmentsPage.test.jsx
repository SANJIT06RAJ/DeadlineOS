import { describe, it, expect, vi, beforeEach } from 'vitest'
import {
  render,
  screen,
  waitFor,
  within,
} from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { MemoryRouter } from 'react-router-dom'

import AssignmentsPage from './AssignmentsPage'
import {
  getAssignments,
  createAssignment,
} from '../services/api'

vi.mock('../services/api', () => ({
  getAssignments: vi.fn(),
  createAssignment: vi.fn(),
}))

vi.mock('../components/layout/Header', () => ({
  default: ({ title, description }) => (
    <header>
      <h1>{title}</h1>
      <p>{description}</p>
    </header>
  ),
}))

vi.mock('../components/assignments/AssignmentProgress', () => ({
  default: () => null,
}))

vi.mock('../components/assignments/DocumentUploader', () => ({
  default: () => null,
}))

const mockAssignments = [
  {
    id: 1,
    title: 'Database Assignment',
    description: 'Complete SQL exercises',
    due_date: '2026-11-15',
    status: 'pending',
    priority: 'high',
    is_overdue: false,
    days_remaining: 9,
  },
  {
    id: 2,
    title: 'Software Engineering Project',
    description: 'Build a project using React',
    due_date: '2026-11-20',
    status: 'in_progress',
    priority: 'medium',
    is_overdue: false,
    days_remaining: 14,
  },
  {
    id: 3,
    title: 'Networking Report',
    description: 'Research network security',
    due_date: '2026-11-25',
    status: 'completed',
    priority: 'low',
    is_overdue: false,
    days_remaining: 19,
  },
]

function renderPage() {
  return render(
    <MemoryRouter>
      <AssignmentsPage />
    </MemoryRouter>,
  )
}

describe('AssignmentsPage', () => {
  beforeEach(() => {
    vi.clearAllMocks()
    getAssignments.mockResolvedValue(mockAssignments)
  })

  it('loads and displays assignments from the API', async () => {
    renderPage()

    expect(
      screen.getByText('Loading assignments...'),
    ).toBeInTheDocument()

    expect(
      await screen.findByText('Database Assignment'),
    ).toBeInTheDocument()

    expect(
      screen.getByText('Software Engineering Project'),
    ).toBeInTheDocument()

    expect(getAssignments).toHaveBeenCalledOnce()
  })

  it('searches assignments by title or description', async () => {
    const user = userEvent.setup()

    renderPage()

    await screen.findByText('Database Assignment')

    const searchInput = screen.getByRole('searchbox', {
      name: 'Search assignments by title or description',
    })

    await user.type(searchInput, 'network security')

    expect(
      screen.getByText('Networking Report'),
    ).toBeInTheDocument()

    expect(
      screen.queryByText('Database Assignment'),
    ).not.toBeInTheDocument()

    expect(
      screen.queryByText('Software Engineering Project'),
    ).not.toBeInTheDocument()
  })

  it('filters assignments by status', async () => {
    const user = userEvent.setup()

    renderPage()

    await screen.findByText('Database Assignment')

    await user.selectOptions(
      screen.getByRole('combobox', {
        name: 'Filter assignments by status',
      }),
      'in_progress',
    )

    expect(
      screen.getByText('Software Engineering Project'),
    ).toBeInTheDocument()

    expect(
      screen.queryByText('Database Assignment'),
    ).not.toBeInTheDocument()

    expect(
      screen.queryByText('Networking Report'),
    ).not.toBeInTheDocument()
  })

  it('creates an assignment and displays a success message', async () => {
    const user = userEvent.setup()

    const newAssignment = {
      id: 4,
      title: 'Testing Assignment',
      description: 'Write frontend tests',
      due_date: '2026-11-30',
      status: 'pending',
      priority: 'high',
      is_overdue: false,
      days_remaining: 24,
    }

    createAssignment.mockResolvedValue(newAssignment)

    renderPage()

    await screen.findByText('Database Assignment')

    // Open the assignment form.
    await user.click(
      screen.getByRole('button', {
        name: 'Create Assignment',
      }),
    )

    const dialog = screen.getByRole('dialog')

    // Fill in the form.
    await user.type(
      within(dialog).getByLabelText(/assignment title/i),
      'Testing Assignment',
    )

    await user.type(
      within(dialog).getByRole('textbox', {
        name: 'Description',
      }),
      'Write frontend tests',
    )

    await user.selectOptions(
      within(dialog).getByLabelText('Priority'),
      'high',
    )

    // Submit using the button inside the dialog.
    await user.click(
      within(dialog).getByRole('button', {
        name: 'Create Assignment',
      }),
    )

    await waitFor(() => {
      expect(createAssignment).toHaveBeenCalledWith({
        title: 'Testing Assignment',
        description: 'Write frontend tests',
        due_date: null,
        status: 'pending',
        priority: 'high',
      })
    })

    expect(
      await screen.findByText('Testing Assignment'),
    ).toBeInTheDocument()

    expect(
      screen.getByText('Assignment created successfully.'),
    ).toBeInTheDocument()
  })

  it('displays an error when assignments fail to load', async () => {
    getAssignments.mockRejectedValue(
      new Error('Network error'),
    )

    const consoleError = vi
      .spyOn(console, 'error')
      .mockImplementation(() => {})

    renderPage()

    expect(
      await screen.findByText("Couldn't load assignments"),
    ).toBeInTheDocument()

    expect(
      screen.getByRole('button', { name: 'Try again' }),
    ).toBeInTheDocument()

    consoleError.mockRestore()
  })

  it('retries loading assignments after a failure', async () => {
    const user = userEvent.setup()

    getAssignments
      .mockRejectedValueOnce(new Error('Network error'))
      .mockResolvedValueOnce(mockAssignments)

    const consoleError = vi
      .spyOn(console, 'error')
      .mockImplementation(() => {})

    renderPage()

    await screen.findByText("Couldn't load assignments")

    await user.click(
      screen.getByRole('button', { name: 'Try again' }),
    )

    expect(
      await screen.findByText('Database Assignment'),
    ).toBeInTheDocument()

    expect(getAssignments).toHaveBeenCalledTimes(2)

    consoleError.mockRestore()
  })
})
