# Ohjelmistotekniikka, harjoitustyö

Harjoitustyö kurssille *TKT20018 Aineopintojen harjoitustyö: Ohjelmistotekniikka*

Työn tavoitteena on luoda **laskuri aurinkopaneelin takaisinmaksuajasta**

## Dokumentaatio

- [Vaatimusmäärittely](./sovellus/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./sovellus/dokumentaatio/tuntikirjanpito.md)
- [Changelog](./sovellus/dokumentaatio/changelog.md)

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.