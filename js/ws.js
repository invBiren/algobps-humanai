let socket;
let reconnectTimer = null;

export function connectWS(onMessage) {
    const WS_URL = location.protocol === "https:"
        ? `wss://${location.host}/market/ltp`
        : `ws://${location.host}/market/ltp`;

    socket = new WebSocket(WS_URL);

    socket.onopen = () => {
        console.log("🟢 WS Connected");
        clearTimeout(reconnectTimer);
    };

    socket.onmessage = (e) => {
        onMessage(JSON.parse(e.data));
    };

    socket.onclose = () => {
        console.warn("🔴 WS Disconnected — retrying...");
        reconnectTimer = setTimeout(() => connectWS(onMessage), 1500);
    };

    socket.onerror = () => socket.close();
}
