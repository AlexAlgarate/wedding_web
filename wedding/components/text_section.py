from typing import Optional

import reflex as rx

from wedding.styles import FontWeight, style


def text_section(
    text: str, font_weight: Optional[str] = FontWeight.LIGHT.value
) -> rx.Component:
    """
    Creates a text section with the specified text and optional font weight.

    Args:
        text (str): The text content.
        font_weight (Optional[str]): The font weight. Defaults to FontWeight.LIGHT.value.

    Returns:
        rx.Component: The text section component.
    """

    return rx.text(text, font_weight=font_weight, style=style.TEXT_SECTION_STYLE)
