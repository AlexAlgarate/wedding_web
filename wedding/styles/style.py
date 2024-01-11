from enum import Enum
import reflex as rx

from wedding.styles.colors import Color, TextColor
from wedding.styles.fonts import Font, FontWeight

# Constants

MAX_WIDTH = "800px"
FLEX_DIRECTION = ["column", "column", "column", "row", "row"]


STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Antic+Didone&family=Alex+Brush&display=swap",
    "/styles.css",
]


# Base Sizes
class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.25em"
    MEDIUM_SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    MEDIUM_BIGGER = "3em"
    VERY_BIG = "4em"


# Styles

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "font_size": Size.DEFAULT.value,
    "background_color": Color.BACKGROUND.value,
    "color": TextColor.DEFAULT.value,
}


NAVBAR_STYLE = {
    "background_color": Color.CONTENT.value,
    "color": TextColor.DEFAULT.value,
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.BOLD.value,
    "font_size": Size.DEFAULT.value,
}
