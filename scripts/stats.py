"""Writes assets/stats.svg from the public GitHub API (own, non-fork repositories only). Run by .github/workflows/stats.yml."""
import json, os, subprocess, datetime

def api(path):
    return json.loads(subprocess.check_output(["gh", "api", "--paginate", "--slurp", path], text=True))

user = os.environ.get("GH_USER", "AurelioAvila")
u = api(f"users/{user}")[0]
repos = [r for page in api(f"users/{user}/repos?per_page=100&type=owner") for r in page if not r["fork"]]
stars = sum(r["stargazers_count"] for r in repos)
items = [("Public repositories", len(repos)), ("Stars across them", stars), ("Followers", u["followers"])]
today = datetime.date.today().isoformat()
cells = "".join(
    f'<text x="{30 + i * 135}" y="78" font-size="34" font-weight="700" fill="#e8b86d">{v}</text>'
    f'<text x="{30 + i * 135}" y="102" font-size="12" fill="#c9d1d9">{k}</text>'
    for i, (k, v) in enumerate(items)
)
svg = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="440" height="150" viewBox="0 0 440 150" role="img" '
    f'aria-label="GitHub numbers on {today}: {len(repos)} public repositories, {stars} stars, {u["followers"]} followers">'
    '<rect width="440" height="150" rx="8" fill="#0d1117" stroke="#30363d"/>'
    '<g font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif">'
    '<text x="30" y="36" font-size="15" font-weight="600" fill="#e8b86d">GitHub at a glance</text>'
    f'{cells}'
    f'<text x="30" y="134" font-size="11" fill="#8b949e">From the GitHub API, own non-fork repositories. Updated {today}.</text>'
    '</g></svg>\n'
)
open("assets/stats.svg", "w", encoding="utf-8").write(svg)
print(len(repos), stars, u["followers"])
