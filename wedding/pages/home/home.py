import reflex as rx

from wedding import utils
from wedding.components import divider, navbar
from wedding.pages.home.views.bus.bus import bus_service
from wedding.pages.home.views.celebration.celebration import celebration
from wedding.pages.home.views.confirmation.confirmation import wedding_confirmation
from wedding.pages.home.views.countdown.countdown import countdown
from wedding.pages.home.views.gifts.wedding_gifts import wedding_gifts
from wedding.pages.home.views.header.components.images_header import images_header
from wedding.pages.home.views.header.header import header
from wedding.pages.home.views.photo.google_photo import wedding_google_photos
from wedding.routes import FileRoutes as file
from wedding.styles import Size, style


@rx.page(title=utils.title_main, description=utils.description_main)
def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                images_header(image=file.IMAGE_HEADER_ONE.value),
                countdown(),
                images_header(image=file.IMAGE_HEADER_TWO.value),
                divider(),
                wedding_confirmation(),
                divider(),
                celebration(),
                divider(),
                bus_service(),
                # divider(),
                # wedding_gifts(),
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
