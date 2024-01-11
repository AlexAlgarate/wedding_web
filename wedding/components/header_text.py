from typing import Dict

import reflex as rx

from wedding.styles import Size
from wedding.styles.fonts import Font, FontWeight


def header_text(text: str, style: Dict[str, str]) -> rx.Component:
    return rx.text(
        text,
        font_size=[
            Size.MEDIUM_BIGGER.value,
            Size.MEDIUM_BIGGER.value,
            Size.VERY_BIG.value,
            Size.VERY_BIG.value,
            Size.VERY_BIG.value,
        ],
        font_weight=FontWeight.MEDIUM.value,
        font_family=Font.TITLE.value,
        width="100%",
        style=style,
    )
