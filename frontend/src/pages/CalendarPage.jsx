import { useEffect, useMemo, useState } from 'react'
import {
  CalendarDays,
  ChevronLeft,
  ChevronRight,
  ClipboardList,
  LoaderCircle,
} from 'lucide-react'
import Header from '../components/layout/Header'
import { getAssignments } from '../services/api'

function formatDateKey(date) {
  const year = date.getFullYear()
  const month = String(date.getMonth() + 1).padStart(2, '0')
  const day = String(date.getDate()).padStart(2, '0')

  return `${year}-${month}-${day}`
}

function getMonday(date) {
  const monday = new Date(date)
  const day = monday.getDay()
  const difference = day === 0 ? -6 : 1 - day

  monday.setDate(monday.getDate() + difference)
  monday.setHours(0, 0, 0, 0)

  return monday
}

function getDeadlineClass(assignment) {
  if (assignment.status === 'completed') {
    return 'deadline-completed'
  }

  if (assignment.is_overdue) {
    return 'deadline-overdue'
  }

  if (assignment.days_remaining === 0) {
    return 'deadline-today'
  }

  return 'deadline-upcoming'
}

function CalendarPage() {
  const [assignments, setAssignments] = useState([])
  const [isLoading, setIsLoading] = useState(true)
  const [loadError, setLoadError] = useState('')
  const [reloadKey, setReloadKey] = useState(0)
  const [selectedWeek, setSelectedWeek] = useState(() => new Date())

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
        console.error('Failed to load calendar assignments:', error)

        if (isMounted) {
          setLoadError(
            'Unable to load your assignments. Check your connection and try again.'
          )
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

  const weekDays = useMemo(() => {
    const monday = getMonday(selectedWeek)

    return Array.from({ length: 7 }, (_, index) => {
      const date = new Date(monday)
      date.setDate(monday.getDate() + index)

      return {
        date,
        dateKey: formatDateKey(date),
        dayName: date.toLocaleDateString('en', {
          weekday: 'short',
        }),
        dayNumber: date.getDate(),
      }
    })
  }, [selectedWeek])

  const assignmentsByDate = useMemo(() => {
    const grouped = {}

    assignments.forEach((assignment) => {
      if (!assignment.due_date) return

      if (!grouped[assignment.due_date]) {
        grouped[assignment.due_date] = []
      }

      grouped[assignment.due_date].push(assignment)
    })

    return grouped
  }, [assignments])

  const datedAssignmentCount = useMemo(
    () => assignments.filter((assignment) => assignment.due_date).length,
    [assignments]
  )

  const weekLabel = useMemo(() => {
    const firstDay = weekDays[0].date
    const lastDay = weekDays[6].date

    const firstMonth = firstDay.toLocaleDateString('en', {
      month: 'short',
    })

    const lastMonth = lastDay.toLocaleDateString('en', {
      month: 'short',
      year: 'numeric',
    })

    if (firstDay.getMonth() === lastDay.getMonth()) {
      return `${firstMonth} ${firstDay.getDate()} – ${lastDay.getDate()}, ${firstDay.getFullYear()}`
    }

    return `${firstDay.toLocaleDateString('en', {
      month: 'short',
      day: 'numeric',
    })} – ${lastMonth} ${lastDay.getDate()}`
  }, [weekDays])

  function changeWeek(amount) {
    setSelectedWeek((current) => {
      const next = new Date(current)
      next.setDate(next.getDate() + amount * 7)
      return next
    })
  }

  function goToToday() {
    setSelectedWeek(new Date())
  }

  const todayKey = formatDateKey(new Date())

  return (
    <>
      <Header
        title="Calendar"
        description="View your academic deadlines throughout the week."
      />

      <section className="calendar-toolbar">
        <div className="calendar-week-navigation">
          <button
            type="button"
            className="calendar-nav-button"
            onClick={() => changeWeek(-1)}
            aria-label="Previous week"
          >
            <ChevronLeft size={19} />
          </button>

          <h2>{weekLabel}</h2>

          <button
            type="button"
            className="calendar-nav-button"
            onClick={() => changeWeek(1)}
            aria-label="Next week"
          >
            <ChevronRight size={19} />
          </button>
        </div>

        <button
          type="button"
          className="calendar-today-button"
          onClick={goToToday}
        >
          Today
        </button>
      </section>

      {isLoading ? (
        <div className="loading-state" role="status" aria-live="polite">
          <LoaderCircle className="loading-spinner" size={24} />
          <span>Loading calendar...</span>
        </div>
      ) : loadError ? (
        <section className="empty-state error-state">
          <div className="empty-state-icon">
            <CalendarDays size={30} />
          </div>

          <h2>Couldn't load calendar</h2>
          <p>{loadError}</p>

          <button
            type="button"
            className="clear-filters-button"
            onClick={() => setReloadKey((current) => current + 1)}
          >
            Try again
          </button>
        </section>
      ) : datedAssignmentCount === 0 ? (
        <section className="empty-state">
          <div className="empty-state-icon">
            <ClipboardList size={30} />
          </div>

          <h2>No scheduled deadlines yet</h2>
          <p>
            Assignments with due dates will appear on your weekly calendar.
          </p>
        </section>
      ) : (
        <>
          <div className="calendar-grid">
            {weekDays.map((day) => {
              const dayAssignments = assignmentsByDate[day.dateKey] || []
              const isToday = day.dateKey === todayKey

              return (
                <section
                  className={`calendar-day ${isToday ? 'calendar-day-today' : ''}`}
                  key={day.dateKey}
                  aria-label={`${day.dayName}, ${day.dateKey}`}
                >
                  <div className="calendar-day-header">
                    <span>{day.dayName}</span>
                    <strong>{day.dayNumber}</strong>
                    {isToday && (
                      <small className="calendar-today-label">TODAY</small>
                    )}
                  </div>

                  <div className="calendar-day-assignments">
                    {dayAssignments.length > 0 ? (
                      dayAssignments.map((assignment) => (
                        <article
                          className={`calendar-assignment ${getDeadlineClass(assignment)}`}
                          key={assignment.id}
                        >
                          <strong>{assignment.title}</strong>

                          <span
                            className={`priority-badge priority-${assignment.priority || 'medium'}`}
                          >
                            {(assignment.priority || 'medium').toUpperCase()}
                          </span>

                          <small className="calendar-assignment-status">
                            {assignment.status.replace('_', ' ')}
                          </small>
                        </article>
                      ))
                    ) : (
                      <p className="calendar-empty-day">No deadlines</p>
                    )}
                  </div>
                </section>
              )
            })}
          </div>

          <p className="calendar-footer">
            Showing {datedAssignmentCount} assignment(s) with due dates.
            Completed assignments remain visible.
          </p>
        </>
      )}
    </>
  )
}

export default CalendarPage
