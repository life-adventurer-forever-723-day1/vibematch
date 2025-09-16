import axios from "axios";
import { useState } from "react";
export default function Signup(){ 
  const [name,setName]=useState(''); const [email,setEmail]=useState(''); const [password,setPassword]=useState('');
  async function submit(e){ e.preventDefault(); try{ await axios.post('http://localhost:8000/signup',{name,email,password}); alert('Signed up! Now login.')}catch(err){ alert(err?.response?.data || err.message) } }
  return (<div className="container"><div className="card"><h3>Signup</h3><form onSubmit={submit}><input placeholder="Name" value={name} onChange={e=>setName(e.target.value)} /><br/><input placeholder="Email" value={email} onChange={e=>setEmail(e.target.value)} /><br/><input placeholder="Password" type="password" value={password} onChange={e=>setPassword(e.target.value)} /><br/><button className="btn" type="submit">Sign up</button></form></div></div>) }