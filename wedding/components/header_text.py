from typing import Dict, Optional

import reflex as rx

from wedding.styles import Font, FontWeight


def header_text(text: str, style: Optional[Dict[str, str]] = None) -> rx.Component:
    return rx.heading(
        text,
        size="2xl",
        font_weight=FontWeight.MEDIUM.value,
        font_family=Font.TITLE.value,
        width="100%",
    )
