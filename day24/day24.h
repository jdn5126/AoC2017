#include<iostream>

namespace day24 {

class Port {
    public:
        Port(int _comp1, int _comp2);
        ~Port();
        int getComp1();
        int getComp2();
        bool getUsed();
        void setComp1(int _comp1);
        void setComp2(int _comp2);
        void setUsed(bool val);
        friend std::ostream& operator<<(std::ostream& os, const Port &port);
    protected:
        int comp1;
        int comp2;
        bool used;
};

} // namespace day24
