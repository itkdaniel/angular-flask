class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
    DEFAULT = "\033[0m"

    LIGHT_CYAN_BG_BLACK = "\033[1;36;40m"
    LIGHT_CYAN_BG_RED = "\033[1;36;41m"
    LIGHT_CYAN_BG_GREEN = "\033[1;36;42m"
    LIGHT_CYAN_BG_YELLOW = "\033[1;36;43m"
    LIGHT_CYAN_BG_BLUE = "\033[1;36;44m"
    LIGHT_CYAN_BG_PURPLE = "\033[1;36;45m"
    LIGHT_CYAN_BG_CYAN = "\033[1;36;46m"
    LIGHT_CYAN_BG_WHITE = "\033[1;36;47m"

class BGColors:
    BG_BLACK = "\033[1;40m"
    BG_RED = "\033[1;41m"
    BG_GREEN = "\033[1;42m"
    BG_YELLOW = "\033[1;43m"
    BG_BLUE = "\033[1;44m"
    BG_PURPLE = "\033[1;45m"
    BG_CYAN = "\033[1;46m"
    BG_WHITE = "\033[1;47m"

"""
print("\033[1;32;40m Bright Green \n")
\033[ Escape code, this is always the same
1 = Style, 1 for normal.
32 = Text colour, 32 for bright green.
40m = Background colour, 40 is for black.
"""

# print("\033[1;31;40m Bright Red \033[0m 1;31;40m \033[0;31;47m Red \033[0m 0;31;47m \033[0;37;42m Black \033[0m 0;37;42m \033[0m")
# print("\033[1;32;40m Bright Green \033[0m 1;32;40m \033[0;32;47m Green \033[0m 0;32;47m \033[0;37;43m Black \033[0m 0;37;43m \033[0m")
# print("\033[1;33;40m Yellow \033[0m 1;33;40m \033[0;33;47m Brown \033[0m 0;33;47m \033[0;37;44m Black \033[0m 0;37;44m \033[0m")
# print("\033[1;34;40m Bright Blue \033[0m 1;34;40m \033[0;34;47m Blue \033[0m 0;34;47m \033[0;37;45m Black \033[0m 0;37;45m \033[0m")
# print("\033[1;35;40m Bright Magenta \033[0m 1;35;40m \033[0;35;47m Magenta \033[0m 0;35;47m \033[0;37;46m Black \033[0m 0;37;46m \033[0m")
# print("\033[1;36;40m Bright Cyan \033[0m 1;36;40m \033[0;36;47m Cyan \033[0m 0;36;47m \033[0;37;47m Black \033[0m 0;37;47m \033[0m")
# print("\033[1;37;40m White \033[0m 1;37;40m \033[0;37;40m Light Grey \033[0m 0;37;40m \033[0;37;48m Black \033[0m 0;37;48m \033[0m")

    # print("\n\t{}BLACK\n\t{}RED\n\t{}GREEN\n\t{}BROWN\n\t{}BLUE\n\t{}PURPLE\n\t{}CYAN\n\t{}LIGHT_GRAY\n\t{}DARK_GRAY\n\t{}LIGHT_RED\n\t{}LIGHT_GREEN\n\t{}YELLOW\n\t{}LIGHT_BLUE\n\t{}LIGHT_PURPLE\n\t{}LIGHT_CYAN\n\t{}LIGHT_WHITE\n\t{}BOLD\n\t{}FAINT\n\t{}ITALIC\n\t{}UNDERLINE\n\t{}BLINK\n\t{}NEGATIVE\n\t{}CROSSED\n\t{}END\n\t{}DEFAULT".format(
# Colors.BLACK,Colors.RED,Colors.GREEN,Colors.BROWN,Colors.BLUE,Colors.PURPLE,Colors.CYAN,Colors.LIGHT_GRAY,Colors.DARK_GRAY,Colors.LIGHT_RED,Colors.LIGHT_GREEN,Colors.YELLOW,Colors.LIGHT_BLUE,Colors.LIGHT_PURPLE,Colors.LIGHT_CYAN,Colors.LIGHT_WHITE,Colors.BOLD,Colors.FAINT,Colors.ITALIC,Colors.UNDERLINE,Colors.BLINK,Colors.NEGATIVE,Colors.CROSSED,Colors.END,"\033[0m"))
