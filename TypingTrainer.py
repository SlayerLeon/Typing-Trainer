import sys
import colorama
import configparser

config = configparser.ConfigParser()
config.read(r'typetrainer\settings.ini')
try:
    from typetrainer import game, multiplayer_menu, socket_client, text_tools,\
        texts_generator, menu
except Exception as e:
    print('Game modules not found: "{}"'.format(e), file=sys.stderr)
    exit(config['ERR_CODES']['ERROR_MISSING_MODULE'])


def main():
    # TODO -h --help
    colorama.init()
    menu.main_menu()


if __name__ == '__main__':
    main()