import reflex as rx

from wedding.styles import Size


def image_web(image: str, alt: str) -> rx.Component:
    return rx.image(
        src=image,
        margin_bottom=Size.MEDIUM.value,
        border_radius="12px 50px",
        box_shadow="""
        inset 0 -3em 3em rgba(0, 0, 0, 0.1),
        0.3em 0.3em 1em rgba(0, 0, 0, 0.3)
        """,
        alt=alt,
    )
