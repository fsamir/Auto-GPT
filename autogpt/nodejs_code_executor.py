from autogpt.docker_executor import DockerExecutor


class NodeJsCodeExecutor:
    IMAGE = 'fsamir/nodejs-puppeteer:dev'

    def __init__(self):
        # image = 'node:18-buster-slim'
        self.docker_executor = DockerExecutor(NodeJsCodeExecutor.IMAGE, ['.js'])

    def execute(self, file, command: str = None):
        """Execute a JavaScript file in a Docker container and return the output"""
        if command is None:
            command = f"node {file}"

        return self.docker_executor.execute(file, command)
