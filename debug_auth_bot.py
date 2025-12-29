import requests
import sys
import time

BASE = "http://127.0.0.1:8000"

def banner(msg):
    print("\n" + "=" * 60)
    print(msg)
    print("=" * 60)

def fatal(msg):
    banner("❌ FATAL ERROR")
    print(msg)
    sys.exit(1)

def ok(msg):
    print(f"✅ {msg}")

# ----------------------------
# STEP 1 — Verify backend alive
# ----------------------------
banner("STEP 1 — BACKEND HEALTH")

try:
    r = requests.get(f"{BASE}/session/authority", timeout=5)
    ok("Backend reachable")
except Exception as e:
    fatal(f"Backend not reachable: {e}")

# ----------------------------
# STEP 2 — Verify clean session
# ----------------------------
banner("STEP 2 — SESSION RESET CHECK")

session = r.json()
print("Session:", session)

if session.get("connected") is True:
    print("⚠️ Session already connected — resetting required")
else:
    ok("Session initially disconnected")

# ----------------------------
# STEP 3 — Trigger LOGIN
# ----------------------------
banner("STEP 3 — LOGIN CALL")

r = requests.post(
    f"{BASE}/broker/mstock/login",
    json={"username": "TEST", "password": "TEST"},
)

print("Response:", r.json())

if r.json().get("status") != "otp_sent":
    fatal("Login endpoint NOT returning otp_sent")

ok("Login endpoint OK")

# ----------------------------
# STEP 4 — Trigger VERIFY OTP
# ----------------------------
banner("STEP 4 — VERIFY OTP CALL")

r = requests.post(
    f"{BASE}/broker/mstock/verify-otp",
    json={"api_key": "TESTKEY", "otp": "123456"},
)

print("Response:", r.json())

if r.json().get("status") != "connected":
    fatal("verify-otp is NOT returning connected")

ok("verify-otp endpoint OK")

# ----------------------------
# STEP 5 — Confirm session mutation
# ----------------------------
banner("STEP 5 — SESSION CONFIRMATION")

r = requests.get(f"{BASE}/session/authority")
session = r.json()
print("Session:", session)

if session.get("connected") is not True:
    fatal("SESSION FLAG DID NOT PERSIST")

ok("Session flag persisted")

# ----------------------------
# STEP 6 — Frontend redirect contract
# ----------------------------
banner("STEP 6 — FRONTEND CONTRACT CHECK")

print("""
Frontend MUST redirect when:
response.status === "connected"

If browser is still stuck:
• verifyOtp() is NOT wired
• onclick is wrong
• old JS cached
""")

ok("Backend side validated")

banner("🎯 BOT COMPLETE — BACKEND AUTH IS CORRECT")
