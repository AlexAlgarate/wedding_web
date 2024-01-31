from typing import List

import reflex as rx

from wedding.styles import style


def wedding_date_header(list_date: List[str]) -> rx.Component:
    return rx.heading(" ".join(list_date), size="2xl", style=style.WEDDING_DATE_HEADER)
