COLORS = {
    'reset': '\033[0m',
    'black': '\033[0;30m',
    'red': '\033[0;31m',
    'green': '\033[0;32m',
    'yellow': '\033[0;33m',
    'blue': '\033[0;34m',
    'magenta': '\033[0;35m',
    'cyan': '\033[0;36m',
    'white': '\033[0;37m',

    'bg_red': '\033[0;41m',
    'bg_yellow': '\033[0;43m',
    'bg_black': '\033[0;40m',
    'bg_green': '\033[0;42m',
    'bg_blue': '\033[0;44m',
    'bg_magenta': '\033[0;45m',
    'bg_ciano': '\033[0;46m',
    'bg_white': '\033[0;47m',

    'style_negrito': '\033[1m',
    'style_sublinhado': '\033[4m',
    'style_invertido': '\033[7m',
}


def print_colored_string(text, color_name):
    text = text
    color_code = COLORS.get(color_name.lower(), '')
        
    return print(f"{color_code}{text}{COLORS['reset']}")


def return_colored_string(text, color_name):
    text = text
    color_code = COLORS.get(color_name.lower(), '')
        
    return f"{color_code}{text}{COLORS['reset']}"
