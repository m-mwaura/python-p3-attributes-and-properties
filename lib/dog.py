#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    approved_breeds = ["Labrador", "Beagle", "Bulldog", "Pug"]  
    
    def __init__(self, name="Unknown", breed=None):
        if not name or not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            return  
        
        self.name = name
        
        if breed and breed not in Dog.approved_breeds:
            print("Breed must be in list of approved breeds.")
            return
        
        self.breed = breed if breed else "Unknown"

