import reflex as rx
from navaja_suiza.states.main_state import MainState
from navaja_suiza.states.auth_state import AuthState


def sidebar_button(
    text: str, icon_name: str, page_name: str
) -> rx.Component:
    return rx.el.button(
        rx.icon(tag=icon_name, class_name="mr-2 h-5 w-5"),
        text,
        on_click=[
            lambda: MainState.set_page(page_name),
            MainState.close_mobile_menu,
        ],
        class_name=rx.cond(
            MainState.current_page == page_name,
            "w-full flex items-center justify-start px-4 py-3 text-sm font-medium text-white bg-blue-600 rounded-lg",
            "w-full flex items-center justify-start px-4 py-3 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white rounded-lg",
        ),
    )


def sidebar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                tag="layout-dashboard",
                class_name="h-8 w-8 text-blue-500",
            ),
            rx.el.h2(
                "Navaja Suiza",
                class_name="text-2xl font-bold text-gray-100 ml-2",
            ),
            class_name="hidden md:flex items-center p-4 border-b border-gray-700",
        ),
        rx.el.nav(
            sidebar_button("Libros", "book-open", "books"),
            sidebar_button("Agenda", "contact", "agenda"),
            sidebar_button(
                "Calendario", "calendar-days", "calendar"
            ),
            sidebar_button(
                "Chat IA", "message-circle", "chat"
            ),
            class_name="flex flex-col space-y-2 p-4 flex-grow",
        ),
        rx.el.div(
            rx.el.button(
                rx.icon(
                    tag="log-out", class_name="mr-2 h-5 w-5"
                ),
                "Cerrar Sesión",
                on_click=AuthState.sign_out,
                class_name="w-full flex items-center justify-start px-4 py-3 text-sm font-medium text-gray-300 hover:bg-red-600 hover:text-white rounded-lg transition-colors",
            ),
            class_name="p-4 border-t border-gray-700",
        ),
        class_name=rx.cond(
            MainState.is_mobile_menu_open,
            "fixed top-0 left-0 z-50 h-screen w-64 flex flex-col bg-gray-800 border-r border-gray-700 transition-transform transform translate-x-0",
            "fixed top-0 left-0 z-50 h-screen w-64 flex flex-col bg-gray-800 border-r border-gray-700 transition-transform transform -translate-x-full md:translate-x-0",
        ),
    )