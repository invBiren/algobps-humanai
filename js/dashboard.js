const ws = new WebSocket("ws://127.0.0.1:8000/trade/pnl/ws");

ws.onmessage = e => {
  document.getElementById("pnl").innerText = "₹" + JSON.parse(e.data).pnl;
};

async function refresh() {
  const s = await fetch("/algo/status").then(r => r.json());
  document.getElementById("algoState").innerText = s.running ? "RUNNING" : "STOPPED";
}
setInterval(refresh, 2000);

function startAlgo(){ fetch("/algo/start"); }
function stopAlgo(){ fetch("/algo/stop"); }
