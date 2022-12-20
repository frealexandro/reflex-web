"""UI and logic for the navbar component."""

import pynecone as pc

from pcweb import constants, styles
from pcweb.base_state import State
from pcweb.components.logo import logo
from pcweb.components.sidebar import sidebar as sb
from pcweb.pages.docs.gallery import gallery
from pcweb.pages.docs.getting_started import introduction
from pcweb.pages.index import index


class NavbarState(State):
    """The state for the navbar component."""

    # Whether the sidebar is open.
    sidebar_open: bool = False

    def toggle_sidebar(self):
        """Toggle the sidebar open state."""
        self.sidebar_open = not self.sidebar_open


# Styles to use for the navbar.
logo_style = {
    "width": "3.21em",
    "height": "3em",
}
logo = logo(**logo_style)

button_style = {
    "color": styles.DOC_REG_TEXT_COLOR,
    "_hover": {"color": styles.ACCENT_COLOR, "text_decoration": "none"},
}


def navbar(sidebar: pc.Component = None) -> pc.Component:
    """Create the navbar component.

    Args:
        sidebar: The sidebar component to use.
    """
    # If the sidebar is not provided, create a default one.
    sidebar = sidebar or sb()

    # Create the navbar component.
    return pc.box(
        pc.hstack(
            pc.link(
                pc.hstack(
                    logo,
                    pc.tablet_and_desktop(
                        pc.text(
                            "Pynecone",
                            font_size=styles.H3_FONT_SIZE,
                            font_weight=600,
                        ),
                    ),
                    spacing="0.25em",
                ),
                href=index.path,
                _hover={"text_decoration": "none"},
            ),
            pc.hstack(
                pc.tablet_and_desktop(
                    pc.link(
                        pc.text(
                            "Docs",
                        ),
                        href=introduction.path,
                        **button_style,
                    ),
                ),
                pc.tablet_and_desktop(
                    pc.link(
                        pc.text(
                            "Gallery",
                        ),
                        href=gallery.path,
                        **button_style,
                    ),
                ),
                pc.desktop_only(
                    pc.menu(
                        pc.hstack(
                            pc.menu_button(
                                "Reference",
                                pc.icon(tag="ChevronDownIcon"),
                                color=styles.DOC_REG_TEXT_COLOR,
                                _hover={"color": styles.ACCENT_COLOR},
                            ),
                        ),
                        pc.menu_list(
                            pc.link(
                                pc.menu_item(
                                    "Components",
                                    _hover={"background_color": "white"},
                                    _focus={},
                                ),
                                _hover={"color": styles.ACCENT_COLOR},
                                href="/docs/library",
                            ),
                            pc.link(
                                pc.menu_item(
                                    "Hosting", _hover={"background_color": "white"}
                                ),
                                _hover={"color": styles.ACCENT_COLOR},
                                href="/docs/hosting/deploy",
                            ),
                        ),
                    )
                ),
                pc.desktop_only(
                    pc.link(
                        pc.image(src="/github.png", height="1.25em"),
                        href=constants.GITHUB_URL,
                    ),
                ),
                pc.mobile_and_tablet(
                    pc.icon(
                        tag="HamburgerIcon",
                        on_click=NavbarState.toggle_sidebar,
                        width="1.5em",
                        height="1.5em",
                        _hover={
                            "cursor": "pointer",
                            "color": styles.ACCENT_COLOR,
                        },
                    ),
                ),
                spacing="1em",
            ),
            pc.drawer(
                pc.drawer_overlay(
                    pc.drawer_content(
                        pc.hstack(
                            logo,
                            pc.icon(
                                tag="CloseIcon",
                                on_click=NavbarState.toggle_sidebar,
                                width="4em",
                                _hover={
                                    "cursor": "pointer",
                                    "color": styles.ACCENT_COLOR,
                                },
                            ),
                            justify="space-between",
                            margin_bottom="1.5em",
                        ),
                        sidebar if sidebar is not None else pc.text("Sidebar"),
                        padding_x="2em",
                        padding_top="2em",
                        bg="rgba(255,255,255, 0.97)",
                    ),
                    bg="rgba(255,255,255, 0.5)",
                ),
                placement="left",
                is_open=NavbarState.sidebar_open,
                on_close=NavbarState.toggle_sidebar,
                bg="rgba(255,255,255, 0.5)",
            ),
            justify="space-between",
            padding_x=styles.PADDING_X,
        ),
        bg="rgba(255,255,255, 0.8)",
        backdrop_filter="blur(6px)",
        padding_y=["0.8em", "0.8em", "0.5em"],
        border_bottom="0.05em solid rgba(100, 116, 139, .1)",
        position="sticky",
        width="100%",
        top="0px",
        z_index="99",
    )