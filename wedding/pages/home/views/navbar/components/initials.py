import reflex as rx

from wedding.styles import Color, Font, FontWeight, Size


def _capital_letter_initial(letter: str) -> rx.Component:
    return rx.span(
        letter,
        font_size=[
            Size.BIG_TITLES.value,
            Size.MEDIUM_BIGGER.value,
            Size.MEDIUM_BIGGER.value,
            Size.MEDIUM_BIGGER.value,
            Size.MEDIUM_BIGGER.value,
        ],
    )


def initials_navbar() -> rx.Component:
    return rx.box(
        _capital_letter_initial("V"),
        rx.span(
            "&",
            font_size="1.75em",
        ),
        _capital_letter_initial("Á"),
        height="100%",
        font_weight=FontWeight.MEDIUM.value,
        color=Color.TITLES.value,
        font_family=Font.TITLE.value,
        letter_spacing="5px",
    )
