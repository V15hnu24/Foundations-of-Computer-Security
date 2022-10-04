#FCS Assignment 1, question 1
#Name:
#Roll number:

import gmpy2
import cryptography

def alice_generates_symmetric_key():
    ''' 
    A function that uses Fernet to create a shared symmetric key K.
    This key should be used to encrypt Bob and Alice's communications.
    But before that, it needs to be sent to Bob.

    Input: NA
    Return: the symmetric key
    '''
    pass

def bob_generates_asymmetric_keys(p ,q):
    '''
    A function that takes in prime numbers p and q and generates 
    the public and private keys for Bob as per RSA. Note that you are 
    not allowed to use loops to find e or d.

    Input: p, q (upto 1023 digits long)
    Return: Bob's public key (e,n) as a tuple
    '''
    pass

def alice_sends_symmetric_key(k, n, e):
    '''
    A function that Alice uses to encrypt the symmetric key
    using Bob's public key. The ciphertext is sent to Bob.

    Input: the symmetric key k, Bob's public key e, n.
    Return: encrypted ciphertext
    '''
    pass

def bob_decrypts_symmetric_key(c, d, n):
    '''
    A function that Bob uses to decrypt the ciphertext c using his private key.
    The decrypted message would give him the symmetric key.

    Input: the ciphertext c, Bob's private key d, n.
    Return: the symmetric key
    '''
    pass

def bob_sends_message(m, k):
    '''
    A function that takes a message m, shared key k and uses Fernet to encrypt m.

    Input: the message m, the shared key k
    Return: encrypted ciphertext
    '''
    pass

def alice_decrypts_message(c_, k):
    '''
    A function that takes an encrypted message c_, shared key k and uses Fernet to decrypt c_.

    Input: the ciphertext c_, the shared key k
    Return: plaintext message
    '''
    pass

if __name__=="main":
    # p, q and the message m will be taken as inputs from the user.
    pass
