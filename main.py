import tkinter as tk
from typing import List, Union


# Custom exception for division by zero
class DivideByZeroException(Exception):
    pass


# Calculation class to store each operation
class Calculation:
    def __init__(self, operation: str, operand1: Union[int, float], operand2: Union[int, float],
                 result: Union[int, float]):
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = result

    def __repr__(self) -> str:
        return f"{self.operand1} {self.operation} {self.operand2} = {self.result}"


class Calculator:
    history: List[Calculation] = []

    def __init__(self):
        self.running_total = 0
        self.buffer = "0"
        self.previous_operator = None

    def add(self, a: float, b: float) -> float:
        result = a + b
        self._add_to_history('+', a, b, result)
        return result

    def subtract(self, a: float, b: float) -> float:
        result = a - b
        self._add_to_history('-', a, b, result)
        return result

    def multiply(self, a: float, b: float) -> float:
        result = a * b
        self._add_to_history('*', a, b, result)
        return result

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise DivideByZeroException("Cannot divide by zero!")
        result = a / b
        self._add_to_history('/', a, b, result)
        return result

    def _add_to_history(self, operation: str, a: float, b: float, result: float) -> None:
        calculation = Calculation(operation, a, b, result)
        self.__class__.history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        return cls.history[-1] if cls.history else None

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history

    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()

    @staticmethod
    def is_operator_valid(operator: str) -> bool:
        return operator in ['+', '-', '*', '/']


# GUI for calculator
class CalculatorGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Calculator")

        self.calculator = Calculator()

        self.screen = tk.Label(root, text="0", anchor='e', font=("Arial", 24), bg="white", fg="black")
        self.screen.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        # Button layout
        buttons = [
            ('C', 1, 0), ('←', 1, 1), ('/', 1, 2), ('*', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('-', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('+', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('=', 4, 3),
            ('0', 5, 0)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", 20), command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, sticky='nsew')

        # Make the layout flexible
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def button_click(self, value):
        if value in "0123456789":
            self.handle_number(value)
        else:
            self.handle_symbol(value)
        self.screen.config(text=self.calculator.buffer)

    def handle_number(self, number_string: str) -> None:
        if self.calculator.buffer == "0":
            self.calculator.buffer = number_string
        else:
            self.calculator.buffer += number_string

    def handle_symbol(self, symbol: str) -> None:
        try:
            if symbol == "C":
                self.calculator.buffer = "0"
                self.calculator.running_total = 0
            elif symbol == "←":
                self.calculator.buffer = self.calculator.buffer[:-1] or "0"
            elif symbol == "=":
                if self.calculator.previous_operator is None:
                    return
                self.calculator.running_total = self.perform_operation(int(self.calculator.buffer))
                self.calculator.buffer = str(self.calculator.running_total)
                self.calculator.previous_operator = None
            elif symbol in "+-*/":
                if self.calculator.previous_operator:
                    self.calculator.running_total = self.perform_operation(int(self.calculator.buffer))
                else:
                    self.calculator.running_total = int(self.calculator.buffer)
                self.calculator.previous_operator = symbol
                self.calculator.buffer = "0"
        except DivideByZeroException:
            self.screen.config(text="Error: Divide by Zero")

    def perform_operation(self, value: int) -> int:
        if self.calculator.previous_operator == "+":
            return self.calculator.add(self.calculator.running_total, value)
        elif self.calculator.previous_operator == "-":
            return self.calculator.subtract(self.calculator.running_total, value)
        elif self.calculator.previous_operator == "*":
            return self.calculator.multiply(self.calculator.running_total, value)
        elif self.calculator.previous_operator == "/":
            return self.calculator.divide(self.calculator.running_total, value)


if __name__ == "__main__":
    root = tk.Tk()
    calculator_app = CalculatorGUI(root)
    root.mainloop()
