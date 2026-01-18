import os
import time
import requests
import subprocess
import random

# --- CONFIGURATION ---
GITHUB_TOKEN = "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"      # <--- PASTE TOKEN
REPO_OWNER = "StefanGebhard"          # <--- PASTE USERNAME
REPO_NAME = "mock-repo-test"
BRANCH_NAME = "master"
# ---------------------

BASE_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# --- REALISTIC CONTENT GENERATORS ---

def get_push_content():
    """Returns a scenario where Code and Docs change together."""
    scenarios = [
        {
            "name": "Update Server Port",
            "file_code": "src/main.py",
            "content_code": f"""
def start_server():
    # Updated port configuration
    port = {random.randint(8000, 9000)}
    print(f"Server started on port {{port}}")
""",
            "file_doc": "README.md",
            "content_doc": f"# Server Config\n\nThe server now listens on a dynamic port range (8000-9000) for better load balancing.\nUpdated at {time.ctime()}."
        },
        {
            "name": "Fix Math Logic",
            "file_code": "src/utils.js",
            "content_code": """
function add(a, b) {
    // Fixed logic to handle string inputs
    return Number(a) + Number(b);
}
""",
            "file_doc": "docs/api_v2.md",
            "content_doc": "# API Utilities\n\nThe `add` function now explicitly casts inputs to Numbers to prevent string concatenation bugs."
        }
    ]
    return random.choice(scenarios)

def get_pr_content():
    """Returns a new feature scenario with both Code and Docs."""
    features = [
        {
            "branch": "feature-auth-login",
            "title": "Add OAuth Login Flow",
            "body": "This PR implements the OAuth2 handshake in `auth.py` and documents the flow in `docs/auth.md`.",
            "files": {
                "src/auth.py": "def login_oauth(provider):\n    return f'Redirecting to {provider}...' ",
                "docs/auth.md": "# Authentication\n\nWe support OAuth2. Call `login_oauth('google')` to start."
            }
        },
        {
            "branch": "feature-database-connector",
            "title": "Add Database Connection Pooling",
            "body": "Added a new `db.py` module for pooling. Updated architecture docs.",
            "files": {
                "src/db.py": "class DB:\n    def connect(self):\n        print('Connected to pool')",
                "docs/architecture.md": "# Database\n\nWe now use connection pooling defined in `src/db.py`."
            }
        }
    ]
    return random.choice(features)

# --- GIT HELPERS ---

def run_git(command):
    try:
        subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Git Error: {e.stderr.strip()}")

def ensure_dir(file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

# --- TRIGGERS ---

def trigger_push():
    print("\n--- Triggering REALISTIC PUSH ---")
    scenario = get_push_content()
    print(f"Scenario: {scenario['name']}")
    
    # 1. Update Code File
    ensure_dir(scenario['file_code'])
    with open(scenario['file_code'], "w") as f:
        f.write(scenario['content_code'])
    
    # 2. Update Doc File
    ensure_dir(scenario['file_doc'])
    with open(scenario['file_doc'], "w") as f:
        f.write(scenario['content_doc'])
    
    # 3. Git operations
    run_git(f"git add {scenario['file_code']} {scenario['file_doc']}")
    run_git(f'git commit -m "{scenario["name"]}: Updated {scenario["file_code"]} and docs"')
    run_git(f"git push origin {BRANCH_NAME}")
    print("✅ Push complete.")

def trigger_pr():
    print("\n--- Triggering REALISTIC PR ---")
    scenario = get_pr_content()
    branch = f"{scenario['branch']}-{int(time.time())}"
    
    # 1. New Branch
    run_git(f"git checkout -b {branch}")
    
    # 2. Create Files
    for filepath, content in scenario['files'].items():
        ensure_dir(filepath)
        with open(filepath, "w") as f:
            f.write(content)
            
    # 3. Push
    run_git("git add .")
    run_git(f'git commit -m "Feat: {scenario["title"]}"')
    run_git(f"git push origin {branch}")
    
    # 4. Create PR via API
    data = {
        "title": scenario['title'],
        "body": scenario['body'],
        "head": branch,
        "base": BRANCH_NAME
    }
    resp = requests.post(f"{BASE_URL}/pulls", json=data, headers=HEADERS)
    
    run_git(f"git checkout {BRANCH_NAME}") # Switch back safely
    
    if resp.status_code == 201:
        print(f"✅ PR Created: {resp.json()['html_url']}")
    else:
        print(f"❌ Error: {resp.text}")

def trigger_issue():
    print("\n--- Triggering REALISTIC ISSUE ---")
    # Issues that reference specific files
    issues = [
        {"title": "Bug in main.py server loop", "body": "The `start_server` function in `src/main.py` does not handle port conflicts."},
        {"title": "Documentation missing for auth.py", "body": "I see `src/auth.py` was added but `README.md` mentions nothing about login flows."}
    ]
    data = random.choice(issues)
    
    resp = requests.post(f"{BASE_URL}/issues", json=data, headers=HEADERS)
    if resp.status_code == 201:
        item = resp.json()
        print(f"✅ Issue Created: #{item['number']} - {item['title']}")
        return item['number']
    return None

def trigger_comment(issue_number):
    print(f"\n--- Triggering REALISTIC COMMENT on #{issue_number} ---")
    comments = [
        "I checked `src/main.py` and I think line 4 is the issue.",
        "Can you update `docs/api_v2.md` to reflect these changes?",
        "The code in `src/utils.js` seems to contradict the documentation."
    ]
    data = {"body": random.choice(comments)}
    
    resp = requests.post(f"{BASE_URL}/issues/{issue_number}/comments", json=data, headers=HEADERS)
    if resp.status_code == 201:
        print("✅ Comment added.")

def main():
    while True:
        print("\n=== AI Training Event Generator ===")
        print("1. Push (Code + Doc update)")
        print("2. Pull Request (New Feature Code + Docs)")
        print("3. Issue (Refers to specific files)")
        print("4. Comment (Discusses code/docs)")
        print("5. Exit")
        
        choice = input("Select: ")
        
        if choice == '1': trigger_push()
        elif choice == '2': trigger_pr()
        elif choice == '3': 
            global last_issue
            last_issue = trigger_issue()
        elif choice == '4':
            inum = input(f"Issue # (default {last_issue if 'last_issue' in globals() else '?'}): ")
            if not inum and 'last_issue' in globals(): inum = last_issue
            if inum: trigger_comment(inum)
        elif choice == '5': break

if __name__ == "__main__":
    main()