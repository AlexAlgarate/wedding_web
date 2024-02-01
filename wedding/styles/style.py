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


# Styles
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


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "font_size": Size.DEFAULT.value,
    "background_color": Color.BACKGROUND.value + "!important",
    "color": Color.DEFAULT_TEXT.value,
}


NAVBAR_STYLE = {
    "box_shadow": f"0px 1px 5px 1px {Color.PURPLE_OPACITY.value}",
    "position": "sticky",
    "padding_top": "0.75em",
    "padding_bottom": Size.ZERO.value,
    "z_index": "5",
    "justify_content": "center",
    "justify": "center",
    "top": "0",
    "background_color": Color.CONTENT.value,
    "width": "100%",
}


INITIALS_NAVBAR_STYLE = {
    "height": "100%",
    "font_weight": FontWeight.MEDIUM.value,
    "color": Color.TITLES.value,
    "font_family": Font.TITLE.value,
    "letter_spacing": "5px",
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


MAIN_BUTTON_STYLE = {
    "width": "100%",
    "font_size": [
        Size.DEFAULT.value,
        Size.DEFAULT.value,
        Size.DEFAULT.value,
        Size.LARGE.value,
        Size.LARGE.value,
    ],
    "padding": "8px 24px",
    "color": Color.BACKGROUND.value,
    "background": Color.BUTTONS.value,
    "border_radius": "5px",
    "border": "2px solid #4F1F7E",
    "text_align": "center",
    "margin_bottom": Size.DEFAULT.value,
    "_hover": {
        "background": "rgba(80, 69, 135, 0.91)",
    },
}


BUS_TITLE_SECTION = {
    "color": Color.TITLES.value,
    "font_weight": FontWeight.BOLD.value,
    "font_size": "1.25em",
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
    "font_size": [
        Size.DEFAULT.value,
        Size.DEFAULT.value,
        Size.DEFAULT.value,
        Size.LARGE.value,
        Size.LARGE.value,
    ],
}


COUNTDOWN_BAR_STYLE = {
    "padding": "16px 0px",
    "gap": "1.5em",
    "align_self": "stretch",
    "background": Color.COUNTDOWN_BACKGROUND.value,
    "width": "100%",
}


COUNTDOWN_NUMBERS_STYLE = {
    "color": Color.NUMBERS_COUNTDOWN.value,
    "width": "100%",
    "height": "100%",
    # "border": "2px",
    "font_family": Font.TITLE.value,
    "text_align": "center",
    "font_style": "normal",
    "font_weight": FontWeight.MEDIUM_INSIDE_TEXTS.value,
    "line_height": FontHeight.NORMAL.value,
    "font_size": [
        Size.BIG.value,
        Size.BIG.value,
        Size.BIG.value,
        Size.BIG.value,
        Size.BIG.value,
    ],
}


COUNTDOWN_TEXT_STYLE = {
    "color": Color.TEXT_COUNTDOWN.value,
    "text_align": "center",
    "font_family": Font.DEFAULT.value,
    "font_size": "16px",
    "font_style": "normal",
    "font_weight": FontWeight.MEDIUM_INSIDE_TEXTS.value,
    "line_height": FontHeight.NORMAL.value,
}


TEXT_HEADER_STYLE = {
    "font_family": Font.TITLE.value,
    "font_weight": FontWeight.MEDIUM.value,
    "font_style": "normal",
    "line_height": "normal",
    "color": Color.TITLES.value,
}


IMAGE_HEADER = {
    "width": "100%",
    "height": "50%",
    "box_shadow": "0px 8px 5px 1px #F8F8FA inset",
    "align_self": "stretch",
    "padding": "-6px 12px",
}


WEDDING_DATE_HEADER = {
    "font_family": Font.TITLE.value,
    "width": "100%",
    "font_weight": FontWeight.MEDIUM.value,
    "font_style": "normal",
    "text_align": "center",
    "color": Color.TITLES.value,
}


BOTTOM_TEXT_STYLE = {
    "font_family": Font.TITLE.value,
    "font_weight": FontWeight.MEDIUM.value,
    "font_style": "normal",
    "line_height": "normal",
    "color": Color.TITLES.value,
    "position": "relative",
    "top": "50px",
}
