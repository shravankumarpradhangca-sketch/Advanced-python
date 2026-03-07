#4. Movie Ticket Booking System and Check showtimes, book tickets, select seats, and print confirmation through OOPs cooncept in python.
class Movie:
    def __init__(self, title, showtime, available_seats):
        self.title = title
        self.showtime = showtime
        self.available_seats = available_seats
def book_ticket(self, num_seats):
        if num_seats <= self.available_seats:
            self.available_seats -= num_seats
            print(f"Successfully booked {num_seats} seats for '{self.title}' at {self.showtime}.")
        else:
            print(f"Sorry, only {self.available_seats} seats are available for '{self.title}' at {self.showtime}.")
#Example usage
movie1 = Movie("Inception", "7:00 PM", 100)
movie1.book_ticket(5)
movie1.book_ticket(97)
movie1.book_ticket(1)

#User input for booking tickets and checking showtiimes
while True:
    action = input("Enter 'book' to book tickets, 'showtime' to check showtimes, or 'quit' to exit: ").strip().lower()
    if action == 'book':
        title = input("Enter the movie title: ")
        showtime = input("Enter the showtime: ")
        num_seats = int(input("Enter the number of seats to book: "))
        movie = Movie(title, showtime, 100)  # Assuming 100 seats available for simplicity
        movie.book_ticket(num_seats)
    elif action == 'showtime':
        title = input("Enter the movie title to check showtime: ")
        print(f"Showtime for '{title}' is at 7:00 PM.")  # Placeholder showtime
    elif action == 'quit':
        print("Exiting the Movie Ticket Booking System. Goodbye!")
        break
    else:
        print("Invalid action. Please try again.") 