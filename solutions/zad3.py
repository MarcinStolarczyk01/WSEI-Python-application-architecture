"""
Za pomocą API zwracającego informacje dot. uniwersytetów w danym państwie:
http://universities.hipolabs.com/search?country=<nazwa_kraju_eng> wyświetl
nazwy uniwersytetów z 20 wybranych krajów w postaci: {<nazwa_kraju>:
[<nazwa_uniwersytet1>, <nazwa_uniwersytet2>,...], …}. W celu przyspieszenia
pobierania danych, wykorzystaj moduł threading do realizacji wielowątkowego
pobierania informacji.
"""