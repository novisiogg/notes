from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class ChatHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # ── ROUTING ──────────────────────────────────────────────────────
        # Handle only /api/chat endpoint; everything else gets 404.
        if self.path != "/api/chat":
            self.send_error(404)
            return

        # ── READ REQUEST BODY ───────────────────────────────────────────
        # Content-Length tells us how many bytes to read from the socket.
        content_length = int(self.headers["Content-Length"])
        # Read exactly that many bytes from the input stream.
        raw_body = self.rfile.read(content_length)  # bytes
        # Decode UTF-8 → string, then parse JSON → Python dict/list.
        body_str = raw_body.decode("utf-8")
        data = json.loads(body_str)

        # ── EXTRACT LAST USER MESSAGE ───────────────────────────────────
        # Expected payload shape:
        #   {"model": "...", "messages": [{"role": "...", "content": "..."}, ...]}
        # The most recent user utterance is the last element in the list.
        user_message = data["messages"][-1]["content"]

        # ── GENERATE REPLY ───────────────────────────────────────────────
        # Replace this with real LLM logic later — for now, simple echo.
        model = data["model"]
        reply_text = f"{model}: {user_message}"

        # ── BUILD RESPONSE ──────────────────────────────────────────────
        # 1. Status line: "HTTP/1.1 200 OK\r\n"
        self.send_response(200)

        # 2. Headers (one per line). Body is JSON, so declare it:
        self.send_header("Content-Type", "application/json")

        # 3. Calculate body size and send Content-Length header.
        response_bytes = json.dumps({"reply": reply_text}).encode("utf-8")
        self.send_header("Content-Length", str(len(response_bytes)))

        # 4. Blank line — signals end of headers.
        self.end_headers()

        # 5. Body — raw bytes go out on the wire.
        self.wfile.write(response_bytes)

    # Optional: silence the default access log to keep stdout clean.
    def log_message(self, format, *args):
        pass


# ── SERVER BOOTSTRAP ──────────────────────────────────────────────────
if __name__ == "__main__":
    # Bind to localhost:5000. 'localhost' resolves to 127.0.0.1.
    server = HTTPServer(("localhost", 8000), ChatHandler)
    print("Mock server running on http://localhost:5000/api/chat")
    print("Press Ctrl+C to stop.")
    # Blocking infinite loop: accept() → handle() → close() → repeat.
    server.serve_forever()
