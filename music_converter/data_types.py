from enum import Enum
from pathlib import Path
from pydantic import BaseModel, model_validator, field_validator

class FileType(Enum):
    FLAC = "flac"
    AIFF = "aiff"
    WAV = "wav"
    MP3 = "mp3"
    
class ConversionPlan(BaseModel):
    from_filetype: FileType
    to_filetype: FileType
    source: Path
    destination: Path | None
    
    @model_validator(mode="after")
    def check_different_filepaths(cls, m: "ConversionPlan"):
        if m.from_filetype.value == m.to_filetype.value:
            raise ValueError("From and to filetypes are the same")
        return m
    
    @field_validator("source", mode='after')
    def check_source_folder_exists(cls, val: Path):
        if not val.exists():
            raise ValueError(f"{val} is not a real path, check the source again")
        return val
    
    def create_destination_folder(self, default_folder: str) -> None:
        if not self.destination:
            self.destination = self.source / default_folder
            print(f"Destination folder not supplied, new files will be written to: {self.destination}")
        if not self.destination.exists():
            print(f"Destination folder does not exist, creating: {self.destination}")
            self.destination.mkdir()
        else:
            print(f"Destination folder already exists, continuing...")
