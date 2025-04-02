# Vaatimusmäärittely

## Sovelluksen tarkoitus

Laskuri aurinkopaneelien takaisinmaksuajasta.
Käyttäjä syöttää laskuriin aurinkopaneelien hankintaan ja sähkönkulutukseen liittyviä perustietoja. Osa laskurin tiedoista tulee automaattisesti muualta saatujen tilastojen perusteella.
Näiden tietojen pohjalta laskuri laskee ajan, jonka kuluessa aurinkopaneelien hankintahinta on saatu kuoletettua.

## Käyttäjät

Laskurilla on yksi peruskäyttäjärooli.

## Käyttöliittymäluonnos

![](./kuvat/kayttoliittymaluonnos.png)

## Perusversion tarjoama toiminnallisuus

- Käyttäjä voi luoda itselleen käyttäjätunnuksen ja salasanan
	- Käyttäjätunnuksen tulee olla uniikki
	- Salasanojen tulee täsmätä
- Käyttäjä voi kirjautua järjestelmään
	- Käyttäjätunnuksen ja salasanan tulee täsmätä
	- Jos käyttäjätunnus tai salasana ei täsmää, niin järjestelmä antaa virheilmoituksen
- Käyttäjä voi kirjautua ulos järjestelmästä
- (Tehty) Käyttäjä voi syöttää laskuriin tiedot
	- Tyhjiä kenttiä ei voi palauttaa, tällöin järjestelmä antaa virheilmoituksen
- (Tehty) Käyttäjä voi nähdä laskuriin syöttämänsä tiedot sekä laskurin laskeman tuloksen
- Käyttäjä voi muokata laskuriin syöttämiänsä tietoja

## Jatkokehitysideoita

- Ylläpitäjäroolin lisääminen
- Ylläpitäjille mahdollisuus päivittää tilastotietoja
- Peruskäyttäjä voi syöttää useamman aurinkopaneelitehtaan tiedot
