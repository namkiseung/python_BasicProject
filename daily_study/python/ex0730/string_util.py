# -*- coding : utf-8 -*-

def word_counter(file_name):
    with open(file_name, "r") as f:
        msg = f.read()
    words = len(msg.split())
    lines = len(msg.split("\n"))
    return words, lines