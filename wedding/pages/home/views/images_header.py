import reflex as rx

from wedding import utils as utils
from wedding.components.images import image_header
from wedding.routes import FileRoutes as file
from wedding.styles.style import Size


def images_header(image: str) -> rx.Component:
    return rx.vstack(
        rx.center(
            image_header(image=image, alt=utils.alt_image_one),
            spacing=Size.MEDIUM.value,
            align_items="center",
            width="75%",
        ),
    )
