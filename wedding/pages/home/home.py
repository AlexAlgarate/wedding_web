import reflex as rx

from wedding import utils
from wedding.components import flowers_mobile
from wedding.routes import FileRoutes
from wedding.styles import Size, style

from .views import (
    bus_service,
    celebration,
    contact,
    countdown,
    header,
    navbar,
    wedding_confirmation,
    wedding_gifts,
    wedding_google_photos,
)


class State(rx.State):
    ...


@rx.page(title=utils.title_main, description=utils.description_main)
def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        flowers_mobile(image=FileRoutes.LAVENDER_TOP.value),
        rx.vstack(
            rx.flex(
                header(),
                countdown(),
                wedding_confirmation(),
                celebration(),
                wedding_gifts(),
                bus_service(),
                wedding_google_photos(),
                contact(),
                direction="column",
                gap=Size.LARGE.value,
                align="center",
                width="100%",
                max_width=style.MAX_WIDTH,
            ),
            width="auto",
        ),
        flowers_mobile(image=FileRoutes.LAVENDER_BOTTOM.value, margin_type=False),
        width="100%",
        style=style.BASE_STYLE,
        align_items="center",
    )
