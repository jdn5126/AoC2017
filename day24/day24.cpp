#include "day24.h"

namespace day24 {

// Constructor
Port::Port(int _comp1, int _comp2) {
    comp1 = _comp1;
    comp2 = _comp2;
    used = false;
}

Port::~Port() {
}

int 
Port::getComp1() {
    return comp1;
}

int 
Port::getComp2() {
    return comp2;
}

bool
Port::getUsed() {
    return used;
}

void 
Port::setComp1(int _comp1) {
    comp1 = _comp1;
}

void
Port::setComp2(int _comp2) {
    comp2 = _comp2;
}

void
Port::setUsed(bool val) {
    used = val;
}

std::ostream &
operator<<(std::ostream &os, const Port &port) {
    os << port.comp1 << "/" << port.comp2;
    return os;
}

} // namespace day24
