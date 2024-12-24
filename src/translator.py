import logging
from typing import overload, Union, Literal
from pathlib import Path
from dataclasses import dataclass
from exceptions import *

@dataclass
class MISSING:
    pass

class Translator:
    """
    Class to create a translator for dynamic language applications

    Author: official-Cromatin
    Source: https://github.com/official-Cromatin/Python-Translator
    Version: V3.0
    """

    def __get_matching_files(self, names:list[str], raise_error:bool = False) -> list[Path]:
        """Returns a list containing the parts for all matching files
        
        Logs an error when illegal (.dotfiles or non .json) files are detected"""
        files_path:list[Path] = list(self.__localization_folder.iterdir())
        file_names:dict[str, Path] = {}

        # Filter all invalid or illegal files
        for file_path in files_path:
            full_file_name = file_path.name
            split_file_name = full_file_name.split(".")
            
            # Check for invalid file name
            if len(split_file_name) != 2 and raise_error:
                if raise_error:
                    raise InvalidFile(f"The file name {full_file_name} (full path: {file_path})is invalid, there are no dot files in the folder allowed")
                self.__logger.warning(f"The file name {full_file_name} (full path: {file_path})is invalid, there are no dot files in the folder allowed. The file has been omitted!")
                continue
            file_name, file_extension = split_file_name

            # Check for invalid file extension
            if file_extension != "json":
                if raise_error:
                    raise InvalidFile(f"The file {full_file_name} (full path: {file_path}) is not permitted, no loading of the files possible")
                self.__logger.warning(f"The file {full_file_name} (full path: {file_path}) is not permitted, the file was omitted!")
                continue

            file_names[file_name] = file_path
        
        # Append the path of each existing and requested file to the returning list
        selected_files:list[Path] = []
        valid_file_names:list[str] = list(file_names.keys())
        for name in names:
            # Check for the existence of the file
            if name not in valid_file_names:
                if raise_error:
                    raise MissingFile(f"The file with the name {name} could not be found")
                self.__logger.error(f"The file with the name {name} could not be found, it was therefore not loaded!")
                continue

            selected_files.append(file_names[name])

        return selected_files
