class ListElement:

    def __init__(self, data, next_=None):
        self.next_ = next_
        self.data = data

    def __contains__(self, item):
        return self.find(item)

    def find(self, item):
        el = self
        while el:
            if el.data == item:
                return el
            el = el.next_
        return None
