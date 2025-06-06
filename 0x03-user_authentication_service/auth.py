#!/usr/bin/env python3
""" Auth class defintion
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """ hash password function """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
