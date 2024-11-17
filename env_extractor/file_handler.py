import json

class FileHandler:
    @staticmethod
    def save_as_json(env_vars, output_file):
        with open(output_file, "w") as f:
            json.dump(env_vars, f, indent=4)
        print(f"Extracted environment variables saved to {output_file} (JSON).")

    @staticmethod
    def save_as_env(env_vars, output_file):
        with open(output_file, "w") as f:
            for key, value in env_vars.items():
                f.write(f"{key}=      #{value}\n")
        print(f"Extracted environment variables saved to {output_file} (.env).")
