from tkinter import ttk, StringVar, constants
from services.counter_service import counter_service, UsernameExistsError

#UI was developed with reference to the sample repository "todo-app".

class CreateUserView:

    def __init__(self, root, handle_create_user, handle_show_login_view):

        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_show_login_view = handle_show_login_view
        self._frame = None

        self._username_entry = None
        self._password_entry = None
        self._password_confirm_entry = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        password_confirm = self._password_confirm_entry.get()

        if password != password_confirm:
            self._show_error("Salasanat eivät täsmää.")
            return

        if len(password) < 1:
            self._show_error("Salasana ei voi olla tyhjä.")
            return

        try:
            counter_service.create_user(username, password)
            self._handle_create_user()
        except UsernameExistsError:
            self._show_error("Käyttäjänimi on jo käytössä.")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Salasana")

        self._password_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_confirm_field(self):
        password_label = ttk.Label(master=self._frame, text="Salasana uudestaan")

        self._password_confirm_entry = ttk.Entry(master=self._frame)

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_confirm_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading = ttk.Label(master=self._frame, text="Luo uusi käyttäjä", font=("Helvetica", 16))
        heading.grid(row=0, column=0, columnspan=2, pady=10)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()
        self._initialize_password_confirm_field()

        create_user_button = ttk.Button(
            master=self._frame,
            text="Luo käyttäjä",
            command=self._create_user_handler
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._handle_show_login_view
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()
