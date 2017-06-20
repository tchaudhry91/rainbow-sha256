import hashlib

"""
Return SHA256 digest for the given string
"""
def get_SHA256_digest(unicode_string):
    return hashlib.sha256(unicode_string.encode('utf-8')).hexdigest()
