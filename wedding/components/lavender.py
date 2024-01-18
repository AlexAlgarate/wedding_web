import reflex as rx

from wedding.styles import Size


def image_lavender() -> rx.Component:
    return rx.image(
        src="/images/lavanda.png",
        width="100%",
        opacity="0.80",
        margin_top=Size.LARGE.value,
        height="100%",
    )

    # rx.image(src="/bg.svg", width="100%"),
