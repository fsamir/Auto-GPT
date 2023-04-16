from autogpt.docker_executor import DockerExecutor


class NodeJsCodeExecutor:

    IMAGE = 'fsamir/nodejs-puppeteer:dev'

    def __init__(self):
        # image = 'node:18-buster-slim'
        self.docker_executor = DockerExecutor(NodeJsCodeExecutor.IMAGE, ['.js'])

    def execute(self, command, file_name):
        """Execute a JavaScript file in a Docker container and return the output"""

        return self.docker_executor.execute(command, file_name)
