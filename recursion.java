class Node {
    int data;
    Node left, right;
    
    // Конструктор узла
    public Node(int item) {
        this.data = item;
        this.left = null;
        this.right = null;
    }
}

public class BinaryTreeLeafCounter {

    // Метод для подсчета листьев в бинарном дереве
    static int countLeaves(Node root) {
        if (root == null)
            return 0;
        
        // Если узел является листом (нет детей слева и справа)
        if (root.left == null && root.right == null)
            return 1;
            
        // Рекурсивно считаем листья в левом и правом поддереве
        else
            return countLeaves(root.left) + countLeaves(root.right);
    }

    public static void main(String[] args) {
        /* Пример бинарного дерева:
              1
           /     \
          2       3
         / \     /
        4   5   6
               /
              7
        */
        
        // Создаем дерево вручную
        Node root = new Node(1); 
        root.left = new Node(2); 
        root.right = new Node(3); 
        root.left.left = new Node(4); 
        root.left.right = new Node(5); 
        root.right.left = new Node(6); 
        root.right.left.left = new Node(7); 
        
        // Вычисляем количество листьев
        System.out.println("Количество листьев в данном бинарном дереве: " + countLeaves(root));
    }
}

вывод:Количество листьев в данном бинарном дереве: 3
