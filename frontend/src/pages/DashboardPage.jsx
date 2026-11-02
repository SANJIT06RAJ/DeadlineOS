
import { useEffect, useState } from 'react'
import {
  CalendarDays,
  CheckCircle2,
  CircleAlert,
  Clock3,
  ClipboardList,
  TrendingUp,
} from 'lucide-react'
import { Link } from 'react-router-dom'
import Header from '../components/layout/Header'
import {
  getAssignments,
  getAssignmentSummary,
} from '../services/api'

function DashboardPage() {
  const [summary, setSummary] = useState(null)
  const [upcomingAssignments, setUpcomingAssignments] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    async function loadDashboard() {
      try {
        setLoading(true)
        setError('')

        const [summaryData, assignmentsData] = await Promise.all([
          getAssignmentSummary(),
          getAssignments(),
        ])

        setSummary(summaryData)

        const upcoming = assignmentsData
          .filter(
            (assignment) =>
              assignment.due_date &&
              assignment.status !== 'completed' &&
              !assignment.is_overdue &&
              assignment.days_remaining >= 0,
          )
          .slice(0, 5)

        setUpcomingAssignments(upcoming)
      } catch (err) {
        setError(
          err.response?.data?.detail ||
            'Unable to load dashboard data. Please try again.',
        )
      } finally {
        setLoading(false)
      }
    }

    loadDashboard()
  }, [])

  const completionRate =
    summary && summary.total_assignments > 0
      ? Math.round(
          (summary.completed_assignments / summary.total_assignments) * 100,
        )
      : 0

  const statistics = [
    {
      label: 'Total Assignments',
      value: summary?.total_assignments ?? '--',
      description: 'All your assignments',
      icon: ClipboardList,
    },
    {
      label: 'Pending',
      value: summary?.pending_assignments ?? '--',
      description: 'Waiting to be started',
      icon: Clock3,
    },
    {
      label: 'Completed',
      value: summary?.completed_assignments ?? '--',
      description: 'Successfully finished',
      icon: CheckCircle2,
    },
    {
      label: 'Overdue',
      value: summary?.overdue_assignments ?? '--',
      description: 'Past their deadlines',
      icon: CircleAlert,
    },
  ]

  function formatDueDate(dateValue) {
    return new Date(`${dateValue}T00:00:00`).toLocaleDateString(
      undefined,
      {
        day: 'numeric',
        month: 'short',
        year: 'numeric',
      },
    )
  }

  return (
    <>
      <Header
        title="Dashboard"
        description="Stay organized and keep track of your academic progress."
      />

      <section className="welcome-section">
        <div>
          <span className="welcome-label">YOUR WORKSPACE</span>
          <h2>Welcome back!</h2>
          <p>Let's make today a productive one.</p>
        </div>

        <div className="welcome-decoration">
          <CalendarDays size={76} />
        </div>
      </section>

      <section className="dashboard-section">
        <div className="section-heading">
          <h2>Overview</h2>
          <span>Your academic summary</span>
        </div>

        {error && <p className="dashboard-error">{error}</p>}

        <div className="stats-grid">
          {statistics.map(({ label, value, description, icon: Icon }) => (
            <div className="stat-card" key={label}>
              <div className="stat-card-top">
                <span>{label}</span>
                <Icon size={19} />
              </div>

              <strong>{loading ? '--' : value}</strong>
              <small>{description}</small>
            </div>
          ))}
        </div>
      </section>

      <section className="dashboard-bottom-grid">
        <div className="dashboard-panel">
          <div className="panel-heading">
            <div>
              <h2>Upcoming Deadlines</h2>
              <p>Your next assignments to work on.</p>
            </div>
            <CalendarDays size={20} />
          </div>

          {loading ? (
            <div className="dashboard-placeholder">
              <span>Loading upcoming deadlines...</span>
            </div>
          ) : upcomingAssignments.length > 0 ? (
            <div className="upcoming-list">
              {upcomingAssignments.map((assignment) => (
                <div className="upcoming-item" key={assignment.id}>
                  <div>
                    <strong>{assignment.title}</strong>
                    <span>{formatDueDate(assignment.due_date)}</span>
                  </div>
                  <small>
                    {assignment.days_remaining === 0
                      ? 'Due today'
                      : `${assignment.days_remaining} day(s) left`}
                  </small>
                </div>
              ))}
            </div>
          ) : (
            <div className="dashboard-placeholder">
              <CalendarDays size={30} />
              <strong>No upcoming deadlines</strong>
              <span>Your upcoming assignments will appear here.</span>
            </div>
          )}

          <Link to="/assignments" className="panel-link">
            View assignments
          </Link>
        </div>

        <div className="dashboard-panel">
          <div className="panel-heading">
            <div>
              <h2>Work Progress</h2>
              <p>Your assignment completion overview.</p>
            </div>
            <TrendingUp size={20} />
          </div>

          <div className="progress-placeholder">
            <div className="progress-circle">
              <span>{loading ? '--%' : `${completionRate}%`}</span>
            </div>
            <strong>
              {loading ? 'Calculating progress...' : 'Completion rate'}
            </strong>
            <span>
              {summary
                ? `${summary.completed_assignments} of ${summary.total_assignments} assignments completed`
                : 'Progress will appear when data is available.'}
            </span>
          </div>
        </div>
      </section>
    </>
  )
}

export default DashboardPage
