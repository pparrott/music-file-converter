import argparse
from argparse import Namespace
from music_converter.config import DEFAULT_OUTPUT_FOLDER
from music_converter.convert_files import desired_input_files, convert_input_files_to_desired_filetype
from music_converter.data_types import FileType, ConversionPlan
from pathlib import Path

def get_args() -> Namespace:
    parser = argparse.ArgumentParser(prog="Music file converter")
    parser.add_argument("-f", "--from-file", help="Filetype to convert from", required=True)
    parser.add_argument("-t", "--to-file", help="Filetype to convert to", required=True)
    parser.add_argument("-s", "--source", help="Source folder", required=True)
    parser.add_argument("-d", "--destination", help="Destination folder", required=False)
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    conversion_plan = ConversionPlan(
        from_filetype=FileType(args.from_file),
        to_filetype=FileType(args.to_file),
        source=Path(args.source),
        destination=Path(args.destination) if args.destination else None
    )
    conversion_plan.create_destination_folder(DEFAULT_OUTPUT_FOLDER)
    input_files = desired_input_files(
        source=conversion_plan.source,
        from_filetype=conversion_plan.from_filetype
    )
    convert_input_files_to_desired_filetype(
        input=input_files,
        destination=conversion_plan.destination,
        to_filetype=conversion_plan.to_filetype
    )