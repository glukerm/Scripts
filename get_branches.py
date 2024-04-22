# Store list of PRs to merge
# Use GitHub API to get list of branches
# Update first PR in list to be merged
# Check PR is up to date with main branch
# Merge PR
# Update next PR in list to be merged

import requests

pr_list = [6, 7]
url = "repos/glukerm/Scripts/branches"

r = requests.get(f"https://api.github.com/{url}")
print(r.status_code)
print(r.json())