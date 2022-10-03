import random

class Node:
    def __init__(self , value=None):
        self.data_value = value
        self.next_value = None

class SingleLinkedList:
    def __init__(self):
        self.head_value = None

    # Содержится ли элемент в списке
    def contains(self, data):
        last = self.head_value
        while last:
            if data == last.data_value:
                return True
            else:
                last = last.next_value
        return False

    # Получение узла по индексу
    def get_data(self, data_index):
        try:
            last = self.head_value
            node_index = 0
            while node_index <= data_index:
                if node_index == data_index:
                    return last.data_value
                node_index += 1
                last = last.next_value
        except Exception:
            print('Индекса не существет')

    # Добавление элемента в начало
    def insert_at_start(self, new_data):
        new_node = Node(new_data)
        new_node.next_value = self.head_value
        self.head_value = new_node

    # Удаление первого элемента
    def remove_first_element(self):
        head = self.head_value
        self.head_value = self.head_value.next_value
        self.remove(head)

    # Добавление элемента в конец
    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head_value is None:
            self.head_value = new_node
            return
        last = self.head_value
        while last.next_value:
            last = last.next_value
        last.next_value = new_node

    # Удаление последнего элемента
    def remove_last_element(self):
        last = self.head_value
        while last.next_value:
            last = last.next_value
        self.remove(last.data_value) 
        
    # Удаление элемента
    def remove(self, data):
        head = self.head_value
        if head is not None:
            if head.data_value == data:
                self.head_value = head.next_value
                head = None
                return
        while head is not None:
            if head.data_value == data:
                break
            last = head
            head = head.next_value
        if head == None:
            return
        last.next_value = head.next_value
        head = None

    # Печать списка
    def print_list(self):
        value_to_print = self.head_value
        while value_to_print is not None:
            print(value_to_print.data_value)
            value_to_print = value_to_print.next_value


test = SingleLinkedList()
test.insert_at_end(1)
test.insert_at_end(2)
test.insert_at_end(3)
test.remove_first_element()
print(test.print_list())