# Porównanie wyników implementacji w C++ i Pythonie

## Struktura projektu

### Pliki projektu:
- **generator** - Skrypt generujący dane wejściowe.
- **outputC** - Implementacja sortowania w języku C++.
- **outputPy** - Implementacja sortowania w języku Python.
- **results** - Katalog zawierający podsumowanie, analizę porównawczą oraz raporty.

## Działanie projektu
1. **Generowanie danych** – Liczby losowe są zapisywane do pliku tekstowego.
2. **Uruchomienie programów** – Sortowanie danych przy użyciu implementacji w C++ oraz Pythonie.
3. **Porównanie wyników** – Analiza czasu wykonania poszczególnych operacji.

---

## Analiza wyników

### 1. Wydajność wczytywania i konwersji liczb
- **Python:** 0.192 ms
- **C++:** 0.2372 ms
- **Wniosek:** Python jest nieznacznie szybszy dzięki optymalizacjom wbudowanych funkcji do obsługi plików i operacji na liczbach.

### 2. Wydajność sortowania
- **Python:** 0.001 ms
- **C++:** 0.0004 ms
- **Wniosek:** C++ zdecydowanie przewyższa Python w tej kategorii dzięki wysoko zoptymalizowanej bibliotece STL (std::sort). Python używa Timsort, który jest efektywny, ale nieco wolniejszy ze względu na interpretowany charakter języka.

### 3. Wydajność zapisu liczb
- **Python:** 0.304 ms
- **C++:** 0.2825 ms
- **Wniosek:** C++ jest minimalnie szybszy w operacjach wejścia/wyjścia, ale różnica jest niewielka.

---

## Podsumowanie
C++ oferuje lepszą wydajność w operacjach wymagających dużej mocy obliczeniowej, takich jak sortowanie, co potwierdza jego zastosowanie w krytycznych zadaniach. Python, choć minimalnie wolniejszy, zapewnia większą czytelność i łatwość implementacji.

### **Wybór języka w zależności od zastosowania:**
- **C++** → Gdy kluczowa jest ekstremalna wydajność (np. przetwarzanie dużych zbiorów danych, systemy o wysokiej wydajności).
- **Python** → Gdy priorytetem jest prostota kodu, szybki rozwój i elastyczność (np. analiza danych, aplikacje webowe, AI).

