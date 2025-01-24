
Projekt ma na celu porównanie wyników generowanych przez implementacje programu w dwóch różnych językach: "C++" oraz "Python". Główne komponenty projektu obejmują generowanie danych wejściowych, uruchamianie programu w obu językach oraz analizowanie wyników.

plik generator:
  Zawiera skrypty lub narzędzia odpowiedzialne za generowanie danych wejściowych potrzebnych do uruchomienia programów.

plik outputC:
  Przechowuje wyniki działania programu napisanego w języku C.

plik outputPy
  Zawiera wyniki działania programu napisanego w Pythonie.

plik results: 
  W tym katalogu znajdują się ostateczne wyniki, takie jak podsumowanie, analiza porównawcza, raporty itp.

Jak działa projekt?
   Najpierw należy wygenerować liczby oraz zapisać je do pliku tekstowego. Należy uruchomić program w obu językach i porównać za co odpowiada plik results.


Działanie programu oraz wnioski wynikające z testów:
1. Wydajność wczytywania i konwersji liczb
Python był minimalnie szybszy w wczytywaniu i konwersji liczb (0.192 ms w Pythonie vs 0.2372 ms w C++). Wynika to prawdopodobnie z optymalizacji wbudowanych funkcji Pythona do obsługi plików i operacji na liczbach, które są wysoko zintegrowane z interpretatorem języka.

2. Wydajność sortowania
C++ znacznie przewyższa Python w czasie sortowania danych (0.0004 ms w C++ vs 0.001 ms w Pythonie). Jest to zgodne z oczekiwaniami, ponieważ biblioteka STL w C++ (np. std::sort) jest jedną z najbardziej zoptymalizowanych implementacji algorytmów sortowania. Python używa Timsort, który jest również wydajny, ale interfejs interpretowany może generować nieznaczny narzut.

3. Wydajność zapisu liczb
C++ był odrobinę szybszy w zapisywaniu danych do pliku (0.2825 ms w C++ vs 0.304 ms w Pythonie). Różnica jest jednak niewielka i może być uzależniona od szczegółów implementacji operacji wejścia/wyjścia w obu językach.

Podsumowując - C++ okazał się szybszy w operacjach wymagających dużej liczby obliczeń i optymalizacji, takich jak sortowanie, co potwierdza jego wydajność w zastosowaniach wymagających dużej mocy obliczeniowej. Python, choć minimalnie wolniejszy w większości operacji, oferuje wystarczającą wydajność do codziennych zadań oraz przewagę w prostocie i czytelności kodu.

Jeżeli kluczowe są ekstremalnie niskie czasy wykonania, jak w przypadku sortowania, C++ będzie lepszym wyborem. Natomiast w przypadku zadań, gdzie łatwość implementacji i rozwój mają większe znaczenie, Python może być bardziej odpowiedni.
