import json
import os

languages = ["de-DE","en-EN"]
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
    value = dataDE[key]
    replacement_list = str_between(value, "{", "}")
    runs = len(replacement_list)

    if runs != 0:
        for i in range(runs):
            replacement = replacement_list[i]
            replacement_value = globals()[replacement]

            value = value.replace("{"+replacement+"}", replacement_value, 1)
        return value
    else:
        return value

def language_picker(supported_languages):
    number = len(supported_languages)
    i = 0

    while True:
        lang = supported_languages[i]
        eingabe = input(translator(lang, "language.select"))
        if eingabe == "1":
            return "de-DE"
        elif eingabe == "2":
            return "en-EN"
        else:
            if i == 0:
                i = 1
            elif i == 1:
                i = 0

lang = language_picker(languages)

eingabe = input(translator(lang, "input.help"))
if eingabe == "1":
    output = translator(lang, "useless.help")
    print(output)
elif eingabe == "2":
    output = translator(lang, "usefull.help").format(placeholder="dann")
    print(output)
else:
    print(translator(lang, "no.help"))