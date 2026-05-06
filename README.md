# Starter aplikace – backend pomocí frameworku Flask (Python)

Jednoduchá aplikace pro výuku webových technologií, zejména backendu.

Zadání úkolů: [ukoly.md](ukoly.md)

## Spuštění lokálně
- Instalace Flasku: *`pip install Flask` (na školních PC by mělo být nainstalováno)*
- Spuštění v debug módu `python app.py` (případně `flask run --debug`)

Aplikace běží na <http://127.0.0.1:5000>.

## Spuštění na Render
- Root directory `backend/app-flask-starter` *(pokud tam posílám celý tento repozitář, musím nastavit v jaké složce se nachází aplikace)*
- Build command `pip install -r requirements.txt`
- Start command `gunicorn app:app`
*Pozn.: soubor requirements.txt slouží pro spuštění na službě Render*