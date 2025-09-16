import axios from "axios";
import { useEffect, useState } from "react";
export default function Feed(){ 
  const [topics,setTopics]=useState([]);
  useEffect(()=>{ axios.get('http://localhost:8000/topics').then(r=>setTopics(r.data)).catch(()=>setTopics([])) },[]);
  return (<div className="container">{topics.map(t=> <div className="card topic" key={t.id}><h4>{t.title}</h4><p className="small">{t.description}</p></div>)}</div>) }