from github import Github
from os import environ
from datetime import datetime

gh = Github(environ["GITHUB_TOKEN"])

with open("README.md", "w") as readme:
    readme.write(
        """# 🌟🌟🌟🌟🌟

These are my most recent stars, [updated daily](.github/workflows/readme.yml).

"""
    )

    for repo in gh.get_user().get_starred()[:5]:
        readme.write("* [" + repo.full_name + "](" + repo.html_url + ")\n")
        print(":: " + repo.full_name)

    readme.write("\nLast updated: " + datetime.utcnow().isoformat() + "\n")
