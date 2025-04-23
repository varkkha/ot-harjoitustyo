# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne on esitetty alla olevassa kaaviossa. Rakenne noudattaa kolmitasoista kerrosarkkitehtuuria. _UI_-pakkaus vastaa sovelluksen käyttöliittymästä, _Services_-pakkaus sovelluslogiikasta ja Repositories_-pakkaus vastaa sovelluksen tietokantaoperaatioista. _Entities-pakkaus sisältää luokat, jotka kuvaavat sovelluksen käyttämiä tietomalleja.

```mermaid
graph TD
    UI --> Services
    Services --> Repositories
    Services --> Entities
    Repositories --> Entities
```
## Käyttöliittymä


## Sovelluslogiikka

Sovelluksessa käytettäviä tietomalleja ovat luokat ![User](../src/entities/user.py) ja ![Counter](../src/entities/counter.py). Counter-luokka kuvaa aurinkopaneelilaskuria ja User-luokka kuvaa käyttäjätunnuksen luonutta käyttäjää.

```mermaid
classDiagram
    class Counter {
        +acquisition_cost
        +tax_deduction
        +e_consumption
        +e_generation
        +e_purchase_price
        +user_id
        +counter_id
        +yearly_savings()
        +payback_time()
    }

    class User {
        +username
        +password
        +user_id
    }

    Counter "*" --> "1" User
```
Alla sovellusta kuvaava luokkakaavio.

```mermaid
classDiagram
    UI "1" -- "1" Services
    Services "1" -- "1" Repositories
    Services "1" -- "1" Entities
    Repositories "1" -- "1" Entities

    class UI{
        CreateUserView
        LoginView
        CounterView
    }

    class Services{
        CounterService
    }

    class Repositories{
        UserRepository
        CounterRepository
    }

    class Entities{
        User
        Counter
    }

```

## Päätoiminnallisuudet

### Uuden käyttäjän luominen

Kun halutaan luoda uusi käyttäjätunnus, painetaan kirjautumissivulla olevaa painiketta "Luo uusi käyttäjä".
Käyttäjälle aukeaa uusi sivu, johon käyttäjä syöttää uuden käyttäjätunnuksen. Käyttäjätunnuksen tulee olla uniikki.
Sovellus antaa virheilmoituksen mikäli käyttäjätunnus on jo käytössä. Käyttäjätunnuksen jälkeen käyttäjä syöttää valitsemansa salasanan.
Tämän jälkeen käyttäjä syöttää salasanan uudestaan ja sen tulee täsmätä aiemmin annettuun salasanaan. Mikäli salasanat eivät täsmää,
sovellus antaa virheilmoituksen. Syötettyään tiedot käyttäjä painaa "Luo käyttäjä"-painiketta ja sovellus kirjaa käyttäjän sisälle järjestelmään.

Alla sekvenssikaavio uuden käyttäjän luomisesta:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant CounterService
  participant UserRepository

  User->>UI: click "Luo uusi käyttäjä"
  UI->>UI: tarkista täsmäävätkö salasanat
  alt virheellinen syöte
    UI->>User: näytä virheilmoitus
  else validi syöte
    UI->>CounterService: create_user("käyttäjätunnus", "salasana")
    CounterService->>UserRepository: find_by_username("käyttäjätunnus")
    alt käyttäjänimi on jo käytössä
      CounterService-->>UI: UsernameExistsError
      UI->>User: näytä virheilmoitus
    else uusi käyttäjä
      CounterService->>UserRepository: create(User)
      UserRepository-->>CounterService: user
      CounterService-->>UI: user
      UI->>UI: show_counter_view()
    end
  end
```


