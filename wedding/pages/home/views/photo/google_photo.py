import reflex as rx

from wedding import urls, utils
from wedding.components import button, card, icon_section, text_section, title_section
from wedding.routes import IconRoutes as icon


def wedding_google_photos() -> rx.Component:
    """
    Create a component for opening the Google Photos album dedicated to the wedding.

    Returns:
    - rx.Component: A Reflex component designed to facilitate access to the wedding Google Photos album.

    This component includes an icon, title, descriptive paragraphs about the Google Photos album,
    and a button that, when clicked, opens the Google Photos album in a new browser window or tab.
    """

    return card(
        icon_section(icon=icon.ICON_CAMERA.value),
        title_section(title=utils.title_photo),
        text_section(text=utils.google_photo_text_one),
        text_section(text=utils.google_photo_text_two),
        button(button_name=utils.google_photo_button, url=urls.GOOGLE_FOTOS_URL),
        id="photos_section",
    )
