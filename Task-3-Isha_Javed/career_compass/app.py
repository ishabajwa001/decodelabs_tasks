import csv
import math
import os
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import webbrowser
import threading

DATA_FILE = os.path.join(os.path.dirname(__file__), "raw_skills.csv")
HTML_FILE = os.path.join(os.path.dirname(__file__), "index.html")
BASE_DIR    = os.path.dirname(__file__)
IMAGES_DIR  = os.path.join(BASE_DIR, "..", "images")

def load_dataset():
    roles = []
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            roles.append({"job_role": row["job_role"], "skills": row["skills"].split()})
    return roles

def compute_idf(roles):
    N = len(roles)
    df = {}
    for role in roles:
        for skill in set(role["skills"]):
            df[skill] = df.get(skill, 0) + 1
    return {skill: math.log(N / count) for skill, count in df.items()}

def compute_tfidf_vector(skills, idf, vocabulary):
    total = len(skills)
    tf = {}
    for skill in skills:
        tf[skill] = tf.get(skill, 0) + 1
    return {
        term: (tf[term] / total) * idf[term]
        if term in tf and term in idf else 0.0
        for term in vocabulary
    }

def cosine_similarity(vec_a, vec_b):
    dot   = sum(vec_a.get(k, 0) * vec_b.get(k, 0) for k in vec_a)
    mag_a = math.sqrt(sum(v ** 2 for v in vec_a.values()))
    mag_b = math.sqrt(sum(v ** 2 for v in vec_b.values()))
    if mag_a == 0 or mag_b == 0:
        return 0.0
    return dot / (mag_a * mag_b)

def recommend(user_skills, top_n=3):
    roles = load_dataset()
    idf   = compute_idf(roles)
    vocab = set()
    for role in roles:
        vocab.update(role["skills"])
    vocab.update(user_skills)
    user_vec = compute_tfidf_vector(user_skills, idf, vocab)
    scored = []
    for role in roles:
        role_vec = compute_tfidf_vector(role["skills"], idf, vocab)
        score    = cosine_similarity(user_vec, role_vec)
        scored.append({"role": role["job_role"], "score": round(score, 4)})
    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:top_n]


MIME_TYPES = {
    "png":  "image/png",
    "jpg":  "image/jpeg",
    "jpeg": "image/jpeg",
    "svg":  "image/svg+xml",
    "webp": "image/webp",
    "gif":  "image/gif",
    "ico":  "image/x-icon",
    "css":  "text/css",
    "js":   "application/javascript",
}

class Handler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        pass

    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/":
            with open(HTML_FILE, "r", encoding="utf-8") as f:
                html = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))

        elif path.startswith("/images/"):
            filename = path[len("/images/"):]
            file_path = os.path.join(IMAGES_DIR, filename)
            if os.path.isfile(file_path):
                ext = file_path.rsplit(".", 1)[-1].lower()
                self.send_response(200)
                self.send_header("Content-Type", MIME_TYPES.get(ext, "application/octet-stream"))
                self.end_headers()
                with open(file_path, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.send_response(404)
                self.end_headers()

        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if urlparse(self.path).path == "/recommend":
            length = int(self.headers.get("Content-Length", 0))
            body   = self.rfile.read(length)
            try:
                data        = json.loads(body)
                user_skills = [str(s).strip().lower() for s in data.get("skills", []) if s]
                results     = recommend(user_skills)
                response    = json.dumps({"results": results})
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(response.encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode())
        else:
            self.send_response(404)
            self.end_headers()


def main():
    PORT = 5000
    server = HTTPServer(("localhost", PORT), Handler)
    url = f"http://localhost:{PORT}"
    print(f"\n  Career Compass is running!")
    print(f"  Open: {url}\n")
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")
        server.shutdown()


if __name__ == "__main__":
    main()
