import reflex as rx
from navaja_suiza.states.main_state import MainState


def calendar_event_item(
    event: dict[str, str],
) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            event["date"],
            class_name="text-sm font-semibold text-blue-400",
        ),
        rx.el.p(
            event["title"],
            class_name="text-md text-gray-300",
        ),
        class_name="p-3 bg-gray-800 border border-gray-700 rounded-lg shadow-sm",
    )


def calendar_page() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "Mi Calendario",
            class_name="text-3xl font-bold text-gray-100 mb-6",
        ),
        rx.el.p(
            "La funcionalidad del calendario está en desarrollo.",
            class_name="text-gray-300 mb-4",
        ),
        rx.el.h2(
            "Próximos Eventos (Marcador de posición)",
            class_name="text-xl font-semibold text-gray-200 mb-3",
        ),
        rx.cond(
            MainState.calendar_events.length() > 0,
            rx.el.div(
                rx.foreach(
                    MainState.calendar_events,
                    calendar_event_item,
                ),
                class_name="space-y-2",
            ),
            rx.el.p(
                "No hay eventos programados.",
                class_name="text-gray-400",
            ),
        ),
        rx.el.div(
            rx.el.input(
                placeholder="Fecha del Evento (AAAA-MM-DD)",
                name="event_date",
                class_name="p-2 border border-gray-600 rounded mr-2 bg-gray-700 text-gray-100 placeholder-gray-400",
            ),
            rx.el.input(
                placeholder="Título del Evento",
                name="event_title",
                class_name="p-2 border border-gray-600 rounded mr-2 bg-gray-700 text-gray-100 placeholder-gray-400",
            ),
            rx.el.button(
                "Añadir Evento (prueba)",
                class_name="px-3 py-2 bg-blue-500 text-white rounded hover:bg-blue-600",
            ),
            class_name="mt-6 p-4 border-t border-gray-700",
        ),
        class_name="p-6 md:p-8",
    )