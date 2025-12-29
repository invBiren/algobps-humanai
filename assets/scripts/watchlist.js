const ws = new WebSocket(`ws://${location.host}/market/ltp`);

ws.onmessage = e => {
  const prices = JSON.parse(e.data);
  const tbody = document.querySelector("#watchlist tbody");
  tbody.innerHTML = "";

  Object.entries(prices).forEach(([sym, ltp]) => {
    tbody.innerHTML += `
      <tr>
        <td>${sym}</td>
        <td>${ltp}</td>
        <td>${(Math.random()*2-1).toFixed(2)}</td>
        <td><button onclick="buy('${sym}')">B</button></td>
        <td><button onclick="sell('${sym}')">S</button></td>
      </tr>
    `;
  });
};

function buy(sym){ openOrder(sym, "BUY"); }
function sell(sym){ openOrder(sym, "SELL"); }
