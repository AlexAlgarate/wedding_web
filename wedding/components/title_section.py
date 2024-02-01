import reflex as rx

from wedding.styles import style


def title_section(title: str) -> rx.Component:
    """
    Creates a title section with the specified title.

    Args:
        title (str): The title text.

    Returns:
        rx.Component: The title section component.
    """

    return rx.heading(title, style=style.TITLE_STYLE)
