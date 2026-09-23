# Iterators and Generators

#Part-A Custom Iterator
print("PartA")

class UserIterator:
    def __init__(self,users: list[dict]) -> None:
        self.users = users
        self.index = 0
    
    def __iter__(self)-> UserIterator :
        return self
    
    def __next__(self) -> dict:
        if self.index < len(self.users):
            val = self.users[self.index]
            self.index += 1
            return val
        raise StopIteration

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
]

user_iterator = UserIterator(users)

for user in user_iterator:
    print(user)

#Part-B Generator
print("PartB")

def user_generator(users: list[dict]) :
    index = 0
    while index < len(users):
        yield users[index]
        index += 1

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
]

for user in user_generator(users):
    print(user)

generator = user_generator(users)

print(next(generator))
print(next(generator))
print(next(generator))