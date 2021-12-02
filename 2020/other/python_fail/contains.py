import bag


class Contains():
    ''' directed edge '''

    def __init__(self, value, bag: bag.Bag):
        self.value = value
        self.bag = bag
