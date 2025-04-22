"""Aurinkopaneelilaskurin ja aiempien laskelmien näyttämisestä vastaava näkymä."""

from tkinter import ttk, StringVar, constants
from services.counter_service import counter_service

#UI was developed with reference to the sample repository "todo-app".

class CounterView:
    """Aurinkopaneelilaskurin ja aiempien laskelmien näyttämisestä vastaava näkymä."""

    def __init__(self, root, handle_logout, user):
        """Luokan konstruktori. Alustaa uuden CounterView-näkymän.

        Args:
            root:
            TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_logout:
            Funktio, jota kutsutaan uloskirjautumisen yhteydessä.
            user:
            Sisäänkirjautunut käyttäjä, jonka laskelmia näkymässä käsitellään.
        """

        self._root = root
        self._handle_logout = handle_logout
        self._user = user

        self._frame = None
        self._acquisition_cost_entry = None
        self._tax_deduction_entry = None
        self._net_cost_label = None
        self._e_consumption_entry = None
        self._e_generation_entry = None
        self._e_purchase_price_entry = None
        self._savings_label = None
        self._payback_time_label = None
        self._previous_calculations_label = None

        self._acquisition_cost_var = StringVar()
        self._tax_deduction_var = StringVar()

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
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

        try:

            acquisition_cost = float(self._acquisition_cost_entry.get())
            tax_deduction = float(self._tax_deduction_entry.get())
            e_consumption = float(self._e_consumption_entry.get())
            e_generation = float(self._e_generation_entry.get())
            e_purchase_price = float(self._e_purchase_price_entry.get())

        except ValueError as e:
            print("ValueError:", e)
            self._show_error("Anna arvo kaikkiin kenttiin. " \
            "Jos kenttään ei ole arvoa, syötä 0. " \
            "Käytä pistettä (.) desimaalierottimena.")
            return

        net_cost = acquisition_cost - tax_deduction
        self._net_cost_label.config(text=f"{net_cost:.2f}")

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

    #generoitu koodi alkaa
    def _update_net_cost(self):
        try:
            acquisition_cost = float(self._acquisition_cost_var.get().strip())
            tax_deduction = float(self._tax_deduction_var.get().strip())
            net_cost = acquisition_cost - tax_deduction
            self._net_cost_label.config(text=f"{net_cost:.2f}")
        except ValueError:
            self._net_cost_label.config(text="-")
    #generoitu koodi loppuu

    def _initialize_footer(self):
        self._acquisition_cost_entry = ttk.Entry(master=self._frame, textvariable=self._acquisition_cost_var)
        self._tax_deduction_entry = ttk.Entry(master=self._frame, textvariable=self._tax_deduction_var)
        self._e_consumption_entry = ttk.Entry(master=self._frame)
        self._e_generation_entry = ttk.Entry(master=self._frame)
        self._e_purchase_price_entry = ttk.Entry(master=self._frame)

        #generoitu koodi alkaa
        self._acquisition_cost_var.trace_add("write", lambda *args: self._update_net_cost())
        self._tax_deduction_var.trace_add("write", lambda *args: self._update_net_cost())
        #generoitu koodi loppuu

        create_counter_button = ttk.Button(
            master=self._frame,
            text="Luo laskelma",
            command=self._handle_create_counter
        )

        acquisition_cost_label = ttk.Label(master=self._frame, text="Hankintahinta (eur):")
        tax_deduction_label = ttk.Label(master=self._frame, text="Verovähennys (eur):")
        net_cost_label = ttk.Label(master=self._frame, text="Kustannus: ")
        e_consumption_label = ttk.Label(master=self._frame, text="Sähkönkulutus / vuosi (kWh):")
        e_generation_label = ttk.Label(master=self._frame, text="Oma sähkön tuotto / vuosi (kWh):")
        e_purchase_price_label = ttk.Label(master=self._frame, text="Sähkön ostohinta (eur/kWh):")

        self._net_cost_label = ttk.Label(master=self._frame, text="0.00 eur")

        acquisition_cost_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        self._acquisition_cost_entry.grid(row=1, column=1, padx=5, pady=5, sticky=constants.EW)

        tax_deduction_label.grid(row=2, column=0, padx=5, pady=5, sticky=constants.W)
        self._tax_deduction_entry.grid(row=2, column=1, padx=5, pady=5, sticky=constants.EW)

        net_cost_label.grid(row=3, column=0, padx=5, pady=5, sticky=constants.W)
        self._net_cost_label.grid(row=3, column=1, padx=5, pady=5, sticky=constants.EW)

        e_consumption_label.grid(row=4, column=0, padx=5, pady=5, sticky=constants.W)
        self._e_consumption_entry.grid(row=4, column=1, padx=5, pady=5, sticky=constants.EW)

        e_generation_label.grid(row=5, column=0, padx=5, pady=5, sticky=constants.W)
        self._e_generation_entry.grid(row=5, column=1, padx=5, pady=5, sticky=constants.EW)

        e_purchase_price_label.grid(row=6, column=0, padx=5, pady=5, sticky=constants.W)
        self._e_purchase_price_entry.grid(row=6, column=1, padx=5, pady=5, sticky=constants.EW)

        create_counter_button.grid(
            row=7,
            column=0,
            columnspan=2,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        self._savings_label = ttk.Label(master=self._frame, text="Vuotuiset säästöt: ")
        self._payback_time_label = ttk.Label(master=self._frame, text="Takaisinmaksuaika: ")

        self._savings_label.grid(row=8, column=0, padx=5, pady=5, sticky=constants.W)
        self._payback_time_label.grid(row=9, column=0, padx=5, pady=5, sticky=constants.W)

    def _delete_counter(self, counter_id):
        counter_service.delete_counter(counter_id)
        self.display_previous_calculations()

    def display_previous_calculations(self):
        """Näyttää aiemmat käyttäjän tekemät laskelmat näkymässä.

        Poistaa ensin kaikki aiemmin listatut laskelmat näkymästä (rivit 10 ja siitä eteenpäin),
        hakee käyttäjään liittyvät tallennetut laskelmat palvelusta ja näyttää ne
        käyttöliittymässä. Jokaiselle laskelmalle näytetään tiedot sekä "Poista"-painike,
        jonka avulla käyttäjä voi poistaa kyseisen laskelman.

        Jos käyttäjällä ei ole tallennettuja laskelmia, näytetään ilmoitus siitä.
        """

        #generoitu koodi alkaa
        for widget in self._frame.grid_slaves():
            if int(widget.grid_info()["row"]) >= 10:
                widget.destroy()
        #generoitu koodi loppuu

        previous_calculations = counter_service.get_previous_calculations(self._user)

        if previous_calculations:
            row = 10
            header_label = ttk.Label(self._frame, text="Aiemmat laskelmat", font=("bold"))
            header_label.grid(row=row, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)
            row += 1

            for calc in previous_calculations:
                text = (
                    f"Hankintahinta: {calc.acquisition_cost} eur\n"
                    f"Verovähennys: {calc.tax_deduction} eur\n"
                    f"Sähkönkulutus / vuosi: {calc.e_consumption} kWh\n"
                    f"Oma sähkön tuotto / vuosi: {calc.e_generation} kWh\n"
                    f"Sähkön ostohinta: {calc.e_purchase_price} eur/kWh\n"
                    f"Vuotuiset säästöt: {calc.yearly_savings:.2f} eur\n"
                    f"Takaisinmaksuaika: {calc.payback_time:.1f} vuotta\n"
                )

                info_label = ttk.Label(self._frame, text=text, justify="left", anchor="w")
                info_label.grid(row=row, column=0, sticky=constants.W, padx=5, pady=5)

                delete_button = ttk.Button(
                    self._frame,
                    text="Poista",
                    command=lambda counter_id=calc.counter_id: self._delete_counter(counter_id)
                )
                delete_button.grid(row=row, column=1, sticky=constants.E, padx=5)

                row += 1
        else:
            no_calcs_label = ttk.Label(self._frame, text="Aiempia laskelmia ei ole.")
            no_calcs_label.grid(row=10, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

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

        self.display_previous_calculations()
