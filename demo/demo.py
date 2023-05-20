import json
import time
from random import randint
from os import chdir, path
chdir(path.dirname(path.realpath(__file__)))

languages = ["de-DE","en-EN"]

class Translator():
    """
    Class to create language dynamic applications based on json files.
    
    Author: official-Cromatin
    Source: https://github.com/official-Cromatin/Python-Translator
    Version: V2.1
    """

    # You are allowed to change these
    path_prefix = "./lang/" # Path under which the json files are found
    file_format = ".json" # File format which should be loaded
    placeholder_prefix = "{" # Initial character with which a placeholder is marked
    placeholder_suffix = "}" # End character with which a placeholder is marked

    error_no_attribute = "Placeholder" # Value to be used for an unspecified placeholder
    error_file_not_found = "File not found for specified language" # Value to return if the file was not found
    error_file_not_json = "File is not a valid json format" # Value to return if the file is not in json format
    error_no_key_found = "Translation not found" # Value to return if the translation was not found

    # But fingers off these
    current_languages = []
    cached_language = {}

    def translate(lang:str, key:str, pick_random_array_value:bool = True, **kwargs):
        """
        Main method of the class, it calls values depending on the key, adjusts replacement values and returns them as string
        
        Arguments:
        ----------
        - `lang`: Name of the file (excluding the filename extension) to be loaded
        - `key`: Name of the key from which the value is to be retrieved
        - `pick_random_array_value`: If the value for a json value is an array ...
            - `True`: ... a value is selected randomly.
            - `False`: ...  the first value is selected.
        - `**kwargs`: Optional arguments whose values replace the placeholders from the json value

        Returns:
        --------
        `str`: String reflecting the entry of the corresponding json file
        """
        if not lang in Translator.current_languages:
            try:
                text_wrapper = open(Translator.path_prefix + lang + Translator.file_format)
            except FileNotFoundError:
                return Translator.error_file_not_found
            else:
                try:
                    Translator.cached_language[lang] = json.load(text_wrapper)
                except json.decoder.JSONDecodeError:
                    return Translator.error_file_not_json
                else:
                    Translator.current_languages.append(lang)
        
        try:
            value:str = Translator.cached_language[lang][key]
        except KeyError:
            return Translator.error_no_key_found
        
        if isinstance(value, list):
            if pick_random_array_value:
                value = value[randint(0, len(value) - 1)]
            else:
                value = value[0]
        
        if kwargs.items():
            opt_args = dict(kwargs.items())
            runs = 0
            for letter in value:
                if letter == Translator.placeholder_prefix:
                    runs += 1
            for _ in range(runs):
                begin = value.rindex(Translator.placeholder_prefix) + len(Translator.placeholder_prefix)
                end = value.rindex(Translator.placeholder_suffix)
                placeholder = value[begin:end]

                if placeholder in opt_args:
                    value = value.replace(Translator.placeholder_prefix + placeholder + Translator.placeholder_suffix, str(opt_args[placeholder]), 1)
                else:
                    value = value.replace(Translator.placeholder_prefix + placeholder + Translator.placeholder_suffix, Translator.error_no_attribute, 1)
        return value
    
    def force_reload():
        """Method to clear the temporary cache. It causes a reread of the json files"""
        Translator.current_languages = []
        Translator.cached_language = {}

def language_picker():
    languages = ["de-DE","en-EN"]
    i = 0

    while True:
        lang = languages[i]
        entry = input(Translator.translate(lang, "language.select"))
        if entry == "1":
            return "de-DE"
        elif entry == "2":
            return "en-EN"
        else:
            if i == 0:
                i = 1
            elif i == 1:
                i = 0


lang = language_picker()

print('\033[32m'+Translator.translate(lang, "greeting")+'\033[0m')
while True:
    entry = input('\033[33m'+Translator.translate(lang, "action.select")+'\033[0m')
    if entry == "1":
        print('\033[36m'+Translator.translate(lang, "time", today = time.strftime("%d.%m"), times = time.strftime("%H:%M:%S"))+'\033[0m')
    elif entry == "2":
        print('\033[36m'+Translator.translate(lang, "iam")+'\033[0m')
    elif entry == "3":
        print('\33[44m'+Translator.translate(lang, "color")+'\033[0m')
    elif entry == "4":
        print('\033[36m'+Translator.translate(lang, "arrays")+'\033[0m')
        print('\033[36m'+Translator.translate(lang, "random.output")+'\033[0m')
    elif entry == "5":
        lang = language_picker()
    elif entry == "6":
        print('\033[36m'+Translator.translate(lang, "shutdown")+'\033[0m')
        break
    else:
        print('\033[36m'+Translator.translate(lang, "no.action")+'\033[0m')
