import os

class Utils:
    @staticmethod
    def find_all_py_files(folder):
        py_files = []
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith(".py"):
                    py_files.append(os.path.join(root, file))
        return py_files
