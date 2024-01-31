from enum import Enum

from wedding.styles.colors import Color
from wedding.styles.fonts import Font, FontHeight, FontWeight

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
    "color": Color.DEFAULT_TEXT.value,
}

BUS_TITLE_SECTION = {
    "color": Color.TITLES.value,
    "font_weight": FontWeight.BOLD.value,
    "font_size": "1.25em",
}

CONTACT_BUTTON_STYLE = {
    "width": "100%",
    "font_size": [
        Size.DEFAULT.value,
        Size.DEFAULT.value,
        Size.DEFAULT.value,
        Size.LARGE.value,
        Size.LARGE.value,
    ],
    "padding": Size.DEFAULT.value,
    "color": Color.BACKGROUND.value,
    "background": Color.DEFAULT_TEXT.value,
    "border_radius": Size.VERY_BIG.value,
    "text_align": "center",
    "margin_bottom": Size.DEFAULT.value,
    "box_shadow": f"2px 1.5px 3px 1px {Color.PURPLE_OPACITY.value}",
    "_hover": {
        "background": "rgba(80, 69, 135, 0.81)",
        "box_shadow": "2px 1.5px 3px 1px rgba(80, 69, 135, 0.91)",
    },
}


TEXT_SECTION_STYLE = {
    "max_width": MAX_WIDTH,
    "padding": Size.SMALL.value,
    "text_align": "center",
    "font_size": [
        Size.MAIN_TEXTS.value,
        Size.MAIN_TEXTS.value,
        Size.MAIN_TEXTS.value,
        Size.MAIN_TEXTS.value,
        Size.MAIN_TEXTS.value,
    ],
    "text_wrap": "pretty",
    "font_style": "normal",
    "line_height": "normal",
    "width": "100%",
}

TITLE_STYLE = {
    "size": "xl",
    "font_weight": FontWeight.MEDIUM.value,
    "text_align": "center",
    "width": "100%",
    "letter_spacing": "0.0125rem",
    "line_height": FontHeight.MEDIUM.value,
    "font_family": Font.TITLE.value,
    "color": Color.TITLES.value,
}


SECONDARY_BUTTON_STYLE = {
    "color": Color.TITLES.value,
    "text_align": "center",
    "font_variant_numeric": "lining-nums proportional-nums",
    "padding": "8px 24px",
    "justify_content": "center",
    "align_items": "center",
    "gap": "8px",
    "align_self": "stretch",
    "border_radius": "5px",
    "border": "2px solid #4F1F7E",
    "background": Color.BACKGROUND.value,
}
