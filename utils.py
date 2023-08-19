"""Utility functions that can be used across your project can be placed here. For example,
functions for logging, input validation, or handling file paths could be defined in this module."""


def validate_input(input_data):
    if not input_data:
        raise ValueError("Input data is empty.")
    # Add more validation logic as needed