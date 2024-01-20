from typing import List

import reflex as rx

from wedding.styles import Font, FontWeight


def wedding_date_header(list_date: List[str]) -> rx.Component:
    return rx.heading(
        " ".join(list_date),
        size="2xl",
        font_family=Font.TITLE.value,
        width="100%",
        font_weight=FontWeight.MEDIUM.value,
        font_style="normal",
        text_align="center",
    )
