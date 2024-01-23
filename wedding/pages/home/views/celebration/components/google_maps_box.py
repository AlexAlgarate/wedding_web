import reflex as rx

from wedding import urls


def google_maps_box() -> rx.Component:
    return rx.hstack(
        rx.center(
            rx.html(
                urls.maps,
                width="100%",
            ),
        ),
        align_items="center",
    )
