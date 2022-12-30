import json
import os

languages = ["de-DE","en-EN"]
lang = "de-DE"
greeting = "Hallo"
goodbye = "Auf wiedersehen"

def str_between(str, prefix, suffix):
    runs = count_letters(str, "{")
    between = []
    for i in range(runs):
        begin = str.rindex(prefix) + len(prefix)
        end = str.rindex(suffix)
        between.append(str[begin:end])

        str = str.replace("{"+between[i]+"}", "placeholder", 1)
    return between

def count_letters(str, searcher):
    str = list(str)
    count = 0
    for letter in str:
        if letter == searcher:
            count = count + 1
    return count

def translator(lang, key):
    file_name = "lang/"+lang+".json"
    try:
        file = open(file_name)
    except FileNotFoundError:
        return "File not found for specified language" 
    dataDE = json.load(file)
    try:
        value = dataDE[key]
    except KeyError:
        value = "Translation not found"
    replacement_list = str_between(value, "{", "}")
    runs = len(replacement_list)

    if runs != 0:
        for i in range(runs):
            replacement = replacement_list[i]
            try:
                replacement_value = globals()[replacement]
            except KeyError:
                replacement_value = "Variable not found"

            value = value.replace("{"+replacement+"}", replacement_value, 1)
        return value
    else:
        return value