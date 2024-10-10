import tkinter as tk
from typing import Callable, Dict

class Command:
    def __init__(self, execute: Callable, name: str):
        self.execute = execute
        self.name = name

class CommandPatternCalculator:
    def __init__(self):
        self.commands: Dict[str, Command] = {
            'add': Command(self.add, 'Add two numbers'),
            'subtract': Command(self.subtract, 'Subtract two numbers'),
            'multiply': Command(self.multiply, 'Multiply two numbers'),
            'divide': Command(self.divide, 'Divide two numbers'),
            'menu': Command(self.show_menu, 'Display available commands')
        }

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Divide by zero"
        return a / b

    def show_menu(self):
        return '\n'.join([f"{cmd}: {self.commands[cmd].name}" for cmd in self.commands])

    def repl(self):
        while True:
            user_input = input("Enter a command (or 'menu' for help): ").strip().lower()
            if user_input == 'exit':
                break
            elif user_input in self.commands:
                if user_input == 'menu':
                    print(self.commands[user_input].execute())
                else:
                    try:
                        a = float(input("Enter first number: "))
                        b = float(input("Enter second number: "))
                        print(f"Result: {self.commands[user_input].execute(a, b)}")
                    except ValueError:
                        print("Invalid input. Please enter numbers.")
            else:
                print("Unknown command. Type 'menu' for a list of commands.")
import importlib
import os

class PluginLoader:
    def __init__(self, plugin_directory="plugins"):
        self.plugin_directory = plugin_directory

    def load_plugins(self):
        plugins = {}
        for filename in os.listdir(self.plugin_directory):
            if filename.endswith(".py"):
                plugin_name = filename[:-3]
                module = importlib.import_module(f"{self.plugin_directory}.{plugin_name}")
                if hasattr(module, 'create_plugin'):
                    plugin = module.create_plugin()
                    plugins[plugin.name] = plugin
        return plugins
if __name__ == "__main__":
    calculator = CommandPatternCalculator()
    calculator.repl()
