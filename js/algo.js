export async function refreshAlgoState() {
    const r = await fetch("/algo/status");
    const s = await r.json();

    const btn = document.getElementById("algoToggle");
    btn.textContent = s.running ? "STOP ALGO" : "START ALGO";
    btn.className = s.running ? "danger" : "success";
}

export async function toggleAlgo() {
    const path = document.getElementById("algoToggle").textContent.includes("START")
        ? "/algo/start"
        : "/algo/stop";

    await fetch(path);
    refreshAlgoState();
}
