import json

class Translator():
    """
    Class to create language dynamic applications based on json files.
    
    Author: official-Cromatin
    Source: https://github.com/official-Cromatin/Python-Translator
    Version: V2.0
    """

    # You are allowed to change these
    path_prefix = "./lang" # Path under which the json files are found
    placeholder_prefix = "{" # Initial character with which a placeholder is marked
    placeholder_suffix = "}" # End character with which a placeholder is marked

    error_no_attribute = "Placeholder" # Value to be used for an unspecified placeholder
    error_file_not_found = "File not found for specified language" # Value to return if the file was not found
    error_file_not_json = "File is not a valid json format" # Value to return if the file is not in json format
    error_no_key_found = "Translation not found" # Value to return if the translation was not found

    # But fingers off these
    current_languages = []
    cached_language = {}

    def translate(lang:str, key:str, **kwargs):
        """
        Main method of the class, it calls values depending on the key, adjusts replacement values and returns them as string
        
        Arguments:
        ----------
        - `lang`: Name of the file (excluding the filename extension) to be loaded
        - `key`: Name of the key from which the value is to be retrieved
        - `**kwargs`: Optional arguments whose values replace the placeholders from the json value

        Returns:
        --------
        `str`: 
        """
        if not lang in Translator.current_languages:
            try:
                text_wrapper = open(Translator.path_prefix)
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