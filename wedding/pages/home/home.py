import reflex as rx

from wedding import utils
from wedding.components import divider, navbar
from wedding.routes import FileRoutes
from wedding.styles import Size, style

from .views import (
    bus_service,
    celebration,
    countdown,
    header,
    images_header,
    wedding_confirmation,
    wedding_google_photos,
)


@rx.page(title=utils.title_main, description=utils.description_main)
def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                images_header(image=FileRoutes.IMAGE_HEADER_ONE.value),
                countdown(),
                images_header(image=FileRoutes.IMAGE_HEADER_TWO.value),
                divider(),
                wedding_confirmation(),
                divider(),
                celebration(),
                divider(),
                bus_service(),
                divider(),
                wedding_google_photos(),
                max_width=style.MAX_WIDTH,
                margin=Size.DEFAULT.value,
            ),
            width="100%",
            padding=Size.MEDIUM.value,
            style=style.BASE_STYLE,
        ),
    )
