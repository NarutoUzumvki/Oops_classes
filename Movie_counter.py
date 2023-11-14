from random_list import *

class Customer :
    def __init__(self, name ):
        self.name = name
        # self.seat_no = seat_no
        
    def generate_seat_no(self):
        seat = generate_random(15)
        for i in range(len(seat)) :
            number = seat[i]
        return number

    def __str__(self) :
        return self.name + self.lang + str(self.seat_no)


class Movie :
    def __init__(self) :
        self.movies = {}

    def add(self, title, lang, price):
        self.title = title
        self.lang = lang
        self.price = price
        # self.movies["Title"] = title
        # self.movies["Language"] = lang
        # self.movies["Price"] = price

    def remove(self, title, lang) :
        self.movies.pop(title)
    
    def __str__ (self):
        return self.title + self.lang + self.price


class Ticket_Generator:
    def __init__(self, movie, customer ) :
        self.movie = movie
        self.customer = customer

    def generate_ticket(self) :
        seat_number = self.customer.generate_seat_no()
        
        ticket_str = (f"Dear {self.customer.name}, Your Seat.No is : {seat_number}\n")
        ticket_str += (f"Your Movie-Name is {self.movie.title } \n")
        ticket_str += (f"Language : {self.movie.lang} , and your Price is : Rs.{self.movie.price} \n") 

        return ticket_str


if __name__ == "__main__" :
    movie1 = Movie()
    movie1.add("'ultimate_kick'", "English", 300)
    movie2 = Movie()
    movie2.add("'Criss-cross-hub'", "Japanese", 200)
    movie3 = Movie()
    movie3.add("Avatar", "English", 250)

    customer1 = Customer("Vijay")
    
    ticket1 = Ticket_Generator(movie1, customer1)
    bill1 = ticket1.generate_ticket()
    print(bill1)

    customer2 = Customer("Naruto")
    ticket2 = Ticket_Generator(movie2, customer2)
    bill2 = ticket2.generate_ticket()
    print(bill2)

    customer3 = Customer("Peter")
    ticket3 = Ticket_Generator(movie3, customer3)
    bill3 = ticket3.generate_ticket()
    print(bill3)

