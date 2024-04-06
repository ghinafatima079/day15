# Book class
class Book:
    def __init__(self,title,author,published_year):
        self.title=title
        self.author=author
        self.pb=published_year
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Published Year: {self.pb}")
book1=Book("Harry Potter","JKRowling",1997)
book1.display_info()

# Implement a Python decorator called time_it that calculates and prints the execution time of a function. 
# The decorator should be used to decorate a function of your choice.
import time
def time_it(fn):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=fn(*args,**kwargs)
        end_time=time.time()
        seconds=end_time-start_time
        print(f"The function {fn.__name__} took {seconds} seconds to run.")
        return result
    return wrapper

@time_it
def name():
    first=input("Enter first name:")
    last=input("Enter last name:")
    print(f"Full Name: {first} {last}")
    
name()