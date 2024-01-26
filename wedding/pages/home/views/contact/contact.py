import reflex as rx

from wedding import utils
from wedding.components import card, icon_section, spacer, text_section, title_section
from wedding.routes import IconRoutes as icon

from .components import create_emails_component, create_whatsapp_button


def contact() -> rx.Component:
    """
    Create a contact information section component.

    Returns:
    - rx.Component: A Reflex component representing the contact information section.
    """

    return card(
        icon_section(icon=icon.ICON_CELEBRATION.value),
        title_section(title=utils.contact_title),
        text_section(utils.contact_text_whatsapp),
        create_whatsapp_button(utils.contact_bride, utils.contact_groom),
        text_section(utils.contact_text_email),
        create_emails_component(utils.contact_bride, utils.contact_groom),
        *spacer(spacers=4),
        # rx.button("open countdown", on_click=rx.redirect("/#countdown_section")),  #TODO Prueba estados
        id="contact_section",
    )
