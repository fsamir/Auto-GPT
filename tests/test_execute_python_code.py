import json
import os

from docker_executor import DockerExecutor
from python_code_executor import PythonCodeExecutor

python_code_executor = PythonCodeExecutor()
docke_executor = DockerExecutor('fsamir/python:3.11', ['.py'])


def test_execute_python_file():
    list_json = 'auto_gpt_workspace/book_list.json'

    if os.path.isfile(list_json):
        os.remove(list_json)

    # books = docke_executor.execute("ls", "python/books_scraper.py")
    logs = python_code_executor.execute("python/books_scraper.py")
    
    books = json.loads(logs)

    print(f"Books: {books}")
    assert len(books) == 20


if __name__ == '__main__':
    test_execute_python_file()
