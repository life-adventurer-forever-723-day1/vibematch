import axios from "axios";
import { useState } from "react";
export default function Login(){ 
  const [email,setEmail]=useState(''); const [password,setPassword]=useState('');
  async function submit(e){ e.preventDefault(); try{ const r=await axios.post('http://localhost:8000/login',{email,password}); localStorage.setItem('token', r.data.access_token); alert('Logged in!'); }catch(err){ alert(err?.response?.data || err.message) } }
  return (<div className="container"><div className="card"><h3>Login</h3><form onSubmit={submit}><input placeholder="Email" value={email} onChange={e=>setEmail(e.target.value)} /><br/><input placeholder="Password" type="password" value={password} onChange={e=>setPassword(e.target.value)} /><br/><button className="btn" type="submit">Login</button></form></div></div>) }