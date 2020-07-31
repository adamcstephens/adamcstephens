from github import Github
from os import environ
from datetime import datetime

gh = Github(environ["GITHUB_TOKEN"])

with open("README.md", "w") as readme:
    readme.write(
        """# some recent stars

🌟🌟🌟

"""
    )

    for repo in gh.get_user().get_starred()[:5]:
        readme.write("* " + repo.name + "\n")
        print(repo.name)

    readme.write("\nLast updated: " + datetime.utcnow().isoformat() + "\n")
