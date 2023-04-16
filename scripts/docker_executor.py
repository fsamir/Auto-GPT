import logging
import os

import docker


class DockerExecutor:

    def __init__(self, docker_image, supported_file_extensions=[]):
        self.docker_image = docker_image
        self.supported_file_extensions = supported_file_extensions

    def execute(self, command, file):
        """Execute a file in a Docker container and return the output"""
        workspace_folder = "auto_gpt_workspace"

        print(f"Executing file '{file}' in workspace '{workspace_folder}'")

        if not self.check_string_end(file, self.supported_file_extensions):
            return f"Error: Invalid file type. Only {self.supported_file_extensions} files are allowed."

        file_path = os.path.join(workspace_folder, file)

        # if not os.path.isfile(file_path):
        #     return f"Error: File '{file}' does not exist."

        try:
            client = docker.from_env()

            env_vars = self.populate_env_vars()

            absolute_path = os.path.abspath(workspace_folder)
            logging.debug(f"Running container with image '{self.docker_image}' and command '{command} on workspace '{absolute_path}'")

            # https://docker-py.readthedocs.io/en/stable/containers.html
            container = client.containers.run(
                self.docker_image,
                command,
                volumes={
                    absolute_path: {
                        'bind': '/workspace',
                        'mode': 'rw'}
                },
                environment=env_vars,
                working_dir='/workspace',
                stderr=True,
                stdout=True,
                detach=True,
            )

            output = container.wait()
            logs = container.logs().decode('utf-8')
            container.remove()

            # print(f"Execution complete. Output: {output}")
            # print(f"Logs: {logs}")

            return logs

        except Exception as e:
            return f"Error: {str(e)}"

    def populate_env_vars(self):
        # XXX: Do not load all env var or else it will crash the container run.
        return {
            'OPENAI_API_KEY': os.environ.get('OPENAI_API_KEY'),
            'ANTICAPTCHA_KEY': os.environ.get('ANTICAPTCHA_KEY'),
            'PINECONE_API_KEY': os.environ.get('PINECONE_API_KEY'),
            'PINECONE_ENV': os.environ.get('PINECONE_ENV'),
            'ELEVENLABS_API_KEY': os.environ.get('ELEVENLABS_API_KEY'),
            'HUGGINGFACE_API_TOKEN': os.environ.get('HUGGINGFACE_API_TOKEN')
        }

    def check_string_end(self, string_value, endings_list):
        for ending in endings_list:
            if string_value.endswith(ending):
                return True
        return False
