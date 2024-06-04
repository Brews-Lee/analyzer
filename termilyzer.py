import argparse
from pathlib import Path

from func import *
    
def main():
    p = argparse.ArgumentParser()

    p.add_argument("path", help="Path to a directory to analyze all files from or to a single file to analyze")
    p.add_argument("-o", "--output",
                    help="Path to a file to print output into, default is stdout",
                    default="stdout",
                    required=False)
    p.add_argument("-d", "--delimiter",
                    help="A delimiter that separates that separates data in the csv file, default is a comma ','",
                    default=',',
                    required=False)
    p.add_argument("-s", "--separator",
                    help="A separator character or string, default is '|'",
                    default='|',
                    required=False)
    args = p.parse_args()

    path = Path(args.path)
    
    if not path.exists():
        p.error("The entered path is not a valid path to an existing object!")
    print(f"Analyzing the '{path}' " + f"{'file' if path.is_file()  else 'directory' if path.is_dir() else 'error'}" + "...")
    print(f"Separator: '{args.separator}'")

    data = get_data(path, args.separator)
    analyze(data, args.output)

if __name__ == "__main__":
    main()
