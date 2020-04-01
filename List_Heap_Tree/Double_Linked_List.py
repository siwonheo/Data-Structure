class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.previous = None

    def get_item(self): return self.item

    def get_next(self): return self.next

    def get_previous(self): return self.previous

    def set_item(self, new_item):
        self.item = new_item

    def set_next(self, new_next):
        self.next = new_next

    def set_previous(self, new_previous):
        self.previous = new_previous

class DList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        if self.head == None:
            self.head = Node(item)

        else:
            temp = Node(item)
            temp.set_next(self.head)
            self.head.set_previous(temp)
            self.head = temp

    def size(self):
        current = self.head
        count = 0
        while count != None:
            count += 1
            current = current.get_next()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current!= None and not found:
            if current.get_item() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def delete(self,item):
        if self.head.get_item() == item:
            self.head = self.head.get_next()
            self.head.set_previous(None)

        else:
            current = self.head
            found = False
            while not found:
                if current.get_item() == item:
                    found = True
                else:
                    current = current.get_next()
            if self.get_next() != None:
                current.get_previous().set_next(current.get_next())
                current.get_next().set_previous(current.get_previous())
            else:
                current.get_previous().set_next(None)

    def append(self, item):
        if self.head == None:
            self.head = Node(item)

        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            temp = Node(item)
            current.set_next(temp)
            temp.set_previous(current)

    def pop_first(self):
        if self.head == None:
            print("List is empty")

        else:
            if self.head.get_next() == None:
                self.head = None
            else:
                self.head = self.head.get_next()
                self.head.set_previous(None)

    def pop_last(self):
        if self.head == None:
            print("List is empty")

        else:
            if self.head.get_next() == None:
                self.head = None

            else:
                current = self.head
                while current.get_next() != None:
                    currnet = current.get_next()
                current.get_previous().set_next(None)

    def insert_after(self, item, x):
        if self.head == None:
            print("List is empty.")

        else:
            current = self.head
            found = False
            while current != None and not found:
                if current.get_item() == x:
                    found = True

                else:
                    current = current.get_next()

            if found == False:
                print("Item not on the list")

            else:
                temp = Node(item)
                temp.set_next(current.get_next())
                temp.set_previous(current)
                if current.get_next() != None:
                    current.get_next().set_previous(temp)
                current.set_next(temp)

    def insert_before(self,x,item):
        if self.head == None:
            print("List is empty")

        else:
            current = self.head
            found = False
            while current != None and not found:
                if current.get_item() == x:
                    found = True

                else:
                    current = current.get_next()

            if found == False:
                print("item not in the list")

            else:
                temp = Node(item)
                temp.set_next(current)
                temp.set_previous(current.get_previous())
                if current.get_previous() != None:
                    current.get_previous().set_next(temp)
                else:
                    current.get_previous().set_next(temp)
                    self.head = temp
                current.get_previous(temp)


if __name__ == "__main__":
    d = DList()
    d.add(30)
    d.add(20)
    d.add(15)
    d.append(35)
    d.append(90)
    d.pop_last()
    d.pop_first()
    d.delete(20)
    current = d.head
    while current:
        if current.get_next() != None:
            print(current.get_item(), '<=>', end = ' ')
        else:
            print(current.get_item())
        current = current.get_next()