#include <iostream>
using namespace std;
const int MAX_SIZE = 5;

class Stack
{
private:
    int arr[MAX_SIZE];
    int altura; // posicion de la siguiente entrada

public:
    Stack()
    {
        altura = 0; // means EMPTY
    }
    bool isEmpty()
    {
        return (altura == 0);
    }
    bool isFull()
    {
        return (altura == MAX_SIZE);
    }
    void push(int element)
    {
        if (!isFull())
        {
            arr[altura] = element;
            altura++;
        }
    }
    void pop()
    {
        if (!isEmpty())
        {
            int popped = arr[altura - 1];
            altura--;
        }
    }
    void vaciar()
    {
        altura = 0;
    }
    int altura()
    {
        return altura ;
    }

    friend ostream &operator<<(ostream &os, const Stack &s);
};

ostream &operator<<(ostream &os, const Stack &s)
{
    os << s.altura << ": [";
    for (int i = 0; i < s.altura; i++)
        os << s.arr[i] << ",";
    os << "]";
    return os;
}

int main()
{
    Stack s;
    cout << s << endl;

    s.push(11);
    cout << s << endl;

    s.push(22);
    cout << s << endl;

    cout << s.altura() << endl;

    s.push(33);
    cout << s << endl;

    s.pop();
    cout << s << endl;

    s.push(44);
    cout << s << endl;

    s.push(55);
    cout << s << endl;

    s.push(66);
    cout << s << endl;

    s.push(77);
    cout << s << endl;

    s.vaciar();
    cout << s << endl;
}
