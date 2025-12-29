const s=new URLSearchParams(location.search).get("symbol")
const data=[100,102,101,105,110]
new Chart(c,{type:"line",
 data:{labels:data.map((_,i)=>i),
 datasets:[{label:s,data}]}})