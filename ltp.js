const ws=new WebSocket("ws://127.0.0.1:8000/ws/ltp")
ws.onmessage=e=>{
 const d=JSON.parse(e.data)
 Object.keys(d).forEach(s=>{
  if(document.getElementById(s))
   document.getElementById(s).innerText=d[s]
 })
}
