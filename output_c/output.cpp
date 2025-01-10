
#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>
#include <windows.h>

using namespace std;

double timer(void (*sortFunc)(vector<double>&), vector<double>& arr) {
    LARGE_INTEGER start, end, frequency;
    QueryPerformanceFrequency(&frequency);
    QueryPerformanceCounter(&start);
    sortFunc(arr);
    QueryPerformanceCounter(&end);
    long long elapsed = end.QuadPart - start.QuadPart;
    double elapsedInMicroseconds = (elapsed * 1000000.0) / frequency.QuadPart;
    double elapsedInMilliseconds = elapsedInMicroseconds / 1000.0;
    return elapsedInMilliseconds;
}


void loadFromFile(string filename, vector<double>& arr) {
    ifstream inFile(filename); 
    if (!inFile.is_open()) {   
        cerr << "Nie można otworzyć pliku do odczytu!" << endl;
        return;
    }

    double num;
    while (inFile >> num) {  
        arr.push_back(num);  
    }

    

    inFile.close(); 
}

void sorting(vector<double>& arr) {
    sort(arr.begin(), arr.end());
}

void saveToFile(double loading, double sorting, string filename) {
    LARGE_INTEGER start, end, frequency;
    QueryPerformanceFrequency(&frequency);
    QueryPerformanceCounter(&start);
    ofstream outFile(filename);
    if (!outFile.is_open()) {
        cerr << "Nie można otworzyć pliku do zapisu!" << endl;
        return;
    }

    outFile << "Czas otwierania: " << loading << " ms" << endl;
    outFile << "Czas sortowania: " << sorting << " ms" << endl;

    QueryPerformanceCounter(&end);
    long long elapsedLoad = end.QuadPart - start.QuadPart;
    double elapsedInMicroseconds = (elapsedLoad * 1000000.0) / frequency.QuadPart;
    double elapsedInMilliseconds = elapsedInMicroseconds / 1000.0;
    cout << "Czas zapisywania: " << elapsedInMilliseconds << " ms" << endl;
    outFile << "Czas zapisywania: " << elapsedInMilliseconds << " ms" << endl;

}
int main() {
    vector<double> arr;
    string filename = "C:/Users/Olek/Desktop/zsł/4testowanie/sort_c_py/generator/generator/base.txt";




    LARGE_INTEGER start, end, frequency;
    QueryPerformanceFrequency(&frequency);
    QueryPerformanceCounter(&start);

    loadFromFile(filename, arr);

    QueryPerformanceCounter(&end);
    long long elapsedLoad = end.QuadPart - start.QuadPart;
    double elapsedInMicroseconds = (elapsedLoad * 1000000.0) / frequency.QuadPart;
    double elapsedInMilliseconds = elapsedInMicroseconds / 1000.0;
    cout << "Czas wczytywania: " << elapsedInMilliseconds << " ms" << endl;



    sorting(arr);
    double elapsedSort = timer(sorting, arr);
    cout << "Czas sortowania: " << elapsedSort << " ms" << endl;

    saveToFile(elapsedInMilliseconds, elapsedSort, filename);

    return 0;
}
