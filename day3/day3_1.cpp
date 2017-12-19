#include<iostream>
#include<vector>

using namespace std;

int main(int argc, char **argv) {

    // Get input
    int num;
    cin >> num;

    /* Part 1 */
    // Determine side length
    int side_length;
    for(side_length=1; side_length * side_length < num; side_length+=2);

    // "horizontal" distance
    int distance = side_length / 2;

    // Determine corners and centers
    int corner4 = side_length * side_length;
    int center4 = corner4 - side_length / 2;
    int corner3 = corner4 - side_length + 1;
    int center3 = corner3 - side_length / 2;
    int corner2 = corner3 - side_length + 1;
    int center2 = corner2 - side_length / 2;
    int corner1 = corner2 - side_length + 1;
    int center1 = corner1 - side_length / 2;

    // Find "vertical" distance
    if (num > center4) {
        distance += num - center4;
    } else if (num > corner3) {
        distance += center4 - num;
    } else if (num > center3) {
        distance += num - center3;
    } else if (num > corner2) {
        distance += center3 - num;
    } else if (num > center2) {
        distance += num - center2;
    } else if (num > corner1) {
        distance += center2 - num;
    } else if (num > center1) {
        distance += num - center1;
    } else {
        distance += center1 - num;
    }
    cout << distance << endl;

    return 0;
}
