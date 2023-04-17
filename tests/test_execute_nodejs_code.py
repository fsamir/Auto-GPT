import json

from autogpt.nodejs_code_executor import NodeJsCodeExecutor

nodejs_code_executor = NodeJsCodeExecutor()


def test_execute_nodejs_file():
    # XXX: These files are mounted in the docker container
    file_name = "nodejs/books-scraper-run.js"
    logs = nodejs_code_executor.execute(file_name, "npm install --prefix ./nodejs/")
    # print(f"Logs: {logs}")
    logs = nodejs_code_executor.execute(file_name, f"node {file_name}")

    print(f"Logs: {logs}")

    books = json.loads(logs)
    print(f"Books: {books}")
    assert len(books) == 20


def test_mocha_file():
    file_name = "nodejs/books-scraper-test.js"
    logs = nodejs_code_executor.execute(file_name, f"mocha {file_name} --reporter spec", )

    print(f"Logs: {logs}")

    assert "1 passing" in logs


def test_npm_install():
    file_name = "none.js"
    logs = nodejs_code_executor.execute(file_name, "npm install chai", )

    print(f"Logs: {logs}")

    assert logs is not None


if __name__ == '__main__':
    test_execute_nodejs_file()
    test_mocha_file()
