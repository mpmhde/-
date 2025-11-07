class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def count_leaves(root):
    if root is None:
        return 0
    
    # Если узел является листом (нет потомков)
    if root.left is None and root.right is None:
        return 1
    
    # Рекурсивно считаем листья слева и справа
    left_count = count_leaves(root.left)
    right_count = count_leaves(root.right)
    
    return left_count + right_count


# Пример использования
if __name__ == "__main__":
    # Создаем дерево вручную
    tree_root = TreeNode(1)
    tree_root.left = TreeNode(2)
    tree_root.right = TreeNode(3)
    tree_root.left.left = TreeNode(4)
    tree_root.left.right = TreeNode(5)
    tree_root.right.left = TreeNode(6)
    tree_root.right.right = TreeNode(7)

    print("Количество листьев:", count_leaves(tree_root))  # Результат должен быть 4


вывод:  Количество листьев: 4
