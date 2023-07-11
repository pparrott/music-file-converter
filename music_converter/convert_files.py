import asyncio
from data_types import FileType
from pathlib import Path
import subprocess

def _output_filename(input_filename: Path, to_filetype: FileType, destination: Path) -> Path:
    new_filename = input_filename.with_suffix(f".{to_filetype.value}").name
    output_file = destination / new_filename
    return output_file

async def _convert_file(input: Path, output: Path) -> None:
    command = ['ffmpeg', '-i', input, output]
    try:
        await asyncio.create_subprocess_exec(*command)
        print(f"{input} converted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"FAILED to convert {input}")
        print(e)
        
async def _convert_files(input_files: list[Path], output_files: list[Path]) -> None:
    tasks = []
    print(type(input_files), type(output_files))
    for input_file, output_file in zip(input_files, output_files):
        tasks.append(asyncio.create_task(_convert_file(input_file, output_file)))
    await asyncio.gather(*tasks)

def desired_input_files(source: Path, from_filetype: FileType) -> list[Path]:
    return list(source.glob(f"*.{from_filetype.value}"))

def convert_input_files_to_desired_filetype(input: list[Path], destination: Path, to_filetype: FileType) -> None:
    output = [_output_filename(input_path, to_filetype, destination) for input_path in input]
    asyncio.run(_convert_files(input, output))
    return