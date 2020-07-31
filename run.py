from github import Github
from os import environ

gh = Github(environ["GITHUB_TOKEN"])

with open("README.md", "w") as readme:
    readme.write(
        """check out some recent stars!

🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟
"""
    )

    for repo in gh.get_user().get_starred()[1:4]:
        readme.write("* " + repo.name + "\n")
        print(repo.name)
