from tkinter import ttk, StringVar, constants
from services.counter_service import counter_service

#UI was developed with reference to the sample repository "todo-app".

class CounterView:

    def __init__(self, root, handle_logout):

        self._root = root
        self._handle_logout = handle_logout
        self._user = counter_service.get_user()

        self._frame = None
        self._acquisition_cost_entry = None
        self._tax_deduction_entry = None
        self._e_consumption_entry = None
        self._e_generation_entry = None
        self._e_purchase_price_entry = None
        self._savings_label = None
        self._payback_time_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _logout_handler(self):
        counter_service.logout()
        self._handle_logout()

    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame,
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command=self._logout_handler
        )

        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        logout_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _handle_create_counter(self):

        #poista
        user = counter_service.get_user()
        if user is None:
            print("Ei ole kirjautunutta käyttäjää.")
            return
        #poista

        #poista
        print(f"user: {user}, type: {type(user)}")
        print(f"user.id: {getattr(user, 'id', None)}, type: {type(getattr(user, 'id', None))}")
        #poista

        try:
            acquisition_cost = float(self._acquisition_cost_entry.get())
            tax_deduction = float(self._tax_deduction_entry.get())
            e_consumption = float(self._e_consumption_entry.get())
            e_generation = float(self._e_generation_entry.get())
            e_purchase_price = float(self._e_purchase_price_entry.get())
        except ValueError:
            self._show_error("Käytä pistettä (.) desimaalierottimena.")
            return

        counter = counter_service.save_calculation(
            self._user,
            acquisition_cost,
            tax_deduction,
            e_consumption,
            e_generation,
            e_purchase_price
        )
        self._savings_label.config(text=f"Vuotuiset säästöt: {counter.yearly_savings:.2f} eur")
        self._payback_time_label.config(text=f"Takaisinmaksuaika: {counter.payback_time:.1f} vuotta")

    def _initialize_footer(self):
        self._acquisition_cost_entry = ttk.Entry(master=self._frame)
        self._tax_deduction_entry = ttk.Entry(master=self._frame)
        self._e_consumption_entry = ttk.Entry(master=self._frame)
        self._e_generation_entry = ttk.Entry(master=self._frame)
        self._e_purchase_price_entry = ttk.Entry(master=self._frame)

        create_counter_button = ttk.Button(
            master=self._frame,
            text="Luo laskelma",
            command=self._handle_create_counter
        )

        acquisition_cost_label = ttk.Label(master=self._frame, text="Hankintahinta (eur):")
        tax_deduction_label = ttk.Label(master=self._frame, text="Verovähennys (eur):")
        e_consumption_label = ttk.Label(master=self._frame, text="Sähkönkulutus / vuosi (kWh):")
        e_generation_label = ttk.Label(master=self._frame, text="Oma sähkön tuotto / vuosi(kWh):")
        e_purchase_price_label = ttk.Label(master=self._frame, text="Sähkön ostohinta (eur/kWh):")

        acquisition_cost_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        self._acquisition_cost_entry.grid(row=1, column=1, padx=5, pady=5, sticky=constants.EW)

        tax_deduction_label.grid(row=2, column=0, padx=5, pady=5, sticky=constants.W)
        self._tax_deduction_entry.grid(row=2, column=1, padx=5, pady=5, sticky=constants.EW)

        e_consumption_label.grid(row=3, column=0, padx=5, pady=5, sticky=constants.W)
        self._e_consumption_entry.grid(row=3, column=1, padx=5, pady=5, sticky=constants.EW)

        e_generation_label.grid(row=4, column=0, padx=5, pady=5, sticky=constants.W)
        self._e_generation_entry.grid(row=4, column=1, padx=5, pady=5, sticky=constants.EW)

        e_purchase_price_label.grid(row=5, column=0, padx=5, pady=5, sticky=constants.W)
        self._e_purchase_price_entry.grid(row=5, column=1, padx=5, pady=5, sticky=constants.EW)

        create_counter_button.grid(
            row=6,
            column=0,
            columnspan=2,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        self._savings_label = ttk.Label(master=self._frame, text="Vuotuiset säästöt: ")
        self._payback_time_label = ttk.Label(master=self._frame, text="Takaisinmaksuaika: ")

        self._savings_label.grid(row=7, column=0, padx=5, pady=5, sticky=constants.W)
        self._payback_time_label.grid(row=8, column=0, padx=5, pady=5, sticky=constants.W)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)
        self._error_label.grid_remove()


        self._initialize_header()
        self._initialize_footer()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
