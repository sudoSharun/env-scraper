import argparse
import os
from env_extractor.utils import Utils

class ArgumentParser:
    def __init__(self):
        self.parser = self.setup_argument_parser()

    def setup_argument_parser(self):
        parser = argparse.ArgumentParser(
            description="Extract environment variables from Python files."
        )

        output_group = parser.add_mutually_exclusive_group(required=False)
        output_group.add_argument(
            "--json", action="store_true", help="Output in JSON format."
        )

        parser.add_argument(
            "-o", "--output", type=str, help="Output file for extracted variables."
        )

        parser.add_argument(
            "-a", "--all", action="store_true", help="Scan all .py files."
        )

        parser.add_argument(
            "--folder", type=str, default=os.getcwd(), help="Directory to scan."
        )

        parser.add_argument(
            "-f", "--file", type=str, help="Scan a specific Python file."
        )

        return parser

    def parse_args(self):
        return self.parser.parse_args()
