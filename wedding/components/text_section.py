from typing import Optional
import reflex as rx

from wedding.styles import style, FontWeight


def text_section(
    text: str, font_weight: Optional[str] = FontWeight.LIGHT.value
) -> rx.Component:
    return rx.text(text, font_weight=font_weight, style=style.TEXT_SECTION_STYLE)
