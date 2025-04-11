# Arkkitehtuurikuvaus

## Rakenne
```mermaid
 graph TD
    subgraph "UI"
        U1[CreateUserView]
        U2[LoginView]
        U3[CounterView]
    end

    subgraph "Services"
        S1[CounterService]
    end

    subgraph "Repositories"
        R1[UserRepository]
        R2[CounterRepository]
    end

    subgraph "Entities"
        E1[User]
        E2[Counter]
    end

    UI --> Services
    S1 --> R1
    R1 --> E1
    S1 --> E2
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
 

