import ast

class EnvVariableExtractor(ast.NodeVisitor):
    def __init__(self):
        self.env_vars = {}  # To store environment variable names and types

    def visit_Call(self, node):
        # Handle os.getenv
        if self.is_os_getenv(node):
            env_name, env_type = self.extract_env_var(node, 0, 1)
            if env_name:
                self.env_vars[env_name] = env_type

        # Handle os.environ.get
        elif self.is_os_environ_get(node):
            env_name, env_type = self.extract_env_var(node, 0, 1)
            if env_name:
                self.env_vars[env_name] = env_type

        # Handle dotenv and environs libraries (if applicable)
        elif self.is_environs_or_dotenv(node):
            env_name, env_type = self.extract_env_var(node, 0, 1)
            if env_name:
                self.env_vars[env_name] = env_type

        self.generic_visit(node)

    def is_os_getenv(self, node):
        return (
            isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "os"
            and node.func.attr == "getenv"
        )

    def is_os_environ_get(self, node):
        return (
            isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Attribute)
            and node.func.value.attr == "environ"
            and node.func.attr == "get"
        )

    def is_environs_or_dotenv(self, node):
        # Check for `env.str`, `env.int`, `load_dotenv`, etc.
        return (
            isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id in {"env", "load_dotenv"}
        )

    def extract_env_var(self, node, key_arg_idx, default_arg_idx):
        """Extract environment variable name and type."""
        env_name = None
        env_type = "str"  # Default type is string

        # Extract the environment variable name
        if len(node.args) > key_arg_idx and isinstance(node.args[key_arg_idx], ast.Constant):
            env_name = node.args[key_arg_idx].value

        # Infer type from the default value
        if len(node.args) > default_arg_idx and isinstance(node.args[default_arg_idx], ast.Constant):
            default_value = node.args[default_arg_idx]
            env_type = type(default_value.value).__name__

        return env_name, env_type


def extract_env_variables_from_file(file_path):
    with open(file_path, "r") as file:
        tree = ast.parse(file.read(), filename=file_path)
    extractor = EnvVariableExtractor()
    extractor.visit(tree)
    return extractor.env_vars


