import reflex as rx
from navaja_suiza.states.main_state import MainState


def book_item(pdf_name: str) -> rx.Component:
    return rx.el.div(
        rx.icon(
            tag="file-text",
            class_name="h-5 w-5 text-blue-400 mr-2",
        ),
        rx.el.span(pdf_name, class_name="text-gray-300"),
        rx.el.button(
            rx.icon(tag="trash-2", class_name="h-4 w-4"),
            on_click=lambda: MainState.remove_pdf(pdf_name),
            class_name="ml-auto text-red-500 hover:text-red-400 p-1 rounded-md",
            title="Eliminar PDF",
        ),
        class_name="flex items-center p-3 bg-gray-800 border border-gray-700 rounded-lg shadow-sm hover:shadow-md transition-shadow",
    )


def books_page() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "Mis Libros",
            class_name="text-3xl font-bold text-gray-100 mb-6",
        ),
        rx.upload.root(
            rx.el.div(
                rx.el.button(
                    rx.icon(
                        tag="cloud_upload",
                        class_name="mr-2",
                    ),
                    "Seleccionar Archivos PDF",
                    class_name="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors cursor-pointer font-medium",
                ),
                rx.el.p(
                    "Arrastra y suelta archivos PDF aquí o haz clic para seleccionar",
                    class_name="text-gray-400 text-sm mt-2",
                ),
                class_name="flex flex-col items-center justify-center p-6 border-2 border-dashed border-gray-600 rounded-lg hover:border-blue-500 transition-colors",
            ),
            id="pdf_upload",
            multiple=True,
            accept={"application/pdf": [".pdf"]},
            on_drop=MainState.handle_pdf_upload(
                rx.upload_files(upload_id="pdf_upload")
            ),
            class_name="mb-6",
        ),
        rx.cond(
            MainState.is_uploading,
            rx.el.div(
                rx.el.div(
                    style={
                        "width": MainState.upload_progress.to_string()
                        + "%"
                    },
                    class_name="bg-blue-500 h-2 rounded-full transition-all duration-300 ease-in-out",
                ),
                rx.el.p(
                    f"Subiendo... {MainState.upload_progress}%",
                    class_name="text-sm text-gray-300 mt-1 text-center",
                ),
                class_name="w-full bg-gray-700 rounded-full h-2 mb-4",
            ),
        ),
        rx.el.div(
            rx.foreach(
                rx.selected_files("pdf_upload"),
                lambda file: rx.el.p(
                    file,
                    class_name="text-sm text-gray-300 bg-gray-700 p-2 rounded",
                ),
            ),
            class_name="space-y-1 mb-4",
        ),
        rx.el.button(
            "Subir Seleccionados",
            on_click=MainState.handle_pdf_upload(
                rx.upload_files(upload_id="pdf_upload")
            ),
            is_loading=MainState.is_uploading,
            class_name="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-colors font-medium mb-6",
            disabled=MainState.is_uploading,
        ),
        rx.cond(
            MainState.uploaded_pdfs.length() > 0,
            rx.el.div(
                rx.el.h2(
                    "PDFs Subidos",
                    class_name="text-xl font-semibold text-gray-200 mb-4",
                ),
                rx.el.div(
                    rx.foreach(
                        MainState.uploaded_pdfs, book_item
                    ),
                    class_name="space-y-3",
                ),
                class_name="mt-6",
            ),
            rx.el.p(
                "Aún no se han subido PDFs.",
                class_name="text-gray-400",
            ),
        ),
        class_name="p-6 md:p-8",
    )