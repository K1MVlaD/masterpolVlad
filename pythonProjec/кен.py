class Node:
    def __init__(self, data: float):
        self.data: float = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: float):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def insert_after(self, target_data, data):
        current_node = self.head
        while current_node:
            if current_node.data == target_data:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    def calculate_average(self) -> float:
        current_node = self.head
        total_sum = 0.0
        count = 0

        while current_node:
            total_sum += current_node.data
            count += 1
            current_node = current_node.next

        return total_sum / count if count > 0 else 0.0


# Создание однонаправленного списка
linked_list = LinkedList()
linked_list.append(1.5)
linked_list.append(2.3)
linked_list.append(3.7)
linked_list.append(4.1)

print("Список до изменений:")
linked_list.print_list()

# Вставка элемента после первого элемента с аналогичным значением
linked_list.insert_after(2.3, 2.8)

print("Список после изменений:")
linked_list.print_list()

# Вычисление среднего арифметического элементов списка
average = linked_list.calculate_average()
print(f"Среднее арифметическое элементов списка: {average}")