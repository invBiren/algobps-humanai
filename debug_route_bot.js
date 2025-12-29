const API_BASE = 'http://127.0.0.1:8000';
console.log("🔍 ROUTING DEBUG BOT STARTED");

// 1️⃣ Check current origin
console.log("Frontend origin:", window.location.origin);

// 2️⃣ Check dashboard availability
fetch(API_BASE + "/dashboard.html", { method: "GET" })
  .then(r => {
    if (r.ok) {
      console.log("✅ dashboard.html FOUND on frontend server");
    } else {
      console.error("❌ dashboard.html NOT FOUND (status:", r.status + ")");
    }
  })
  .catch(e => console.error("❌ Fetch failed:", e));

// 3️⃣ Verify redirect logic
async function testRedirect() {
  console.log("Testing redirect…");
  window.location.href = "/dashboard.html";
}

// 4️⃣ Manual trigger (call in console)
window.forceDashboard = testRedirect;

console.log("🧪 Run forceDashboard() to test redirect manually");

