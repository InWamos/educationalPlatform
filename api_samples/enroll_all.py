import requests


USERNAME = "admin"
PASSWORD = "admin88**"
BASE_URL = "http://127.0.0.1:8000/api/"
# retrieve all courses
r = requests.get(f"{BASE_URL}courses/")
courses = r.json()

available_courses = ", ".join([course["title"] for course in courses])
print(f"Available courses: {available_courses}")

for course in courses:
    course_id = course["id"]
    course_title = course["title"]
    r = requests.post(
        f"{BASE_URL}courses/{course_id}/enroll/", auth=(USERNAME, PASSWORD)
    )
    if r.status_code == 200:
        # successful request
        print(f"Successfully enrolled in {course_title}")
