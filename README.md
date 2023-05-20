# Python-Translator

## Which features are offered
- Language dynamic applications based on Json files
- Placeholders built into the json value that can be filled with values by optional parameters
- Easy to use
- Minimization of data volume accesses, through the caching of content

## Demonstartion

```json 
{
    "readme.example": "This is a demonstration of the Translator function"
}
```
> en-EN.json

```json 
{
    "readme.example": "Das ist eine Demonstation der Funktion des Translators"
}
```
> de-DE.json

```python
#Normaly your Code would look like this for the corresponding language
print("This is a demonstration of the Translator function")
#or like this
print("Das ist eine Demonstation der Funktion des Translators")


#However, by querying the contents of the corresponding json file, the translator allows different languages without changing the code itself
print(translator("en-EN", "readme.example"))
#It is also possible to pass the specified language through a variable
lang = "en-EN"
print(translator(lang, "readme.example"))
```
> The actual program

Feel free to try out the [demo](https://github.com/official-Cromatin/Python-Translator/tree/main/demo)


## Implementation

The `translator.py` is the main file where all the code is located, you should also create a subfolder called `lang` in which the .json files for the corresponding languages are located.

If your file is called `de-DE` you have to call it with it, you can also enforce your own naming structure.
However, I recommend to use the [ISO(-639-1) language scheme](http://www.lingoes.net/en/translator/langcode.htm) for understanding reasons.

## Issues and improvements
Originally this code is for me personally and my own projects like the [CLI-Game-Collection](https://github.com/official-Cromatin/CLI-Game-Collection).
However, I decided to make it available for everyone.

If you have any problems or suggestions, feel free to contact me.
After all, I am currently at the beginning and still have a lot to learn