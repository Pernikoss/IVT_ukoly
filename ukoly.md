# Sada úkolů: Základy Flasku


## Doporučený průběh práce
1. Každý úkol potvrď samostatným commitem s rozumným popisem.
2. Po dokončení vždy otestuj lokálně.
3. Po důležitých změnách ověř i nasazenou verzi na Render.

## Co odevzdat
1. Odkaz na veřejný GitHub repozitář.
2. Odkaz na běžící aplikaci na Render.
3. Krátký popis (3-6 vět), co se ti povedlo a kde byl největší problém.


Doporučuji použít <https://www.geeksforgeeks.org/python/flask-tutorial/>

**Úkoly na sebe navazují. Pracuj průběžně v jednom repozitáři.**

## Úkol 1: Spuštění aplikace lokálně
**Cíl:** Ověřit, že umíš rozběhnout Flask aplikaci na svém počítači.

**Zadání:**
1. Nainstaluj závislosti podle projektu (lze přeskočit na školních PC).
2. Spusť aplikaci příkazem `python app.py`.
3. Otevři web v prohlížeči na adrese `http://127.0.0.1:5000`.

**Hotovo, když:**
1. Stránka se zobrazí bez chyby.
2. Funguje formulář se jménem a pozdravem.

## Úkol 2: Git a veřejný repozitář
**Cíl:** Ověřit, že umíš verzovat projekt a publikovat ho.

**Zadání:**
1. Inicializuj Git v projektu.
2. Vytvoř první commit se stávajícím stavem aplikace.
3. Vytvoř veřejný repozitář na GitHubu.
4. Propoj lokální projekt se vzdáleným repozitářem a odešli změny (`push`).

**Hotovo, když:**
1. Repo je veřejně dostupné.
2. Je v něm vidět alespoň jeden commit.

## Úkol 3: Nasazení na Render.com
**Cíl:** Publikovat Flask aplikaci online.

**Zadání:**
1. Vytvoř na Render novou webovou službu propojenou s GitHub repozitářem.
2. Nastav správně `Root directory`, `Build command` a `Start command` podle README.
3. Po nasazení otevři veřejnou URL aplikace a ověř funkčnost.

**Hotovo, když:**
1. Aplikace běží na veřejné URL.
2. Formulář funguje stejně jako lokálně.

## Úkol 4: Rozšíření formuláře o příjmení (GET)
**Cíl:** Procvičit práci s více parametry v `request.args`.

**Zadání:**
1. Do šablony přidej druhé pole formuláře pro příjmení (`surname`).
2. V `app.py` načti `name` i `surname` přes `request.args.get(...)`.
3. Uprav výstup tak, aby se zobrazil pozdrav ve tvaru: `Jméno Příjmení, rád tě vidím!`.
4. Zkontroluj, že se jméno i příjmení zobrazují v URL. To je základní vlastnost metody GET.

**Hotovo, když:**
1. Funguje zadání jména i příjmení.
2. Pozdrav se správně zobrazí při odeslání formuláře.

## Úkol 5: Přechod z GET na POST
**Cíl:** Naučit se odesílat formulář metodou POST.

**Zadání:**
1. Vytvoř novou route, například `/pozdrav-post`.
2. Přidej novou šablonu, například `templates/pozdrav_post.html`.
3. Do nové šablony překopíruj formulář, ale uprav `method="POST"`.
4. U nové route povol metody `GET` i `POST`.
5. Data formuláře čti přes `request.form`.
6. Ověř, že se data po odeslání neobjevují v URL.

**Hotovo, když:**
1. Nová stránka s novou šablonou je funkční.
2. POST formulář na nové stránce odesílá data správně.
3. Data nejsou vidět v adrese stránky.

## Úkol 6: Zadání hesla a tajná informace
**Cíl:** Použít podmínku na serveru a POST data.

**Zadání:**
1. Přidej do formuláře pole pro heslo (`type="password"`).
2. Na serveru porovnej zadané heslo s hodnotou uloženou v proměnné (např. `SPRAVNE_HESLO`).
3. Pokud je heslo správné, zobraz tajnou informaci (např. text nebo zajímavost).
4. Pokud je heslo špatné, zobraz chybovou hlášku.

**Hotovo, když:**
1. Tajná informace se zobrazí pouze po zadání správného hesla.
2. Při špatném hesle se zobrazí jasná chyba.

## Úkol 7: Validace vstupů
**Cíl:** Naučit se základní kontrolu dat od uživatele.

**Zadání:**
1. Ošetři prázdné jméno (nesmí projít).
2. Omez délku jména na 50 znaků.
3. Při nevalidním vstupu vrať uživateli srozumitelnou chybovou zprávu.

**Hotovo, když:**
1. Aplikace neakceptuje neplatné vstupy.
2. Uživatel vždy vidí, co má opravit.

## Úkol 8: Oddělená chráněná stránka
**Cíl:** Procvičit routy a předávání stavu mezi požadavky.

**Zadání:**
1. Vytvoř novou route `/tajne`.
2. Po správném zadání hesla umožni přístup na `/tajne`.
3. Pokud heslo ověřené není, přesměruj uživatele zpět na hlavní stránku.

**Doporučení:**
Použij `session` (<https://www.geeksforgeeks.org/python/how-to-use-flask-session-in-python-flask/>)

**Hotovo, když:**
1. Nepřihlášený uživatel se na `/tajne` nedostane.
2. Přihlášený uživatel chráněnou stránku zobrazí.

## Úkol 9: Záznam pokusů do souboru
**Cíl:** Ukládat jednoduchá data ze serveru. *Zde můžete použít AI :-)*

**Zadání:**
1. Při každém pokusu o přihlášení zapiš do souboru `logins.csv`:
	- datum a čas,
	- zadané jméno,
	- výsledek (`OK` / `FAIL`).
2. Záznamy ukládej průběžně (po řádcích).

**Hotovo, když:**
1. Soubor se vytváří automaticky.
2. Každý pokus se korektně zapíše.

## Úkol 10: Vlastní chybová stránka 404
**Cíl:** Seznámit se s error handlery ve Flasku (<https://www.geeksforgeeks.org/python/python-404-error-handling-in-flask/>).

**Zadání:**
1. Přidej handler pro chybu 404 v `app.py`.
2. Vytvoř šablonu `templates/404.html`.
3. Na stránce zobraz stručnou zprávu a odkaz zpět na hlavní stránku.

**Hotovo, když:**
1. Při návštěvě neexistující URL se zobrazí tvoje vlastní 404 stránka.
2. Uživatel se může jedním kliknutím vrátit na úvod.

