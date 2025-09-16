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
    </header>import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import Signup from "./pages/Signup";
import Login from "./pages/Login";
import Feed from "./pages/Feed";

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gradient-to-br from-blue-200 via-indigo-200 to-purple-200 text-gray-800">
        {/* Navbar */}
        <nav className="bg-white shadow-md p-4 flex justify-between items-center">
          <Link to="/" className="text-xl font-bold text-indigo-600">
            VibeMatch 💜
          </Link>
          <div className="space-x-4">
            <Link to="/signup" className="hover:underline">Signup</Link>
            <Link to="/login" className="hover:underline">Login</Link>
            <Link to="/feed" className="hover:underline">Feed</Link>
          </div>
        </nav>

        {/* Page Content */}
        <div className="p-6">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />
            <Route path="/feed" element={<Feed />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;

    <Routes>
      <Route path="/" element={<Feed/>} />
      <Route path="/signup" element={<Signup/>} />
      <Route path="/login" element={<Login/>} />
      <Route path="/topic/:id" element={<Topic/>} />
      <Route path="/messages" element={<Messages/>} />
    </Routes>
  </BrowserRouter>
)}
