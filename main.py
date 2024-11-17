from env_extractor.parser import ArgumentParser
from env_extractor.extractor import EnvVariableExtractor
from env_extractor.utils import Utils

def main():
    args = ArgumentParser().parse_args()

    if not args.all and not args.file:
        print("Error: You must specify either -a or -f.")
        exit(1)

    if args.all:
        files_to_scan = Utils.find_all_py_files(args.folder)
        if not files_to_scan:
            print(f"No Python files found in folder {args.folder}.")
            exit(1)
    else:
        files_to_scan = [args.file] if args.file else []

    output_file = args.output if args.output else None
    output_format = 'json' if args.json else 'env'

    extractor = EnvVariableExtractor(
        env_files=files_to_scan,
        output_format=output_format,
        output_file=output_file,
    )

    extractor.extract_and_save()

if __name__ == "__main__":
    main()
