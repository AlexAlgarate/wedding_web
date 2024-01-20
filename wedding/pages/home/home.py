import reflex as rx

from wedding import utils
from wedding.components import flowers_mobile
from wedding.styles import Size, style

from .views import (
    bus_service,
    celebration,
    countdown,
    header,
    navbar,
    wedding_confirmation,
    wedding_google_photos,
)


@rx.page(title=utils.title_main, description=utils.description_main)
def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        flowers_mobile(image="/images/lavanda_arriba.png"),
        rx.vstack(
            rx.flex(
                header(),
                countdown(),
                wedding_confirmation(),
                celebration(),
                bus_service(),
                wedding_google_photos(),
                direction="column",
                gap=Size.LARGE.value,
                align="center",
                max_width=style.MAX_WIDTH,
            ),
            width="100%",
        ),
        flowers_mobile(image="/images/lavanda_abajo.png", margin_type=False),
        width="100%",
        style=style.BASE_STYLE,
        align_items="center",
    )
