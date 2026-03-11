import random
from datetime import datetime

# Different "personalities" for your repo
moods = [
    "Feeling electric ⚡", 
    "Contemplating the meaning of 0s and 1s... 🤔", 
    "I need more RAM. Please star this repo to feed me. 🔋",
    "Scanning the matrix... everything looks green. 🟢"
]

def update_readme():
    current_mood = random.choice(moods)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = f"""
# 🤖 The Living Repository

### Status: {current_mood}
> **Last System Pulse:** {timestamp}

This README updates itself every 6 hours using GitHub Actions. 
It’s a project that exists without human touch.
"""
    with open("README.md", "w") as f:
        f.write(content)

if __name__ == "__main__":
    update_readme()
