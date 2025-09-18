    stack<std::string> stack  ##создание пустого стека;
stack.push("Tom");
stack.push("Bob");
stack.push("Sam")  ##добавление трёх элементов;
std::cout << "Top: " << stack.top() << std::endl;  ## вывод верхнего элемента. 