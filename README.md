# kRONO-BOTXY

***

## INSTALLAZIONE DA HEROKU

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

**Non tutte le Var sono obbligatorie basta impostare le due Var sotto:**

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

**UniBorg Config**
La Config UniBorg Config è situata in `userbot/uniborgConfig.py`.

**Heroku Config**
Basta lasciare da predefinita.

**Local Config**
Cerca la Linea 111 e inizia a modificare da li.
Per UniBorg Config non ci sono Var obligatorie.

## Var Obbligatorie

- Solo queste due variabili sono obbligatorie:
  - `APP_ID`: Valore da ottenere da <https://my.telegram.org>
  - `API_HASH`: Valore da ottenere da <https://my.telegram.org>
- Se non ci sono causerà: `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
  