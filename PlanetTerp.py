import requests
from urllib.parse import urlencode
import planetterp

BASE_URL = 'https://api.planetterp.com/v1/'

def course(name, reviews = False):
    params = {"name" : name, "reviews": "true" if reviews else "false"}
    url = BASE_URL + "course?" + urlencode(params)
    return requests.get(url).json()


def courses(department = None, reviews = False, limit = 100, offset = 0):
    params = {"department" : department, "reviews": "true" if reviews else "false", "limit": limit, "offset": offset}
    # filter out None args
    params = {k:v for k, v in params.items() if v is not None}
    url = BASE_URL + "courses?" + urlencode(params)
    return requests.get(url).json()


def professor(name, reviews = False):
    params = {"name" : name, "reviews": "true" if reviews else "false"}
    url = BASE_URL + "professor?" + urlencode(params)
    return requests.get(url).json()


def professors(type_ = None, reviews = False, limit = 100, offset = 0):
    if type_ and type_ not in ["professor", "ta"]:
        raise ValueError("Expected type to be one of ['professor', 'ta'], got " + str(type_))
    params = {"type" : type_, "reviews": "true" if reviews else "false", "limit": limit, "offset": offset}
    # filter out None args
    params = {k:v for k, v in params.items() if v is not None}
    url = BASE_URL + "professors?" + urlencode(params)
    return requests.get(url).json()


def grades(course = None, professor = None, semester = None, section = None):
    params = {"course" : course, "professor": professor, "semester": semester, "section": section}
    # filter out None args
    params = {k:v for k, v in params.items() if v is not None}
    url = BASE_URL + "grades?" + urlencode(params)
    return requests.get(url).json()
