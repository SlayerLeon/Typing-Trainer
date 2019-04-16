import random
from typetrainer import menu

config = menu.get_settings()


def get_random_texts(filename: str, text_number: int):
    try:
        with open(filename,
                  encoding=config['GENERAL']['FILE_ENCODING']) as file:
            data = file.read()
            texts = data.split('\n\n')
            if text_number == -1:
                random.shuffle(texts)
            return texts
    except FileNotFoundError:
        print('Dictionary not found')
        exit(config['ERR_CODES']['ERROR_MISSING_FILE'])


def get_random_words(filename: str):
    try:
        with open(filename,
                  encoding=config['GENERAL']['FILE_ENCODING']) as file:
            data = file.read()
            texts = data.split('\n\n')
            result = []
            for text in texts:
                lines = text.split('\n')
                new_text = []
                for line in lines:
                    words = line.split(' ')
                    random.shuffle(words)
                    new_text.append(' '.join(words))
                result.append('\n'.join(new_text))

            return result
    except FileNotFoundError:
        print('Dictionary not found')
        exit(config['ERR_CODES']['ERROR_MISSING_FILE'])
