import os
from color4console.style import *

os.system("")


class ColorTheme():
    cInfo = ""
    cSuccess = ""
    cWarning = ""
    cError = ""
    cFatal = ""
    cEnd = "\033[0m"

    def __init__(self, theme):
        self.logThemeName = self.get_log_theme_name(theme)
        self.set_log_text_color(self.logThemeName)

    def get_log_theme_name(self, themeName):
        if LogTheme.LIGHT.value == themeName or LogTheme.DARK.value == themeName or LogTheme.DEFAULT.value == themeName or LogTheme.HIGHLIGHT.value == themeName or LogTheme.SYMBOL.value == themeName:
            return themeName
        else:
            return LogTheme.DEFAULT.value

    def set_log_text_color(self, themeName):
        self.cInfo = LogColor[themeName][LogType.INFO.value]
        self.cSuccess = LogColor[themeName][LogType.SUCCESS.value]
        self.cWarning = LogColor[themeName][LogType.WARNING.value]
        self.cError = LogColor[themeName][LogType.ERROR.value]
        self.cFatal = LogColor[themeName][LogType.FATAL.value]

    def normal(self, msg):
        print(msg)

    def warning(self, msg):
        print(self.cWarning + msg + self.cEnd)

    def error(self, msg):
        print(self.cError + msg + self.cEnd)

    def info(self, msg):
        print(self.cInfo + msg + self.cEnd)

    def success(self, msg):
        print(self.cSuccess + msg + self.cEnd)

    def fatal(self, msg):
        print(self.cFatal + msg + self.cEnd)

    def bold(self, msg):
        print(TextStyle.BOLD.value + msg + self.cEnd)

    def light(self, msg):
        print(TextStyle.LIGHT.value + msg + self.cEnd)

    def italic(self, msg):
        print(TextStyle.ITALIC.value + msg + self.cEnd)

    def underline(self, msg):
        print(TextStyle.UNDERLINE.value + msg + self.cEnd)

    def blink(self, msg):
        print(TextStyle.BLINK.value + msg + self.cEnd)


def ColorTest(msg):
    log = ColorTheme("light")
    log.normal("Color Theme: light")
    log.info(msg)
    log.success(msg)
    log.warning(msg)
    log.error(msg)
    log.fatal(msg)
    log.normal(" ")
    log = ColorTheme("symbol")
    log.normal("Color Theme: symbol")
    log.info(msg)
    log.success(msg)
    log.warning(msg)
    log.error(msg)
    log.fatal(msg)
    log.normal(" ")
    log = ColorTheme("highlight")
    log.normal("Color Theme: highlight")
    log.info(msg)
    log.success(msg)
    log.warning(msg)
    log.error(msg)
    log.fatal(msg)
    log.normal(" ")
    log = ColorTheme("default")
    log.normal("Other functions")
    log.bold(msg)
    log.italic(msg)
    log.light(msg)
    log.underline(msg)
    log.blink(msg)
    log.normal(" ")
