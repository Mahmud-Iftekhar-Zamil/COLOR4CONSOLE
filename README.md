# color4console
color4console enables you to print colorful text without wasting time experimenting with various color combinations. It comes with a predefined color scheme. The color of the text is determined by the chosen theme.
This package's goal is to keep things as simple as possible. When the color of a text line is red, for example, bolding, underlining, or highlighting it is not essential. In the same way, if a text line is underlined, it may not be necessary to color it.

# Installation 
You need to install the package using pip.

```
pip install color4console

```

# Pre defined themes:
You can chose any of the following theme. Text color will automatically set based on your selected theme. 
```
default
light
dark
highlight
symbol
```

# Color Supported Functions:
```
info()
success()
warning()
error()
fatal()
```
# Other Functions:
```
normal()
bold()
underline()
italic()
light()
blink()
```

# Usage
In your terminal or python file, use as below.

```python
from color4console import *
log = ColorTheme("light")
log.error("This is a SAMPLE ERROR message.")
```


You can also use following function to check all output of a sample message:
```python
from color4console import *
ColorTest("This is a SAMPLE TEXT to test.")
```

