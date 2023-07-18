class Parking():
    def __init__(self, total_spaces):
        self.tickets = list(range(1,total_spaces+1))
        self.parking_spaces = list(range(1,total_spaces+1))
        self.current_ticket ={}
    

    def takeTicket(self):
        if len(self.tickets) > 0:
            ticket_number = self.tickets.pop(0)
            self.parking_spaces.pop(0)
            self.current_ticket = {"ticket_number": ticket_number, "paid": False}
            print(f"Please take ticket number {ticket_number}.")
        else:
            print("Sorry, the parking garage is full.")

    def payForParking(self):
        if self.current_ticket:
            payment = input("please pay the amount $9.00: ")
            if float(payment) == 9.00:
                self.current_ticket["paid"] = True
                print("Ticket has been paid. You have 15 minutes to leave.")
            else:
                print("Payment cannot be empty.")
        else:
            print("Please take a ticket first.")

    def leaveGarage(self):
        if self.current_ticket:
            if self.current_ticket["paid"]:
                print("Thank you, have a nice day!")
                self.parking_spaces.append(self.current_ticket["ticket_number"])
                self.tickets.append(self.current_ticket["ticket_number"])
                self.current_ticket = {}
            else:
                payment = input("Please pay for your ticket: ")
                if payment:
                    self.current_ticket["paid"] = True
                    print("Thank you, have a nice day!")
                    self.parking_spaces.append(self.current_ticket["ticket_number"])
                    self.tickets.append(self.current_ticket["ticket_number"])
                    self.current_ticket = {}
                else:
                    print("Payment cannot be empty.")
        else:
            print("Please take a ticket first.")


garage = Parking(total_spaces=10)

garage.takeTicket()
garage.payForParking()
garage.leaveGarage()
