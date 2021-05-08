#!/usr/bin/python3

from brownie import Token, accounts


def main():
    return Token.deploy("Test Token", "TST", 18, 1e21, {'from': '0xe8a89c132f5Ffe4ddB31188f5D015a73f4dA1c8f'})
