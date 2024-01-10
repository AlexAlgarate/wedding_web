import reflex as rx

from wedding import utils
from wedding.components.navbar import navbar
from wedding.pages.home.views.countdown.countdown import countdown
from wedding.pages.home.views.header.flamingo_image import flamingo_header
from wedding.pages.home.views.header.header import header
from wedding.pages.home.views.images_header import images_header
from wedding.pages.home.views.main_text import main_text
from wedding.pages.home.views.sections import bus_icon, title_section
from wedding.routes import FileRoutes as file
from wedding.styles import Size, style
from wedding.styles.colors import Color, TextColor
from wedding.styles.fonts import Font, FontWeight

BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "font_size": Size.DEFAULT.value,
    "background_color": Color.BACKGROUND.value,
    "color": TextColor.DEFAULT.value,
}


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
                title_section("Ceremonia y Celebración"),
                bus_icon(),
                rx.spacer(),
                title_section("Servicio de autobuses"),
                bus_icon(),
                rx.spacer(),
                title_section("Confirmación"),
                bus_icon(),
                main_text("Blablblá Juan es un calvo que se parece a Melitón"),
                rx.spacer(),
                title_section("Lista de regalos"),
                bus_icon(),
                main_text("Blablblá Juan es un calvo que se parece a Melitón"),
                rx.spacer(),
                title_section("Albúm de fotos"),
                bus_icon(),
                main_text(
                    "Publica fotos subiéndolas al albúm compartido de Google Fotos de los novios."
                ),
                max_width=style.MAX_WIDTH,
                margin=Size.DEFAULT.value,
            ),
            width="100%",
            padding=Size.MEDIUM.value,
            style=BASE_STYLE,
        ),
    )
