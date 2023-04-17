from autogpt.docker_executor import DockerExecutor


class PythonCodeExecutor:

    def __init__(self):
        self.docker_executor = DockerExecutor('fsamir/python:3.11', ['.py'])

    def execute(self, file):
        """Execute a Python file in a Docker container and return the output"""

        command = f"python {file}"
        return self.docker_executor.execute(file, command)
