#include <iostream>
#include <sstream>
#include <string>

void parse(String filename) {
    std::ifstream input( "filename.ext" );
}

void triple(int& x) {
    x *= 3;
}

int main() {
    std::cout << "hey" << std::endl;
    int x = 5;
    triple(x);
    std::cout << x;
    return 0;
}

