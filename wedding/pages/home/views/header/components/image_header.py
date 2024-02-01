import reflex as rx

from wedding import utils
from wedding.routes import FileRoutes
from wedding.styles import style


def image_header() -> rx.Component:
    """
    Creates an image component for the header.

    Returns:
        rx.Component: The header image component.
    """

    return rx.image(
        src=FileRoutes.IMAGE_HEADER.value,
        alt=utils.alt_image_partners,
        style=style.IMAGE_HEADER,
    )
