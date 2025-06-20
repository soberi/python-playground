# To be placed within class NumManipulator:
#   Convert decimal numbers to octal numbers.
#   Reverse an integer.
#   Print the Fibonacci series using the recursive method.
#   Return the Nth value from the Fibonacci sequence.
#   Find the average of numbers (with explanations).
#   Convert Celsius to Fahrenheit.

class NumManipulator:

    # Helper method
    def to_decimal(self, num):
        """Converts num to respective decimal representation."""
        while num > 1:
            num /= 10
        return num
    
    #   Convert decimal numbers to octal numbers.
    def decimal_to_octal(self, number, places=6):
        """Decimal to be converted on whole and fraction separately."""
        whole, decimal = str(number).split(".")

        whole = int(whole)
        decimal = int(decimal)

        # convert the whole number
        octal = oct(whole).lstrip("0o") + "."

        # convert decimal part of number
        for x in range(places):
            
            # Multiply the decimal value by 8 and separate 
            # the whole number part and decimal part
            whole, decimal = str((self.to_decimal(decimal))*8).split(".")

            # required to keep the for loop running, after the decimal is
            # converted it is checked against to_decimal()
            decimal = int(decimal)

            octal += whole

        return float(octal)

    
    #   Reverse an integer.
    def reverse_integer(self, number):
        reversed_number = str(number)[::-1]
        return int(reversed_number)


    #   Print the Fibonacci series using the recursive method.
    def fibonacci_series(self, places=11):
        
        # Initial sequence
        sequence = [0, 1]

        # Accounting for the initial sequence.
        places = places - 2

        while places > 0:
            next_int = sequence[-1] + sequence[-2]
            sequence.append(next_int)
            places -= 1

        return sequence
    

    #   Return the Nth value from the Fibonacci sequence.
    def find_fibonacci(self, position):
        # Initial sequence
        sequence = [0, 1]

        # Accounting for the initial sequence.
        position = position - 2

        while position > 0:
            next_int = sequence[-1] + sequence[-2]
            sequence.append(next_int)
            position -= 1

        return sequence[-1]


    #   Find the average of numbers (with explanations).
    def find_average(self, number_series):
        average = sum(number_series) / len(number_series)
        return average


    #   Convert Celsius to Fahrenheit.
    def celsius_to_fahrenheit(self, celsius):
        fahrenheit = (celsius * 1.8) + 32
        return fahrenheit
