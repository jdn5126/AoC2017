#include<fstream>
#include<iostream>

using namespace std;

int main(int argc, char **argv) {
    // Open at end of file
    ifstream infile(argv[1], ios::in|ios::ate);
    // Get length of file 
    size_t length = infile.tellg();
    // Seek to beginning of file
    infile.seekg(0, ios::beg);

    // Read one byte at a time
    char mychar;
    int sum = 0, first, prev, cur;
    // Grab first digit (no modular arithmetic here)
    infile.read(&mychar, sizeof(char));
    first = mychar - 48;
    prev = first;

    // Part 1
    for(int i=1; i < length - 1; i++) {
        infile.read(&mychar, sizeof(char));
        cur = mychar - 48;
        if (cur == prev) {
            sum += cur;
        }
        prev = cur;
    }
    if (prev == first) {
        sum += first;
    }
    cout << "Part1: " << sum << endl;

    // Part 2
    int partner;
    sum = 0;
    int stride = (length - 1) / 2;
    for(int i=0; i < stride; i++) {
        // from beginning, seek to i
        infile.seekg(i, ios::beg);
        infile.read(&mychar, sizeof(char));
        cur = mychar - 48;
        // seek to partner
        infile.seekg(stride - 1, ios::cur);
        infile.read(&mychar, sizeof(char));
        partner = mychar - 48;
        if (cur == partner) {
            sum += 2*cur;
        }
    }
    cout << "Part2: " << sum << endl;

    infile.close();

    return 0;
}
