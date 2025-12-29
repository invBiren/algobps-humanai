function toast(msg){
  const t = document.createElement("div");
  t.innerText = msg;
  t.style = "position:fixed;bottom:20px;right:20px;background:#333;color:#fff;padding:10px;";
  document.body.appendChild(t);
  setTimeout(()=>t.remove(),3000);
}
