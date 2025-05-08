# Vaatimusmäärittely

## Sovelluksen tarkoitus

Laskuri aurinkopaneelien takaisinmaksuajasta.
Käyttäjä syöttää laskuriin aurinkopaneelien hankintaan ja sähkönkulutukseen liittyviä perustietoja.
Laskuri laskee vuotuiset säästöt ja niiden pohjalta ajan, jonka kuluessa aurinkopaneelien hankintahinta on saatu kuoletettua.
Käyttäjä näkee aiemmat tekemänsä laskelmat ja voi halutessaan poistaa vanhoja laskelmia.

## Käyttäjät

Laskurilla on yksi peruskäyttäjärooli.

## Käyttöliittymäluonnos

Sovelluksessa on kolme eri näkymää. Ohjelma avautuu sisäänkirjautumissivulle, johon käyttäjä voi syöttää olemassa olevat tunnukset tai vaihtoehtoisesti siirtyä perustamaan uudet tunnukset. Uusien tunnusten perustaminen tapahtuu omassa näkymässä. Kirjauduttuaan sisään käyttäjä pääsee laskurinäkymään, johon voi syöttää laskurin tietoja sekä hallinnoida aiempia omia laskelmia. Tältä sivulta pääsee myös kirjautumaan ulos.

![](./kuvat/kayttoliittymaluonnos.png)

## Perusversion tarjoama toiminnallisuus

- Käyttäjä voi luoda itselleen käyttäjätunnuksen ja salasanan
	- Käyttäjätunnuksen tulee olla uniikki
	- Salasana tulee syöttää kaksi kertaa ja syötettyjen salasanojen tulee täsmätä
- Käyttäjä voi kirjautua järjestelmään
	- Käyttäjätunnuksen ja salasanan tulee täsmätä
	- Jos käyttäjätunnus tai salasana ei täsmää, niin järjestelmä antaa virheilmoituksen
- Käyttäjä voi kirjautua ulos järjestelmästä
- Käyttäjä voi syöttää laskuriin tiedot
	- Tyhjiä kenttiä tai negatiivisia arvoja ei voi palauttaa, tällöin järjestelmä antaa virheilmoituksen
	- Luvut tulee syöttää oikeassa muodossa niin, että desimaalierottimena käytetään pistettä. Mikäli luvut syötetään virheellisessä muodossa, antaa järjestelmä virheilmoituksen.
- Käyttäjä voi nähdä laskuriin syöttämänsä tiedot sekä laskurin laskeman tuloksen
- Käyttäjä voi tyhjentää laskurin tiedot
- Käyttäjä voi nähdä aiemmat laskelmansa ja poistaa vanhoja laskelmiaan

## Jatkokehitysideoita

- Ylläpitäjäroolin lisääminen

