import reflex as rx

from wedding import utils as utils
from wedding.components.images_home import image_header
from wedding.routes import FileRoutes as file
from wedding.styles.style import Size


def images_header() -> rx.Component:
    return rx.vstack(
        rx.responsive_grid(
            image_header(image=file.IMAGE_HEADER_ONE.value, alt=utils.alt_image_one),
            image_header(image=file.IMAGE_HEADER_TWO.value, alt=utils.alt_image_two),
            spacing=Size.MEDIUM.value,
            columns=[1, 2],
            width="75%",
        ),
    )
