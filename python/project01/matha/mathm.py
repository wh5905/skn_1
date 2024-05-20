class Mathc:
    def __init__(self):
        self.vlaue1 = 1
        self.vlaue2 = 2

    def __eq__(self, value):
        return self.vlaue1 == self.vlaue2

    def __ne__(self, value):
        return self.vlaue1 != self.vlaue2

    def __gt__(self, value):
        return self.vlaue1 > self.vlaue2

    def __ge__(self, value):
        return self.vlaue1 >= self.vlaue2

    def __it__(self, value):
        return self.vlaue1 < self.vlaue2

    def __le__(self, value):
        return self.vlaue1 <= self.vlaue2
