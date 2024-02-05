import reflex as rx

from wedding.styles import style


def title_header() -> rx.Component:
    """
    Creates a flex container for the title header.

    Returns:
        rx.Component: The title header component.
    """

    return rx.vstack(
        rx.mobile_and_tablet(
            rx.flex(
                _title("¡Nos"),
                _title("casamos!"),
                direction="column",
                align="center",
            ),
            margin_top="-85px",
        ),
        rx.desktop_only(
            rx.flex(
                _title("¡Nos"),
                _title("casamos!"),
                direction="column",
                align="center",
            )
        ),
    )


def _title(text: str) -> rx.Component:
    """
    Creates a heading component with the specified text and style.

    Args:
        text (str): The text for the heading.

    Returns:
        rx.Component: The heading component.
    """

    return rx.heading(
        text,
        size="2xl",
        style=style.TEXT_HEADER_STYLE,
    )
