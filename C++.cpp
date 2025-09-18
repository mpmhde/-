    #include <iostream>
#include <list>
int main() {
    std::list<int> numbers = {1, 2, 3, 4, 5};
    numbers.push_back(6); // Добавляет элемент в конец
    numbers.push_front(0); // Добавляет элемент в начало
    for(int number : numbers) {
        std::cout << number << " ";
    }
    return 0;
}
 