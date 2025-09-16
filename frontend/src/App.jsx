import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import Feed from './pages/Feed'
import Signup from './pages/Signup'
import Login from './pages/Login'
import Topic from './pages/Topic'
import Messages from './pages/Messages'

export default function App(){ return (
  <BrowserRouter>
    <header style={{display:'flex',gap:12,alignItems:'center',marginBottom:20}}>
      <h2 style={{margin:0}}>VibeMatch</h2>
      <nav style={{marginLeft:'auto'}}><Link to="/">Feed</Link>{" | "}<Link to="/signup">Signup</Link>{" | "}<Link to="/login">Login</Link></nav>
    </header>
    <Routes>
      <Route path="/" element={<Feed/>} />
      <Route path="/signup" element={<Signup/>} />
      <Route path="/login" element={<Login/>} />
      <Route path="/topic/:id" element={<Topic/>} />
      <Route path="/messages" element={<Messages/>} />
    </Routes>
  </BrowserRouter>
)}