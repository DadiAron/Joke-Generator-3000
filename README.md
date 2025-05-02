Til þess að keyra þetta locally þarf að:
PRE: Nota VSCode.
1. Fara inná https://www.python.org/downloads/ og ná í nýjustu útgáfu af python.
2. Skrifa í "searchbarið" eftst í VSCode >Python: Create Environment og velja umhverfi, Venv.
3. Skrifa >Python: Select interpreter, velja recommended.
4. Keyra pip install -r requirements.txt í skipanalínu.
5. Keyra uvicorn app.main:app --reload í skipanalínu.
6. Opna síðuna locally með því að ýta á http://127.0.0.1:8000 sem kemur upp í terminalinu.