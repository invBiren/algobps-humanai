const API_BASE = 'http://127.0.0.1:8000';
function buy(sym){
 fetch(API_BASE + "http://127.0.0.1:8000/order/place",{
  method:"POST",
  headers:{"Content-Type":"application/json"},
  body:JSON.stringify({symbol:sym,side:"BUY",qty:1,type:"MARKET"})
 })
}

