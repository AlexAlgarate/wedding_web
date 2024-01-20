import reflex as rx


def image_header() -> rx.Component:
    return rx.image(
        src="/images/almendros.webp",
        width="100%",
        height="50%",
        box_shadow="0px 8px 5px 1px #F8F8FA inset",
        align_self="stretch",
        padding="-6px 12px",
    )
