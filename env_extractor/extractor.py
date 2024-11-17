import json
from env_extractor.file_handler import FileHandler
from env_extractor.envloader import extract_env_variables_from_file

class EnvVariableExtractor:
    def __init__(self, env_files, output_format, output_file):
        self.env_files = env_files
        self.output_format = output_format
        self.output_file = output_file or ".env"

    def extract_and_save(self):
        all_env_vars = {}
        for env_file in self.env_files:
            env_vars = extract_env_variables_from_file(env_file)
            all_env_vars.update(env_vars)

        if self.output_format == 'json':
            FileHandler.save_as_json(all_env_vars, self.output_file)
        elif self.output_format == 'env':
            FileHandler.save_as_env(all_env_vars, self.output_file)
