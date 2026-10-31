import { Bell } from 'lucide-react'

function Header({ title, description }) {
  return (
    <header className="top-header">
      <div>
        <h1>{title}</h1>
        <p>{description}</p>
      </div>

      <button
        className="notification-button"
        type="button"
        aria-label="Notifications"
      >
        <Bell size={20} />
      </button>
    </header>
  )
}

export default Header