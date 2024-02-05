import reflex as rx

from wedding.styles import Size, style


def _capital_letter_initial(letter: str) -> rx.Component:
    """
    Creates a span with the specified capital letter and font size.

    Args:
        letter (str): The capital letter.

    Returns:
        rx.Component: The capital letter component.
    """

    return rx.span(
        letter.upper(),
        font_size=[
            Size.BIG_TITLES.value,
            Size.MEDIUM_BIGGER.value,
            Size.MEDIUM_BIGGER.value,
            Size.MEDIUM_BIGGER.value,
            Size.MEDIUM_BIGGER.value,
        ],
    )


def initials_navbar() -> rx.Component:
    """
    Creates the initials component for the navbar.

    Returns:
        rx.Component: The initials navbar component.
    """

    return rx.link(
        rx.box(
            _capital_letter_initial("V"),
            rx.span(
                "&",
                font_size="1.75em",
            ),
            _capital_letter_initial("Á"),
            style=style.INITIALS_NAVBAR_STYLE,
        ),
        href="/",
        is_external=False,
        _hover={},
    )
