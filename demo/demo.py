import json
import time

languages = ["de-DE","en-EN"]

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
    file_name = "demo/lang/"+lang+".json"
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

def language_picker():
    languages = ["de-DE","en-EN"]
    i = 0

    while True:
        lang = languages[i]
        entry = input(translator(lang, "language.select"))
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

print('\033[32m'+translator(lang, "greeting")+'\033[0m')
while True:
    entry = input('\033[33m'+translator(lang, "action.select")+'\033[0m')
    if entry == "1":
        today = time.strftime("%d.%m")
        times = time.strftime("%H:%M:%S")
        print('\033[36m'+translator(lang, "time")+'\033[0m')
    elif entry == "2":
        print('\033[36m'+translator(lang, "iam")+'\033[0m')
    elif entry == "3":
        print('\33[44m'+translator(lang, "color")+'\033[0m')
    elif entry == "4":
        print('\033[36m'+translator(lang, "commands")+'\033[0m')
    elif entry == "5":
        lang = language_picker()
    elif entry == "6":
        print('\033[36m'+translator(lang, "shutdown")+'\033[0m')
        break
    else:
        print('\033[36m'+translator(lang, "no.action")+'\033[0m')
