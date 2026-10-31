
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

const statistics = [
  {
    label: 'Total Assignments',
    value: '--',
    description: 'All your assignments',
    icon: ClipboardList,
  },
  {
    label: 'Pending',
    value: '--',
    description: 'Waiting to be started',
    icon: Clock3,
  },
  {
    label: 'Completed',
    value: '--',
    description: 'Successfully finished',
    icon: CheckCircle2,
  },
  {
    label: 'Overdue',
    value: '--',
    description: 'Past their deadlines',
    icon: CircleAlert,
  },
]

function DashboardPage() {
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

        <div className="stats-grid">
          {statistics.map(({ label, value, description, icon: Icon }) => (
            <div className="stat-card" key={label}>
              <div className="stat-card-top">
                <span>{label}</span>
                <Icon size={19} />
              </div>

              <strong>{value}</strong>
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
              <p>Keep an eye on your next tasks.</p>
            </div>
            <CalendarDays size={20} />
          </div>

          <div className="dashboard-placeholder">
            <CalendarDays size={30} />
            <strong>No deadline data yet</strong>
            <span>Your upcoming assignments will appear here.</span>
          </div>

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
              <span>--%</span>
            </div>
            <strong>Progress unavailable</strong>
            <span>Progress will be calculated when data is connected.</span>
          </div>
        </div>
      </section>
    </>
  )
}

export default DashboardPage
