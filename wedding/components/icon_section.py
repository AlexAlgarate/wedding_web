from typing import Optional

import reflex as rx

from wedding.styles import Color, Size


def icon_section(icon: str, width: Optional[str] = None) -> rx.Component:
    return rx.image(
        src=icon,
        color=Color.TEXT_DEFAULT.value,
        width=width if width is not None else Size.VERY_BIG.value,
        max_height="auto",
    )
