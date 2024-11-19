import json

class FileHandler:
    @staticmethod
    def save_as_json(env_vars, output_file):
        # Read existing content if the file exists
        existing_vars = {}
        try:
            with open(output_file, "r") as f:
                existing_vars = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass  # Ignore if file doesn't exist or content isn't valid JSON
        
        # Merge existing variables with new ones (new variables overwrite existing ones)
        existing_vars.update(env_vars)
        
        # Save the updated content
        with open(output_file, "w") as f:
            json.dump(existing_vars, f, indent=4)
        print(f"Extracted environment variables saved to {output_file} (JSON).")

    @staticmethod
    def save_as_env(env_vars, output_file):
        # Read existing content if the file exists
        existing_vars = {}
        try:
            with open(output_file, "r") as f:
                for line in f:
                    if "=" in line:
                        key, _, comment = line.partition("=")
                        key = key.strip()
                        existing_vars[key] = comment.strip()  # Preserve existing comments
        except FileNotFoundError:
            pass  # Ignore if file doesn't exist

        # Merge existing variables with new ones (new variables overwrite existing ones)
        for key, value in env_vars.items():
            if key not in existing_vars:
                existing_vars[key] = f"#{value}"

        # Save the updated content
        with open(output_file, "w") as f:
            for key, value in existing_vars.items():
                f.write(f"{key}=      {value}\n")
        print(f"Extracted environment variables saved to {output_file} (.env).")
