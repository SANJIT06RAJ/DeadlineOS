import NotificationCenter from '../notifications/NotificationCenter'

function Header({ title, description }) {
  return (
    <header className="top-header">
      <div>
        <h1>{title}</h1>
        <p>{description}</p>
      </div>

      <NotificationCenter />
    </header>
  )
}

export default Header