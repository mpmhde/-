 stack = Stack()
 print("Создан новый стек")

 # Добавление элементов
 stack.push(10)
 stack.push(20)
 stack.push(30)
 print(stack)

 # Просмотр и удаление
 print("Верхний элемент:", stack.peek())
 stack.pop()
 print("После удаления:", stack)
 print("Размер стека:", stack.size())
 print("Стек пуст?", stack.is_empty())
 