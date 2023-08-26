# ANSI escape code for green text color
green_text = "\033[32m"

# Reset ANSI escape code to default color
reset_color = "\033[0m"

# Print green text
print(green_text + "This text is green!" + reset_color)


#############################################################################

from colorama import init, Fore, Style

# Initialize colorama
init()

# Print green text
print(Fore.GREEN + "This text is green!" + Style.RESET_ALL)


#############################################################################

# pip install colorama

"""

Sure, here are some ANSI escape codes for text colors in Python. 
ANSI escape codes vary depending on the terminal or console you're using, 
and not all terminals support all codes. However, these are some common codes for text colors:

- **Foreground (Text) Colors:**
  - Black: `\033[30m`
  - Red: `\033[31m`
  - Green: `\033[32m`
  - Yellow: `\033[33m`
  - Blue: `\033[34m`
  - Magenta: `\033[35m`
  - Cyan: `\033[36m`
  - White: `\033[37m`

- **Background Colors:**
  - Black: `\033[40m`
  - Red: `\033[41m`
  - Green: `\033[42m`
  - Yellow: `\033[43m`
  - Blue: `\033[44m`
  - Magenta: `\033[45m`
  - Cyan: `\033[46m`
  - White: `\033[47m`

- **Text Styles:**
  - Reset all attributes: `\033[0m`
  - Bold: `\033[1m`
  - Underline: `\033[4m`
  - Blink: `\033[5m`
  - Reverse: `\033[7m`
  - Conceal: `\033[8m`

Here's an example of how to use these codes to change text colors:

reset = "\033[0m"
red_text = "\033[31m"
green_bg = "\033[42m"
bold_text = "\033[1m"

print(red_text + "This text is red." + reset)
print(green_bg + "This text has a green background." + reset)
print(bold_text + "This text is bold." + reset)

Keep in mind that not all terminals or consoles support these codes, '
and the appearance might vary. Also, if you're targeting a specific terminal or console, 
it's a good idea to check its documentation for the supported ANSI escape codes. Additionally, 
libraries like `colorama` can help you achieve consistent color and style handling across different platforms.

"""