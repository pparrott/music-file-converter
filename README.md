# Music file converter 

Simple program to convert music files to other formats. Takes a source folder and converts all files matching the file format to a destination folder with the new format.

## Pre-requisites
Must have ffmpeg, Poetry, and Python 3.11 installed with ffmpeg available on your path. Check to see this is working by running `ffmpeg -version`

## How to use
From the cli, first install dependencies with `poetry install`

Once installed, run `poetry run python music_converter/main.py -f FILETYPE_TO_CONVERT -t FILETYPE_TO_WRITE -s SOURCE_FOLDER -d DESTINATION_FOLDER`

Arguments:

* `-f --from-file`: the filetype to convert, see supported formats for enumeration options
* `-t --to-file`: the filetype to write to, see supported formats for enumeration options
* `-s --source`: the source folder with the files to be converted. Does not search recursively, only the single directory is considered
* `-d --destination`: the destination folder for the converted files. This is *OPTIONAL* and will by default write to `<source_folder>/converted_files`

Once the program is running, you will need to `ctrl+c` out once the writing is finished

## Supported formats

Supported formats are as follows:

* wav
* flac
* aiff
* mp3