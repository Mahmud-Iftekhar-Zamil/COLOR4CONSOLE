from enum import Enum

NONE = " "
CEND = "\033[0m"
TAB = " "


class LogType(Enum):
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"
    FATAL = "fatal"


class LogTheme(Enum):
    DEFAULT = "default"
    LIGHT = "light"
    DARK = "dark"
    HIGHLIGHT = "highlight"
    SYMBOL = "symbol"


class Symbol(Enum):
    CHECK = u"\u2713"
    DELTA = u"\u0394"
    THETA = u"\u0398"
    CHI = u"\u03A7"
    IOTA = u"\u0399"


class TextStyle(Enum):
    BOLD = "\033[1m"
    LIGHT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"


class FGCOLOR(Enum):
    NBLACK = "\033[30m"
    NRED = "\033[31m"
    NGREEN = "\033[32m"
    NYELLOW = "\033[33m"
    NBLUE = "\033[34m"
    NPURPLE = "\033[35m"
    NCYAN = "\033[36m"
    NWHITE = "\033[37m"
    BLACK = "\033[90m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"


class BGCOLOR(Enum):
    NBLACK = "\033[40m"
    NRED = "\033[41m"
    NGREEN = "\033[42m"
    NYELLOW = "\033[43m"
    NBLUE = "\033[44m"
    NPURPLE = "\033[45m"
    NCYAN = "\033[46m"
    NWHITE = "\033[47m"
    BLACK = "\033[100m"
    RED = "\033[101m"
    GREEN = "\033[102m"
    YELLOW = "\033[103m"
    BLUE = "\033[104m"
    PURPLE = "\033[105m"
    CYAN = "\033[106m"
    WHITE = "\033[107m"


class HIGHLIGHTCOLOR(Enum):
    FG_WHITE_BG_RED = "\033[97;101m"
    FG_BLACK_BG_YELLOW = "\033[30;103m"
    FG_WHITE_BG_BLUE = "\033[97;104m"
    FG_WHITE_BG_PURPLE = "\033[97;45m"


LogColor = {
    LogTheme.DARK.value: {
        LogType.INFO.value: FGCOLOR.BLUE.value, LogType.SUCCESS.value: FGCOLOR.GREEN.value, LogType.WARNING.value: FGCOLOR.YELLOW.value, LogType.ERROR.value: FGCOLOR.RED.value, LogType.FATAL.value: BGCOLOR.RED.value
    },
    LogTheme.LIGHT.value: {
        LogType.INFO.value: FGCOLOR.BLUE.value, LogType.SUCCESS.value: FGCOLOR.GREEN.value, LogType.WARNING.value: FGCOLOR.YELLOW.value, LogType.ERROR.value: FGCOLOR.RED.value, LogType.FATAL.value: BGCOLOR.RED.value
    },
    LogTheme.DEFAULT.value: {
        LogType.INFO.value: FGCOLOR.BLUE.value, LogType.SUCCESS.value: FGCOLOR.GREEN.value, LogType.WARNING.value: FGCOLOR.YELLOW.value, LogType.ERROR.value: FGCOLOR.RED.value, LogType.FATAL.value: BGCOLOR.RED.value
    },
    LogTheme.HIGHLIGHT.value: {
        LogType.INFO.value: HIGHLIGHTCOLOR.FG_WHITE_BG_BLUE.value, LogType.SUCCESS.value: BGCOLOR.NGREEN.value, LogType.WARNING.value: HIGHLIGHTCOLOR.FG_BLACK_BG_YELLOW.value, LogType.ERROR.value: HIGHLIGHTCOLOR.FG_WHITE_BG_RED.value, LogType.FATAL.value: HIGHLIGHTCOLOR.FG_WHITE_BG_PURPLE.value
    },
    LogTheme.SYMBOL.value: {
        LogType.INFO.value: FGCOLOR.NBLUE.value + Symbol.IOTA.value + CEND + TAB, LogType.SUCCESS.value: FGCOLOR.NGREEN.value + Symbol.CHECK.value + CEND + TAB, LogType.WARNING.value: FGCOLOR.NYELLOW.value + Symbol.DELTA.value + CEND + TAB, LogType.ERROR.value: FGCOLOR.NRED.value + Symbol.CHI.value + CEND + TAB, LogType.FATAL.value: FGCOLOR.NPURPLE.value + Symbol.THETA.value + CEND + TAB
    }
}
