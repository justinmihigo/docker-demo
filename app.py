
# app.py

from flask import Flask
app= Flask(__name__)

@app.route("/")
def hello():
    return """<!doctype html>
 <html lang="en">
    <head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Hello from Docker / Kubernetes</title>
  <style>
    :root{
      --bg:#0b69a3;
      --accent:#0ea5d9;
      --card:#ffffff;
      --muted:#6b7280;
    }
    html,body{height:100%;margin:0;font-family:Inter,system-ui,-apple-system,Segoe UI,Roboto,"Helvetica Neue",Arial;}
    body{
      display:flex;
      align-items:center;
      justify-content:center;
      background:linear-gradient(135deg,#062f4b 0%,var(--bg) 60%);
      color:var(--card);
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      padding:24px;
    }
    .wrap{
      width:100%;
      max-width:980px;
      display:grid;
      grid-template-columns: 1fr 380px;
      gap:24px;
      align-items:start;
    }
    .hero{
      background:rgba(255,255,255,0.06);
      border-radius:14px;
      padding:28px;
      box-shadow:0 8px 30px rgba(2,6,23,0.45);
      backdrop-filter: blur(6px);
    }
    h1{
      margin:0 0 8px 0;
      font-size:28px;
      color:#fff;
      line-height:1.05;
    }
    .tag{
      display:inline-block;
      background:rgba(255,255,255,0.08);
      color:#e6f7ff;
      padding:6px 10px;
      border-radius:999px;
      font-size:13px;
      margin-bottom:12px;
    }
    p.lead{
      margin:12px 0 18px 0;
      color:var(--card);
      opacity:0.95;
    }
    .meta{
      background:var(--card);
      color:#0b2850;
      padding:14px;
      border-radius:10px;
      font-size:14px;
      box-shadow: 0 6px 18px rgba(2,6,23,0.25);
    }
    .meta p{margin:6px 0;color:var(--muted);}
    .btn{
      display:inline-block;
      margin-top:14px;
      background:var(--accent);
      color:#042331;
      padding:10px 14px;
      border-radius:10px;
      text-decoration:none;
      font-weight:600;
      box-shadow: 0 6px 14px rgba(14,165,217,0.18);
    }

    /* small column */
    .aside{
      display:flex;
      flex-direction:column;
      gap:14px;
    }
    .card{
      background:var(--card);
      color:#072031;
      border-radius:12px;
      padding:16px;
      box-shadow: 0 8px 24px rgba(2,6,23,0.12);
    }
    .muted{color:var(--muted); font-size:14px}

    /* responsive */
    @media (max-width:880px){
      .wrap{grid-template-columns:1fr; padding:0}
    }

    /* tiny pulse */
    .pulse{
      display:inline-block;
      width:10px;height:10px;border-radius:999px;background:#34d399;
      box-shadow:0 0 0 rgba(52,211,153,0.6);
      animation:pulse 2s infinite;
      vertical-align:middle;margin-right:8px;
    }
    @keyframes pulse{
      0%{box-shadow:0 0 0 0 rgba(52,211,153,0.45)}
      70%{box-shadow:0 0 0 12px rgba(52,211,153,0)}
      100%{box-shadow:0 0 0 0 rgba(52,211,153,0)}
    }
  </style>
</head>
<body>
  <main class="wrap" role="main" aria-labelledby="title">
    <section class="hero" aria-labelledby="title">
      <div class="tag"><span class="pulse" aria-hidden="true"></span> Running in Docker / Kubernetes</div>
      <h1 id="title">Hello from Docker — served through Kubernetes!</h1>
      <p class="lead">This is a lightweight demo service listening on <strong>port 5000</strong>. The page is intentionally minimal and responsive so you can eyeball changes quickly.</p>

      <div class="meta">
        <p><strong>Status:</strong> <span style="color: #059669">Healthy</span> — routing via Kong</p>
        <p><strong>Version:</strong> v2 — these are new changes</p>
        <p class="muted">This message and the HTML layout were updated to make testing and visual verification easier.</p>
        <a class="btn" href="/" role="button">Refresh</a>
      </div>
    </section>

    <aside class="aside">
      <div class="card">
        <h3 style="margin:0 0 8px 0">Recent updates</h3>
        <p style="margin:0 0 8px 0">• Let me see if the changes have gone through now let us test the gpg keys— <em>v2</em></p>
        <p style="margin:0 0 8px 0">• This is the new line added in another version.</p>
        <p class="muted" style="margin-top:12px">Tip: use your browser devtools to verify headers and routing.</p>
      </div>

      <div class="card">
        <h4 style="margin:0 0 8px 0">Debug</h4>
        <p class="muted" style="margin:0">Path: <code>/</code></p>
        <p class="muted" style="margin:0">Upstream: <code>http://localhost:5000</code></p>
      </div>
    </aside>
  </main>
</body>
</html>
"""

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)

