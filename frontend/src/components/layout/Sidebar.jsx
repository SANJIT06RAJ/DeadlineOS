import { NavLink } from 'react-router-dom'
import {
  LayoutDashboard,
  ClipboardList,
  Settings,
  Clock,
} from 'lucide-react'

const navigation = [
  { name: 'Dashboard', path: '/', icon: LayoutDashboard },
  { name: 'Assignments', path: '/assignments', icon: ClipboardList },
]

function Sidebar() {
  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <div className="brand-icon">
          <Clock size={22} />
        </div>
        <div>
          <h2>DeadlineOS</h2>
          <span>STUDENT WORKSPACE</span>
        </div>
      </div>

      <div className="sidebar-section">
        <p className="sidebar-label">WORKSPACE</p>

        <nav className="sidebar-nav">
          {navigation.map(({ name, path, icon: Icon }) => (
            <NavLink
              key={path}
              to={path}
              end={path === '/'}
              className={({ isActive }) =>
                `nav-link ${isActive ? 'active' : ''}`
              }
            >
              <Icon size={19} />
              <span>{name}</span>
            </NavLink>
          ))}
        </nav>
      </div>

      <div className="sidebar-bottom">
        <div className="sidebar-user">
          <div className="user-avatar">N</div>
          <div>
            <strong>Student</strong>
            <span>Personal workspace</span>
          </div>
          <Settings size={18} />
        </div>
      </div>
    </aside>
  )
}

export default Sidebar