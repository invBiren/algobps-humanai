const API = "";

export async function login(api_key, username, password) {
  const res = await fetch(`${API}/auth/login`, {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({ api_key, username, password })
  });
  return res.json();
}
