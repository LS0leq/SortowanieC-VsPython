
#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

void generateRandom(int n, double* arr) {
    srand(time(0));
    ofstream outFile("base.txt");
    if (!outFile.is_open()) {
        cerr << "Nie można otworzyć pliku do zapisu!" << endl;
        return;
    }
    else {
        cout << "Otwarto plik!" << endl << endl << endl;
    }
    for (int x = 0; x < n; x++) {

        arr[x] = (rand() / (double)RAND_MAX) * 100;
        outFile << fixed << setprecision(2) << arr[x] << endl;

    }
    cout << "Zapisano dane i zamykanie pliku!"<<endl;
    outFile.close();

}
int main()
{
    int n = 10000;
    double* arr = new double[n];
    generateRandom(n, arr);
    delete[] arr;

}


