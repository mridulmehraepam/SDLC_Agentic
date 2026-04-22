import { useEffect, useState } from "react";

const API_BASE = "http://127.0.0.1:8000";

export default function App() {
	const [health, setHealth] = useState("checking");

	useEffect(() => {
		fetch(`${API_BASE}/health`)
			.then((res) => res.json())
			.then((data) => setHealth(data.status || "unknown"))
			.catch(() => setHealth("offline"));
	}, []);

	return (
		<main style={{ fontFamily: "Segoe UI, sans-serif", maxWidth: 860, margin: "40px auto", padding: "0 16px" }}>
			<h1>Podcast Episode Planner</h1>
			<p>Initial runnable scaffold for backend and frontend.</p>

			<section style={{ border: "1px solid #ddd", borderRadius: 8, padding: 16 }}>
				<h2>Backend Health</h2>
				<p>Status: <strong>{health}</strong></p>
				<p>URL: {API_BASE}/health</p>
			</section>
		</main>
	);
}
