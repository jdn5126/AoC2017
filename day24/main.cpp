#include<fstream>
#include<map>
#include<sstream>
#include<string>
#include<vector>
#include "day24.h"


int main(int argc, char **argv) {
   
    std::string line;
    std::ifstream infile(argv[1], std::ios::in); 
    std::map<int, std::vector<day24::Port *>> port_map;

    // Parse file
    int comp1, comp2;
    while(std::getline(infile, line)) {
        // Grab components
        std::stringstream ss(line);
        ss >> comp1;
        // Ignore delimeter
        ss.ignore();
        ss >> comp2;
        // Create pointer to Port object
        day24::Port *new_port = new day24::Port(comp1, comp2);
        // Forward and reverse map
        if (port_map.count(comp1) == 0) {
            std::vector<day24::Port *> new_vec(1, new_port);
            port_map.insert(std::pair<int, std::vector<day24::Port *>>(comp1, new_vec)); 
        } else {
            port_map[comp1].push_back(new_port);
        }
        if (port_map.count(comp2) == 0) {
            std::vector<day24::Port *> new_vec(1, new_port);
            port_map.insert(std::pair<int, std::vector<day24::Port *>>(comp2, new_vec)); 
        } else {
            port_map[comp2].push_back(new_port);
        }
    }

    // Print port_map
    for(auto it=port_map.begin(); it != port_map.end(); it++) {
        std::cout << it->first << " => ";
        for(int i=0; i < it->second.size(); i++) {
            std::cout << *it->second[i] << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
