import json
import os

from docker_executor import DockerExecutor
from nodejs_code_executor import NodeJsCodeExecutor

nodejs_code_executor = NodeJsCodeExecutor()

def test_execute_nodejs_file():
    list_json = 'auto_gpt_workspace/book_list.json'
    if os.path.isfile(list_json):
        os.remove(list_json)

    # XXX: This files are mounted in the docker container
    file_name = "books-scraper-run.js"
    nodejs_code_executor.execute(f"node {file_name}", file_name)

    f = open(list_json)
    data = json.load(f)
    
    assert len(data) == 20

def test_mocha_file():
    # file_name = "/app/src/delaware-sos-scraper-tests.js"
    file_name = "books-scraper.js"
    # logs = nodejs_code_executor.execute(f"mocha {file_name} --reporter spec", file_name)
    logs = nodejs_code_executor.execute(f"'mocha --version'", file_name)
    # logs = nodejs_code_executor.execute(f" 'node --version' ", file_name)
    assert len(logs) == 20


if __name__ == '__main__':
    # test_execute_nodejs_file()
    test_mocha_file()
