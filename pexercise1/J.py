class NumberGuesser:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = []

    def guess(self, number, secret_number):
        self.attempts.append(number)
        guessing = True
        while guessing:
            if number == self.secret_number:
                response = f"You won after {len(self.attempts)} attempts"
                cs.send(response.encode())
                cs.close()
            elif number <= self.secret_number:
                response = f"higher"
                cs.send(response.encode())
                cs.close()
            elif number >= self.secret_number:
                response = f"lower"
                cs.send(response.encode())
                cs.close()