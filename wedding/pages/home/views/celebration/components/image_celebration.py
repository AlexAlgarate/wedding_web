import reflex as rx

from wedding import urls as url
from wedding import utils
from wedding.styles import Size


def image_celebration() -> rx.Component:
    return image_we(image=url.AGRIPINA_PHOTO_URL, alt=utils.alt_celebration)


def image_we(image: str, alt: str) -> rx.Component:
    return rx.image(
        src=image,
        margin=Size.MEDIUM.value,
        border_radius="12px 50px",
        box_shadow="""
        inset 0 -3em 3em rgba(0, 0, 0, 0.1),
        0.3em 0.3em 1em rgba(0, 0, 0, 0.3)
        """,
        alt=alt,
        width="70%",
    )
