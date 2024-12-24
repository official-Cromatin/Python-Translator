class TranslatorException(Exception):
    pass

class InvalidFile(TranslatorException):
    pass

class MissingFile(TranslatorException):
    pass
