# Welcome to the Rainbow package!

## Introduction
The `Rainbow` module provides functions to add color to text in the terminal or prompt.

This package aims to make it easier to use colors in the prompt with Python.

Say goodbye to those horrible-to-remember character sets that we had to use to insert colors into the prompt. With this module, coloring the prompt will be quick and easy.

## Installation
You can install `Rainbow` via pip:
- pip install rainbow_prompt

## Usage

### Importing the Module
```python
from rainbow import cstring, rc_string
```

### Printing Colored Text
```python
cstring("Hello, World!", "green")
```

### Returning Colored Text
```python
colored_text = rc_string("Hello, World!", "red")
print(colored_text)
```

## Available Colors
The following color names are available:
- black
- red
- green
- yellow
- blue
- magenta
- cyan
- white

Available Backgrounds:
- bg_black
- bg_red
- bg_green
- bg_yellow
- bg_blue
- bg_magenta
- bg_ciano
- bg_white

Available Styles:
- style_negrito
- style_sublinhado
- style_invertido

> Note: Make sure to use these color names exactly as specified.

## Example
```python
from rainbow import cstring

cstring("This is a colored prompt.", "blue")
cstring("Error!", "red")
cstring("Warning!", "yellow")
```

[GitHub](https://github.com/davidmarquescoder/rainbow-package)
[Issues](https://github.com/davidmarquescoder/rainbow-package/issues)