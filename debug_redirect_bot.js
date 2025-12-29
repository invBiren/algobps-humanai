function handleVerifyResponse(d) {
  if (d.status === "connected") {
    console.log("REDIRECTING TO DASHBOARD");
    window.location.assign("./dashboard.html");
  } else {
    alert("OTP verification failed");
  }
}
