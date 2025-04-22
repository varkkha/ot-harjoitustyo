"""Counter-luokka aurinkopaneelitehtaan laskurin kuvaamista varten."""

class Counter:
    """Luokka, joka kuvaa yksittäistä aurinkopaneelilaskuria

    Attributes:
        acquisition_cost:
        Numeroarvo, joka kuvaa aurinkopaneeleiden bruttohankintahintaa.
        tax_deduction:
        Numeroarvo, joka kuvaa hankintahinnasta saatavaa kotitalousvähennystä.
        e_consumption:
        Numeroarvo, joka kuvastaa vuosittaista sähkönkulutusta kilowattitunteina.
        e_generation:
        Numeroarvo, joka kuvaa vuosittaista oman aurinkopaneelitehtaan sähköntuottoa (kWh).
        e_purchase_price:
        Numeroarvo, joka kuvaa sähkön ostohintaa (€/kWh).
        user_id:
        Numeroarvo, joka yksilöi käyttäjän tietokannassa.
        counter_id:
        Numeroarvo, joka yksilöi aurinkopaneelilaskurin tietokannassa.

    Properties:
        yearly_savings:
        Laskettu vuosittainen säästö euroissa.
        payback_time:
        Laskettu takaisinmaksuaika vuosina.
    """
    def __init__(self,
                 acquisition_cost,
                 tax_deduction,
                 e_consumption,
                 e_generation,
                 e_purchase_price,
                 user_id,
                 counter_id=None):
        """Luokan konstruktori, joka luo uuden aurinkopaneelilaskurin.

        Args:
            acquisition_cost:
            Numeroarvo, joka kuvaa aurinkopaneeleiden bruttohankintahintaa.
            tax_deduction:
            Numeroarvo, joka kuvaa hankintahinnasta saatavaa kotitalousvähennystä.
            e_consumption:
            Numeroarvo, joka kuvastaa vuosittaista sähkönkulutusta kilowattitunteina.
            e_generation:
            Numeroarvo, joka kuvaa vuosittaista oman aurinkopaneelitehtaan sähköntuottoa (kWh).
            e_purchase_price:
            Numeroarvo, joka kuvaa sähkön ostohintaa (€/kWh).
            user_id:
            Numeroarvo, joka yksilöi käyttäjän tietokannassa.
            counter_id:
            Vapaaehtoinen, oletusarvoltaan None.
            Numeroarvo, joka yksilöi aurinkopaneelilaskurin tietokannassa.
        """
        self.counter_id = counter_id
        self.user_id = user_id
        self.acquisition_cost = acquisition_cost
        self.tax_deduction = tax_deduction
        self.e_consumption = e_consumption
        self.e_generation = e_generation
        self.e_purchase_price = e_purchase_price

    @property
    def yearly_savings(self):
        """Laskee aurinkopaneelitehtaan vuosittaiset säästöt (€)."""
        return self.e_generation * self.e_purchase_price

    @property
    def payback_time(self):
        """Laskee takaisinmaksuajan vuosina (nettokustannus / vuotuiset säästöt)."""
        net_cost = self.acquisition_cost - self.tax_deduction
        if self.yearly_savings == 0:
            return float('inf')
        return net_cost / self.yearly_savings
