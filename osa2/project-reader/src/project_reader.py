from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        
        data = toml.loads(content)
        
        project = data["project"]
        
        authors = [
            author["name"]
            for author in project["authors"]
            ]
            

        return Project(
            project["name"],
            project["description"],
            project["license"],
            authors,
            project["dependencies"],
            data["dependency-groups"]["dev"]
        )
