#!/usr/bin/env python3

"""
Stanford CS106AP Crypto Project
"""

import sys

# provided ALPHABET constant - list of the regular alphabet
# in lowercase. Refer to this simply as ALPHABET in your code.
# This list should not be modified.
ALPHABET = list('abcdefghijklmnopqrstuvwxyz')


def key_slug(key):
    """
    Given a key string, return the len-26 slug list for it.
    >>> key_slug('z')
    ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> key_slug('Bananas!')
    ['b', 'a', 'n', 's', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    >>> key_slug('Life, Liberty, and')
    ['l', 'i', 'f', 'e', 'b', 'r', 't', 'y', 'a', 'n', 'd', 'c', 'g', 'h', 'j', 'k', 'm', 'o', 'p', 'q', 's', 'u', 'v', 'w', 'x', 'z']
    >>> key_slug('Zounds!')
    ['z', 'o', 'u', 'n', 'd', 's', 'a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 't', 'v', 'w', 'x', 'y']
    """
    lst = []
    for i in range(len(key)):
        if (key[i].lower() not in lst) and (key[i].isalpha()):
            lst.append(key[i].lower())
    j = 0
    while j < 26:
        if ALPHABET[j] not in lst:
            lst.append(ALPHABET[j])
        j += 1
    return lst


def encrypt_char(source, slug, char):
    """
    Given source and slug lists,
    if char is in source return
    its encrypted form, otherwise
    return it unchanged.
    # Using 'z' slug for testing.
    # Can set a var within a Doctest like this.
    >>> slug = ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> encrypt_char(ALPHABET, slug, 'A')
    'Z'
    >>> encrypt_char(ALPHABET, slug, 'n')
    'm'
    >>> encrypt_char(ALPHABET, slug, 'd')
    'c'
    >>> encrypt_char(ALPHABET, slug, '.')
    '.'
    >>> encrypt_char(ALPHABET, slug, '\\n')
    '\\n'
    """
    index = 0
    encrypted = ""
    if char.lower() not in source:
        return char
    for i in range(len(source)):
        if source[i] == char.lower():
            index = i
    if char.islower():
        encrypted += slug[index].lower()
    if char.isupper():
        encrypted += slug[index].upper()
    return encrypted


def encrypt_str(source, slug, s):
    """
    Given source and slug lists and string s,
    return a version of s where every char
    has been encrypted by source/slug.
    >>> slug = ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> encrypt_str(ALPHABET, slug, 'And like a thunderbolt he falls.\\n')
    'Zmc khjd z sgtmcdqanks gd ezkkr.\\n'
    """
    encrypted = ""
    for i in range(len(s)):
        encrypted += encrypt_char(source, slug, s[i])
    return encrypted


def decrypt_str(source, slug, s):
    """
    Given source and slug lists, and encrypted string s,
    return the decrypted form of s.
    >>> slug = ['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
    >>> decrypt_str(ALPHABET, slug, 'Zmc khjd z sgtmcdqanks gd ezkkr.\\n')
    'And like a thunderbolt he falls.\\n'
    """
    return encrypt_str(slug, source, s)


def encrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the encrypted form of its lines.
    """
    slug = key_slug(key)
    out = ""
    with open(filename, 'r') as f:
        for line in f:
            out += encrypt_str(ALPHABET, slug, line)
    return out


def decrypt_file(filename, key):
    """
    Given filename and key, compute and
    print the decrypted form of its lines.
    """
    slug = key_slug(key)
    out = ""
    with open(filename, 'r') as f:
        for line in f:
            out += decrypt_str(ALPHABET, slug, line)
    return out


def main():
    args = sys.argv[1:]
    # args is the list of command line arguments
    # 2 commmand line argument patterns:
    # -encrypt key filename
    # -decrypt key filename
    # Call encrypt_file() or decrypt_file() based on the args.
    if args[0] == "-encrypt":
        print(encrypt_file(args[2], args[1]))
    if args[0] == "-decrypt":
        print(decrypt_file(args[2], args[1]))


# Python boilerplate.
if __name__ == '__main__':
    main()
