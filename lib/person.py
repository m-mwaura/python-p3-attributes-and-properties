#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    approved_jobs = ["Engineer", "Teacher", "Artist", "ITC"]

    def __init__(self, name="Unknown", job=None):
        if not name or not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            return 
        
        self.name = name.title()
        
        if job and job not in Person.approved_jobs:
            print("Job must be in list of approved jobs.")
            return 

        self.job = job if job else "Unknown"
