import reflex as rx

from wedding import utils
from wedding.components import navbar
from wedding.pages.contact.components.contact_box import contact_box
from wedding.routes import Route
from wedding.styles import Size, style

contact_one, contact_two = utils.contact_1, utils.contact_2


@rx.page(
    route=Route.CONTACT.value,
    title=utils.title_contact,
    description=utils.description_contact,
)
def contact() -> rx.Component:
    return rx.vstack(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        rx.box(
            rx.vstack(
                rx.text(utils.contact_header, font_size=Size.LARGE.value),
                rx.vstack(
                    contact_box(**contact_one),
                    contact_box(**contact_two),
                    width="100%",
                    padding=Size.LARGE.value,
                ),
            )
        ),
        style=style.BASE_STYLE,
        width="100%",
    )
