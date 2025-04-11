# Ohjelmistotekniikka, harjoitustyö

Harjoitustyö kurssille *TKT20018 Aineopintojen harjoitustyö: Ohjelmistotekniikka*

Työn tavoitteena on luoda **laskuri aurinkopaneelin takaisinmaksuajasta**

## Dokumentaatio

- [Vaatimusmäärittely](./sovellus/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./sovellus/dokumentaatio/tuntikirjanpito.md)
- [Changelog](./sovellus/dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](./sovellus/dokumentaatio/arkkitehtuuri.md)

## Releaset

[Viikko 5](https://github.com/varkkha/ot-harjoitustyo/releases/tag/viikko5)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

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

### Pylint

Tiedoston [.pylintrc](./sovellus/.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
