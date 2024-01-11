import reflex as rx

import wedding.utils as utils

from .components import flamingo_header, header_text, wedding_date_header


def header() -> rx.Component:
    return rx.box(
        flamingo_header(),
        rx.vstack(
            rx.hstack(
                header_text(utils.title_header),
            ),
            rx.hstack(
                wedding_date_header(list_date=utils.wedding_date),
                width="100%",
            ),
        ),
        display="flex",
        flex_direction="column",
        justify_content="center",
        align_items="center",
    )
