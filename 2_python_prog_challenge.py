import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

service_tickets = {
    1: {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    2: {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def next_id():  
    last_id = 0
    for id in service_tickets.keys():
        if id > last_id:
            last_id = id
    return last_id + 1

def new_ticket(): 
    new_id = next_id()
    while True:
        customer = input("Please enter the customer name: \n")
        issue = input("Please state the issue: \n")
        print(f"Customer: {customer}, Issue: {issue}")
        correct = input("Is this information correct? (y/n)".lower())
        if correct == 'y' : 
            service_tickets[new_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
            break
        else:
            clear()
            continue
        

def update_ticket():
    ticket_id = int(input("Enter the ticket ID to update: "))
    if ticket_id in service_tickets:
        if service_tickets[ticket_id]["Status"] == "closed":
            print(f"Ticket ID {ticket_id} is already closed.")
        else:
            service_tickets[ticket_id]["Status"] = "closed"
            print(f"Ticket ID {ticket_id} has been closed.")
    else:
        print(f"Ticket ID {ticket_id} does not exist.")

def display_tickets():
    for ticket_id, details in service_tickets.items():
        print(f"Ticket ID: {ticket_id}")
        print(f"  Customer: {details['Customer']}")
        print(f"  Issue: {details['Issue']}")
        print(f"  Status: {details['Status']}")
        print()
        
def main():
    while True:
        ans = input('''
SERVICE TICKET MANAGER 
Enter the corresponding number for the action you'd like to take: 
    1 - Open a new service ticket.
    2 - Close a service ticket.
    3 - Display all sevice tickets. 
    4 - Quit
''')
        if ans == "1":
            clear()
            new_ticket()
        elif ans == "2":
            clear()
            update_ticket()
        elif ans == "3":
            clear()
            display_tickets()      
        elif ans == "4":
            clear()
            print("Have a great day!")
            break
        else: 
            print("Enter something write for once in your life") 

main()