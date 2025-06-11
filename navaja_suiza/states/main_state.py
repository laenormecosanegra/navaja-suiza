import reflex as rx


class MainState(rx.State):
    current_page: str = "books"
    is_mobile_menu_open: bool = False
    uploaded_pdfs: list[str] = []
    upload_progress: int = 0
    is_uploading: bool = False
    contacts: list[dict[str, str]] = [
        {
            "name": "Juan Pérez",
            "phone": "123-456-7890",
            "email": "juan.perez@example.com",
        },
        {
            "name": "Ana García",
            "phone": "098-765-4321",
            "email": "ana.garcia@example.com",
        },
    ]
    new_contact_name: str = ""
    new_contact_phone: str = ""
    new_contact_email: str = ""
    show_add_contact_form: bool = False
    calendar_events: list[dict[str, str]] = [
        {
            "date": "2024-07-15",
            "title": "Reunión de Equipo",
        },
        {
            "date": "2024-07-20",
            "title": "Entrega de Proyecto",
        },
    ]

    @rx.event
    def set_page(self, page_name: str):
        self.current_page = page_name

    @rx.event
    def toggle_mobile_menu(self):
        self.is_mobile_menu_open = (
            not self.is_mobile_menu_open
        )

    @rx.event
    def close_mobile_menu(self):
        self.is_mobile_menu_open = False

    @rx.event
    async def handle_pdf_upload(
        self, files: list[rx.UploadFile]
    ):
        self.is_uploading = True
        self.upload_progress = 0
        for i, file in enumerate(files):
            if file.content_type != "application/pdf":
                yield rx.toast(
                    "Solo se permiten archivos PDF.",
                    duration=3000,
                )
                continue
            upload_data = await file.read()
            upload_dir = rx.get_upload_dir()
            if not upload_dir.exists():
                upload_dir.mkdir(
                    parents=True, exist_ok=True
                )
            outfile = upload_dir / file.name
            with outfile.open("wb") as file_object:
                file_object.write(upload_data)
            self.uploaded_pdfs.append(file.name)
            self.upload_progress = int(
                (i + 1) / len(files) * 100
            )
            yield
        self.is_uploading = False
        self.upload_progress = 100
        yield rx.toast("¡Subida completada!", duration=3000)
        yield rx.clear_selected_files("pdf_upload")

    @rx.event
    def toggle_add_contact_form(self):
        self.show_add_contact_form = (
            not self.show_add_contact_form
        )
        if not self.show_add_contact_form:
            self.new_contact_name = ""
            self.new_contact_phone = ""
            self.new_contact_email = ""

    @rx.event
    def add_contact(self, form_data: dict):
        name = form_data.get("name", "").strip()
        phone = form_data.get("phone", "").strip()
        email = form_data.get("email", "").strip()
        if name and (phone or email):
            self.contacts.append(
                {
                    "name": name,
                    "phone": phone,
                    "email": email,
                }
            )
            self.show_add_contact_form = False
            self.new_contact_name = ""
            self.new_contact_phone = ""
            self.new_contact_email = ""
        else:
            yield rx.toast(
                "Se requiere el nombre y al menos un método de contacto (teléfono o correo electrónico).",
                duration=3000,
            )

    @rx.event
    def remove_pdf(self, pdf_name: str):
        self.uploaded_pdfs = [
            pdf
            for pdf in self.uploaded_pdfs
            if pdf != pdf_name
        ]

    @rx.event
    def remove_contact(self, contact_name: str):
        self.contacts = [
            c
            for c in self.contacts
            if c["name"] != contact_name
        ]

    @rx.event
    def set_new_contact_name(self, name: str):
        self.new_contact_name = name

    @rx.event
    def set_new_contact_phone(self, phone: str):
        self.new_contact_phone = phone

    @rx.event
    def set_new_contact_email(self, email: str):
        self.new_contact_email = email