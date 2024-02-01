from typing import List

import reflex as rx

from wedding.styles import style


def wedding_date_header(list_date: List[str]) -> rx.Component:
    """
    Creates a heading component for the wedding date.

    Args:
        list_date (List[str]): List of strings representing the wedding date.

    Returns:
        rx.Component: The wedding date header component.
    """

    return rx.heading(
        " ".join(list_date),
        size="2xl",
        style=style.WEDDING_DATE_HEADER,
    )
