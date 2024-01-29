import reflex as rx


def flowers_mobile(image: str, margin_type: bool = True) -> rx.Component:
    """
    Create a mobile-only component displaying an image with optional margin adjustments.

    Parameters:
    - image (str): The path or URL of the image.
    - margin_type (bool): If True, applies a specific margin for the image.

    Returns:
    - rx.Component: A Reflex component representing the mobile-only image.
    """

    return rx.mobile_only(
        rx.cond(
            margin_type,
            rx.image(
                src=image,
                width="100%",
                height="100%",
                flex_shrink="0",
                position="relative",
                margin_bottom="-120px",
                z_index="990",
            ),
            rx.image(
                src=image,
                width="100%",
                height="100%",
                flex_shrink="0",
                margin_top="-139px",
                z_index="990",
            ),
        )
    )
