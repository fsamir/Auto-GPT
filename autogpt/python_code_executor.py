from autogpt.docker_executor import DockerExecutor


class PythonCodeExecutor:

    def __init__(self):
        self.docker_executor = DockerExecutor('fsamir/python:3.11', ['.py'])

    def execute(self, file_name):
        """Execute a Python file in a Docker container and return the output"""

        command = f"python {file_name}"
        return self.docker_executor.execute(command, file_name)
