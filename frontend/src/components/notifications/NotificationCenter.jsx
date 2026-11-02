
import { useEffect, useMemo, useState } from 'react'
import {
  Bell,
  AlertCircle,
  CalendarClock,
  CheckCircle2,
  LoaderCircle,
} from 'lucide-react'
import { Link } from 'react-router-dom'
import { getAssignments } from '../../services/api'

function NotificationCenter() {
  const [assignments, setAssignments] = useState([])
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState('')
  const [isOpen, setIsOpen] = useState(false)

  useEffect(() => {
    async function loadNotifications() {
      try {
        const data = await getAssignments()
        setAssignments(data)
      } catch {
        setError('Unable to load reminders.')
      } finally {
        setIsLoading(false)
      }
    }

    loadNotifications()
  }, [])

  const notifications = useMemo(() => {
    return assignments
      .filter((assignment) => {
        if (!assignment.due_date || assignment.status === 'completed') {
          return false
        }

        return (
          assignment.is_overdue ||
          assignment.days_remaining === 0 ||
          (assignment.days_remaining > 0 &&
            assignment.days_remaining <= 7)
        )
      })
      .map((assignment) => {
        let type
        let message

        if (assignment.is_overdue) {
          type = 'overdue'
          message = `Overdue by ${Math.abs(assignment.days_remaining)} day(s)`
        } else if (assignment.days_remaining === 0) {
          type = 'today'
          message = 'Due today'
        } else {
          type = 'upcoming'
          message = `Due in ${assignment.days_remaining} day(s)`
        }

        return {
          ...assignment,
          type,
          message,
        }
      })
      .sort((a, b) => a.days_remaining - b.days_remaining)
  }, [assignments])

  const notificationCount = notifications.length

  return (
    <div className="notification-container">
      <button
        className="notification-button"
        type="button"
        aria-label={`Notifications, ${notificationCount} active reminders`}
        aria-expanded={isOpen}
        onClick={() => setIsOpen((current) => !current)}
      >
        <Bell size={20} />

        {notificationCount > 0 && (
          <span className="notification-count">
            {notificationCount > 99 ? '99+' : notificationCount}
          </span>
        )}
      </button>

      {isOpen && (
        <section
          className="notification-panel"
          aria-label="Deadline reminders"
        >
          <div className="notification-panel-header">
            <div>
              <h2>Notifications</h2>
              <p>{notificationCount} active reminder(s)</p>
            </div>

            <button
              type="button"
              className="notification-close"
              aria-label="Close notifications"
              onClick={() => setIsOpen(false)}
            >
              ×
            </button>
          </div>

          {isLoading ? (
            <div className="notification-state">
              <LoaderCircle size={20} className="loading-spinner" />
              <span>Loading reminders...</span>
            </div>
          ) : error ? (
            <div className="notification-state notification-error">
              {error}
            </div>
          ) : notifications.length === 0 ? (
            <div className="notification-state">
              <CheckCircle2 size={28} />
              <strong>You're all caught up!</strong>
              <span>No upcoming or overdue deadlines.</span>
            </div>
          ) : (
            <div className="notification-list">
              {notifications.map((notification) => {
                const Icon =
                  notification.type === 'overdue'
                    ? AlertCircle
                    : CalendarClock

                return (
                  <Link
                    to={`/assignments?assignment=${notification.id}`}
                    className={`notification-item notification-${notification.type}`}
                    key={notification.id}
                    onClick={() => setIsOpen(false)}
                  >
                    <Icon size={19} />

                    <div>
                      <strong>{notification.title}</strong>
                      <span>{notification.message}</span>
                    </div>
                  </Link>
                )
              })}
            </div>
          )}

          <Link
            to="/assignments"
            className="notification-footer"
            onClick={() => setIsOpen(false)}
          >
            View assignments
          </Link>
        </section>
      )}
    </div>
  )
}

export default NotificationCenter
