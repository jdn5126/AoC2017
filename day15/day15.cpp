#include<iostream>

#define FACTOR_A 16807
#define MULTIPLE_A 4
#define FACTOR_B 48271
#define MULTIPLE_B 8
#define DIVISOR 2147483647


long long 
num_matches(int seed_a, int seed_b, int num_iters) {
    long long val_a = (long long)seed_a;
    long long val_b = (long long)seed_b;
    int a_16, b_16;
    int num_matches = 0;
    for( int i=0; i < num_iters; i++ ) {
        val_a = (val_a * FACTOR_A) % DIVISOR;
        // Calculate next valid value for a
        while (val_a % 4 != 0) {
            val_a = (val_a * FACTOR_A) % DIVISOR;
        }
        val_b = (val_b * FACTOR_B) % DIVISOR;
        // Calculate next valid value for b
        while (val_b % 8 != 0) {
            val_b = (val_b * FACTOR_B) % DIVISOR;
        }
        // If lower 16 bits match, increment matches
        a_16 = val_a & 0xffff;
        b_16 = val_b & 0xffff;
        if ( a_16 == b_16 ) {
            num_matches++;
        }
    }
    return num_matches;
}


int main(int argc, char **argv) {
    // Get values for Generator A and Generator B... and iterations
    int gen_a, gen_b, iterations;
    std::cout << "Generator A: ";
    std::cin >> gen_a;
    std:: cout << "Generator B: ";
    std::cin >> gen_b;
    std::cout << "Number of Iterations: ";
    std::cin >> iterations;

    // Calculate number of matches for given iterations
    std::cout << num_matches(gen_a, gen_b, iterations) << std::endl;

    return 0;
}
