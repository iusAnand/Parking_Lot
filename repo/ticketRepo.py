class TicketRepo:

    def __init__(self):
        self.count= -1
        self.tickets = {}  # key: ticket id, value: ticket object
        

    def save_ticket(self, ticket):
        newId = self.count+1
        ticket.number = newId
        ticket.id = newId
        self.tickets[newId] = ticket
        self.count += 1
        return ticket
    def find_ticket_by_id(self, ticket_id: int):
        return self.tickets.get(ticket_id)