#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that converts Fahrenheit to Celsius."""


import decimal


def fahrenheit_to_celsius(degrees):
    """Converts a parameter from Fahrenheit to Celsius.

    Args:
        degrees(decimal): A Fahrenheit variable.

    Returns:
        decimal: A celsius value.

    Examples:

        >>> fahrenheit_to_celsius(212)
        Decimal('100')

    """
    return (((decimal.Decimal(degrees) - 32) * 5) / 9)
