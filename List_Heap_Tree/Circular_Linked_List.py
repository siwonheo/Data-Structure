class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

    def get_item(self): return self.item

    def get_next(self): return self.next

    def set_item(self, new_item):
        self.item = new_item

    def set_next(self, new_next):
        self.next = new_next

class CList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        if self.is_empty():
            temp.set_next(temp)
            self.head = temp

        else:
            temp.set_next(self.head.get_next())
            self.head.set_next(temp)


    def search(self,item):
        temp = self.head.get_next()
        current = self.head
        found = False
        if current.get_next() == current:
            return current.get_item() == item

        else:
            while current.get_next() != temp and not found:
                if current.get_item() == item:
                    found = True
                else:
                    current = current.get_next()
            return found

    def append(self, item):
        temp = Node(item)
        if self.is_empty():
            temp.set_next(temp)
            self.head = temp

        else:
            temp.set_next(self.head.get_next())
            self.head.set_next(temp)
            self.head = temp

    def pop_first(self):
        if self.head == None:
            print("List is empty")
        temp = self.head.get_next()
        if temp == temp.get_next():
            self.head = None

        else:
            self.head.set_next(temp.get_next())


if __name__ == "__main__":
    c = CList()
    c.add(30)
    c.add(45)
    c.append(20)
    c.add(55)
    current = c.head
    while current.get_next() != c.head:
        print(current.get_item(), '->', end = ' ')
        current = current.get_next()
    print(current.get_item(), '->')