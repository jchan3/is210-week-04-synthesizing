#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that converts Fahrenheit to Celsius."""


import decimal


ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """Converts a parameter from Fahrenheit to Celsius.

    Args:
        degrees(float): A Fahrenheit variable.

    Returns:
        decimal: A celsius value.

    Examples:

        >>> fahrenheit_to_celsius(212)
        Decimal('100')

    """
    return ((decimal.Decimal(degrees) - 32) * 5) / 9


def celsius_to_kelvin(degrees):
    """Converts a parameter from Celsius to Kelvin.

    Args:
        degrees(float): A celsius variable.

    Returns:
        decimal: A kelvin value.

    Examples:

        >>> celsius_to_kelvin(100)
        Decimal('373.15')

    """
    return ABSOLUTE_DIFFERENCE + degrees


def fahrenheit_to_kelvin(degrees):
    """Converts a parameter from Fahrenheit to Kelvin.

    Args:
        degrees(float): A Fahrenheit variable.

    Returns:
        decimal: A kelvin value.

    Examples:

        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')

    """
    return celsius_to_kelvin(fahrenheit_to_celsius(degrees))
