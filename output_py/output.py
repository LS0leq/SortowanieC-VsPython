import time
import os


def timer(sort_func, arr):
    start_time = time.perf_counter()
    sort_func(arr)
    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) * 1000
    return elapsed_time


def load_from_file(filename, arr):
    if not os.path.exists(filename):
        print(f"Nie można otworzyć pliku do odczytu: {filename}")
        return
    with open(filename, 'r') as file:
        for line in file:
            try:
                arr.append(float(line.strip()))
            except ValueError:
                pass


def sorting(arr):
    arr.sort()


def save_to_file(loading, sorting, filename):
    output_filename = "output.txt"
    start_time = time.perf_counter()

    try:
        with open(output_filename, 'w') as out_file:
            out_file.write(f"Czas otwierania: {loading:.3f} ms\n")
            out_file.write(f"Czas sortowania: {sorting:.3f} ms\n")
    except IOError:
        print("Nie można otworzyć pliku do zapisu!")
        return

    end_time = time.perf_counter()
    elapsed_write = (end_time - start_time) * 1000
    print(f"Czas zapisywania: {elapsed_write:.3f} ms")

    with open(output_filename, 'a') as out_file:
        out_file.write(f"Czas zapisywania: {elapsed_write:.3f} ms\n")


def main():
    arr = []
    filename = "C:/Users/Olek/Desktop/zsł/4testowanie/sort_c_py/generator/generator/base.txt"

    start_time = time.perf_counter()
    load_from_file(filename, arr)
    end_time = time.perf_counter()
    elapsed_load = (end_time - start_time) * 1000
    print(f"Czas wczytywania: {elapsed_load:.3f} ms")

    elapsed_sort = timer(sorting, arr)
    print(f"Czas sortowania: {elapsed_sort:.3f} ms")

    save_to_file(elapsed_load, elapsed_sort, filename)


if __name__ == "__main__":
    main()
