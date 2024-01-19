import reflex as rx

from wedding import icon, url, utils
from wedding.components import (
    button,
    card,
    divider,
    icon_section,
    text_paragraph,
    title_section,
)


def wedding_google_photos() -> rx.Component:
    return card(
        title_section(title=utils.title_photo),
        icon_section(icon=icon.ICON_CAMERA.value),
        divider(width="50%", section=False),
        text_paragraph(text=utils.google_photo_text_one),
        text_paragraph(text=utils.google_photo_text_two),
        button(button_name=utils.google_photo_button, url=url.GOOGLE_FOTOS_URL),
    )


# def wedding_google_photos() -> rx.Component:
#     return rx.flex(
#         title_section(title=utils.title_photo),
#         icon_section(icon=icon.ICON_CAMERA.value),
#         divider(width="50%", section=False),
#         text_paragraph(text=utils.google_photo_text_one),
#         text_paragraph(text=utils.google_photo_text_two),
#         button(button_name=utils.google_photo_button, url=url.GOOGLE_FOTOS_URL),
#         direction="column",
#         align="center",
#         gap="8px",
#         padding="16px 16px",
#         margin_x=Size.MEDIUM.value,
#         justify_content="center",
#         border_radius="12px",
#         box_shadow="0px 2px 4px 0px rgba(0, 0, 0, 0.25)",
#     )


# border-radius: 12px;
# background: #FCFCFD;
# box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.25);

# def wedding_google_photos() -> rx.Component:
#     return rx.box(
#         rx.center(
#             rx.vstack(
#                 title_section(title=utils.title_photo),
#                 icon_section(icon=icon.ICON_CAMERA.value),
#                 divider(width="50%", section=False),
#                 rx.flex(
#                     text_paragraph(text=utils.google_photo_text_one),
#                     text_paragraph(text=utils.google_photo_text_two),
#                     direction="column",
#                     align="center",
#                 ),
#                 button(button_name=utils.google_photo_button, url=url.GOOGLE_FOTOS_URL),
#             ),
#             width="100%",
#         )
#     )
