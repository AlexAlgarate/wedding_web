from enum import Enum

from wedding.styles.colors import Color
from wedding.styles.fonts import Font, FontWeight

# Constants


MAX_WIDTH = "800px"
FLEX_DIRECTION = ["column", "column", "column", "row", "row"]

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Antic+Didone&family=Alex+Brush&family=Elsie&family=Raleway&display=swap",
    "/styles.css",
]


# Base Sizes


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.25em"
    MEDIUM_SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    MAIN_TEXTS = "1.15em"
    LARGE = "1.5em"
    BIG = "2em"
    BIG_TITLES = "2.5em"
    MEDIUM_BIGGER = "3em"
    VERY_BIG = "4em"


# Styles


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "font_size": Size.DEFAULT.value,
    "background_color": Color.BACKGROUND.value + "!important",
    "color": Color.TEXT_DEFAULT.value,
}

style_title_bus = {
    "color": Color.TEXT_DEFAULT.value,
    "font_weight": FontWeight.BOLD.value,
    "font_size": "1.25em",
}
