import reflex as rx

from wedding import utils
from wedding.components.navbar import navbar
from wedding.pages.home.views.countdown import countdown
from wedding.pages.home.views.flamingo_image import flamingo_header
from wedding.pages.home.views.header import header
from wedding.pages.home.views.images_header import images_header
from wedding.pages.home.views.main_text import main_text
from wedding.routes import FileRoutes as file
from wedding.styles import style
from wedding.styles.style import Size


@rx.page(title=utils.title_main, description=utils.description_main)
def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        rx.center(
            rx.vstack(
                flamingo_header(),
                header(),
                images_header(image=file.IMAGE_HEADER_ONE.value),
                countdown(),
                images_header(image=file.IMAGE_HEADER_TWO.value),
                main_text(),
                max_width=style.MAX_WIDTH,
                margin=Size.DEFAULT.value,
            ),
            width="100%",
            padding=Size.MEDIUM.value,
        ),
    )
