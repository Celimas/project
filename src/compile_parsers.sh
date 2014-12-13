#!/bin/bash
# (Re)-compiles the grako parsers for Math and Deck

rm -f g_*

grako deck.grako > g_deck.py
grako math.grako > g_math.py
