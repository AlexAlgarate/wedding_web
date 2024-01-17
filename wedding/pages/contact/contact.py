import reflex as rx

from wedding import utils
from wedding.components import navbar
from wedding.pages.contact.components.contact_box import contact_box
from wedding.routes import Route
from wedding.styles import Size, style


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
                    contact_box(**utils.contact_bride),
                    contact_box(**utils.contact_groom),
                    width="100%",
                    padding=Size.LARGE.value,
                ),
            )
        ),
        style=style.BASE_STYLE,
        width="100%",
    )
