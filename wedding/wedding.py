import reflex as rx

from wedding import utils
from wedding.components import (
    farewell_message,
    flowers_between_section,
    lavender_flowers,
    navbar,
)
from wedding.routes import FileRoutes
from wedding.styles import style

from .views import contact  # wedding_gifts,
from .views import (
    bus_service,
    celebration,
    countdown,
    header,
    wedding_confirmation,
    wedding_google_photos,
)


@rx.page(title=utils.title_main, description=utils.description_main)
def index() -> rx.Component:
    return rx.vstack(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        lavender_flowers(image=FileRoutes.IMAGE_LAVENDER_TOP.value),
        rx.vstack(
            rx.flex(
                header(),
                countdown(),
                flowers_between_section(),
                wedding_confirmation(),
                celebration(),
                # wedding_gifts(),
                bus_service(),
                flowers_between_section(),
                contact(),
                flowers_between_section(),
                wedding_google_photos(),
                direction="column",
                gap="16px",
                align="center",
                width="100%",
                max_width=style.MAX_WIDTH,
            ),
            width="auto",
        ),
        farewell_message(),
        lavender_flowers(
            image=FileRoutes.IMAGE_LAVENDER_BOTTOM.value,
            margin_type=False,
        ),
        align="center",
        width="100%",
        style=style.BASE_STYLE,
        align_items="center",
    )


app = rx.App(stylesheets=style.STYLESHEETS)
