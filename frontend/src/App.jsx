import { BrowserRouter, Routes, Route } from 'react-router-dom'
import AppLayout from './components/layout/AppLayout'
import DashboardPage from './pages/DashboardPage'
import AssignmentsPage from './pages/AssignmentsPage'
import './App.css'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<AppLayout />}>
          <Route path="/" element={<DashboardPage />} />
          <Route path="/assignments" element={<AssignmentsPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App