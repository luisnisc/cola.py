#include <iostream>
using namespace std;
const int MAX_SIZE = 5;

class Stack
{
private:
    int arr[MAX_SIZE];
    int top;

public:
    Stack()
    {
        top = -1; // means EMPTY
    }
    bool isEmpty()
    {
        return (top == -1);
    }
    bool isFull()
    {
        return (top == MAX_SIZE - 1);
    }
    void push(int element)
    {
        top++;
        arr[top] = element;
        // if (!isFull())
        // {
        //     top++;
        //     arr[top] = element;
        // }
    }
    friend ostream &operator<<(ostream &os, const Stack &s);
};

ostream &operator<<(ostream &os, const Stack &s)
{
    os << s.top << "[...todo..."
       << "]";
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

    s.push(33);
    cout << s << endl;

    s.push(44);
    cout << s << endl;

    s.push(55);
    cout << s << endl;

    s.push(66);
    cout << s << endl;
}
