import os
import matplotlib.pyplot as plt
def load_from_file(filename, arr):
    if not os.path.exists(filename):
        print(f"Nie można otworzyć pliku do odczytu: {filename}")
        return
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if "Czas" in line:
                try:

                    parts = line.split(":")
                    if len(parts) > 1:
                        arr.append(float(parts[1].split()[0]))
                except ValueError:
                    print(f"Pominięto niepoprawną wartość: {line}")


def plot_bar_chart(c_times, p_times):
    categories = ['Wczytywanie', 'Sortowanie', 'Zapis']

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.bar([i - 0.2 for i in range(len(categories))], c_times, width=0.4, label='C++', align='center')

    ax.bar([i + 0.2 for i in range(len(categories))], p_times, width=0.4, label='Python', align='center')

    ax.set_xlabel('Kategoria')
    ax.set_ylabel('Czas (ms)')
    ax.set_title('Porównanie czasów dla C++ i Python')
    ax.set_xticks(range(len(categories)))
    ax.set_xticklabels(categories)
    plt.gcf().canvas.manager.set_window_title('Wykres Porównania Czasów: C++ vs Python')
    ax.legend()

    plt.show()


def main():
    arrC = []
    arrP = []

    filenameC = r"C:\Users\Olek\Desktop\zsł\4testowanie\sort_c_py\output_c\output\output.txt"
    filenameP = r"C:\Users\Olek\Desktop\zsł\4testowanie\sort_c_py\output_py\output.txt"

    load_from_file(filenameC, arrC)
    load_from_file(filenameP, arrP)

    print("C++ !!! \nCzas wczytania i konwersji liczb: ", arrC[0], "ms", "\nCzas sortowania: ", arrC[1], "ms", "\nCzas zapisu liczb: ", arrC[2], "ms\n\n")
    print("Python !!! \nCzas wczytania i konwersji liczb: ", arrP[0], "ms", "\nCzas sortowania: ", arrP[1], "ms", "\nCzas zapisu liczb: ", arrP[2], "ms")

    c_times = arrC[:3]
    p_times = arrP[:3]

    plot_bar_chart(c_times, p_times)

if __name__ == "__main__":
    main()
