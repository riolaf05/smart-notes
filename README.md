# Appunti AI

Appunti AI è un supporto allo studio che consente di riassumere automaticamente le immagini delle pagine di libri. Le immagini vengono scattate, elaborate per estrarre il testo e generare un riassunto, che viene poi salvato su una pagina Notion specificata dall'utente.

## Funzionalità

- Acquisizione immagini di pagine di libri
- Estrazione automatica del testo dalle immagini
- Generazione di riassunti dei contenuti
- Salvataggio dei riassunti su una pagina Notion

## Setup del progetto

### 1. Configurazione del workflow n8n

1. Accedi all'istanza n8n all'indirizzo:  
    `http://<server_casa>:5678/projects/F0u3PIPriMdsGvXi/workflows`
2. Configura il workflow seguendo le istruzioni presenti nell'interfaccia.
3. Inserisci le credenziali Notion e gli altri parametri richiesti.

### 2. Setup con Docker

Assicurati di avere Docker installato sul tuo sistema.

1. Clona questo repository:
    ```bash
    git clone https://github.com/<tuo-utente>/appunti-ai.git
    cd appunti-ai
    ```
2. Crea un file `.env` con le variabili necessarie (vedi esempio `.env.example`).
3. Avvia i servizi con Docker Compose:
    ```bash
    docker-compose up -d
    ```
4. Verifica che i container siano in esecuzione:
    ```bash
    docker ps
    ```

## Note

- Assicurati che la pagina Notion sia accessibile tramite le API e che il token sia valido.
- Personalizza il workflow n8n secondo le tue esigenze.

## Licenza

Questo progetto è distribuito con licenza MIT.
