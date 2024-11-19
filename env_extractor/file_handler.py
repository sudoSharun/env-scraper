import json

class FileHandler:
class FileHandler:
    @staticmethod
    def save_as_env(env_vars, output_file):
        # Read existing content if the file exists
        existing_vars = {}
        try:
            with open(output_file, "r") as f:
                for line in f:
                    if "=" in line:
                        key, _, value = line.partition("=")
                        key = key.strip()
                        value = value.strip()
                        existing_vars[key] = value  # Preserve the existing value
        except FileNotFoundError:
            pass  # Ignore if file doesn't exist

        # Append new variables without overwriting existing ones
        for key, value in env_vars.items():
            if key not in existing_vars:
                existing_vars[key] = f"#{value}"  # New variables have default value

        # Save the updated content
        with open(output_file, "w") as f:
            for key, value in existing_vars.items():
                f.write(f"{key}={value}\n")  # Preserve original formatting
        print(f"Extracted environment variables saved to {output_file} (.env).")

    @staticmethod
    def save_as_env(env_vars, output_file):
        with open(output_file, "w") as f:
            for key, value in env_vars.items():
                f.write(f"{key}=      #{value}\n")
        print(f"Extracted environment variables saved to {output_file} (.env).")
