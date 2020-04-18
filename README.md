# kRONO-BOTXY

## Gruppo Telegram

Entra nel Gruppo ***[DA QUI](https://t.me/IOIIIOIIIOI)*** per supporto e info.

***

## INSTALLAZIONE VELOCE DA HEROKU

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## INSTALLAZIONE DA TERMINALE

Clona il repository e avvia il file principale:

```sh
git clone https://github.com/KronosXY/krono-botXY
cd krono-botXY
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Crea local_config.py con le tue variabili>
python3 -m userbot
```

Esempio di `local_config.py` file:

***Non tutte le variabili sono obbligatorie**

***L'userbot si avvia basta impostare le due Var:**

```python3
da heroku_config importa le Var

Development(Var):
  APP_ID =
  API_HASH =
```

**UniBorg Config**
La Config UniBorg Config è situata in `userbot/uniborgConfig.py`.

**Heroku Config**
Basta lasciare da predefinita.

**Local Config**
Cerca la Linea 111 e inizia a modificare da li.
Per UniBorg Config non ci sono Var obligatorie.

## Var Obbligatorie

- Solo queste due variabili sono obbligatorie se non inserite
- Questo causa `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
  - `APP_ID`: Valore da ottenere da <https://my.telegram.org>
    - `API_HASH`: Valore da ottenere da <https://my.telegram.org>
  