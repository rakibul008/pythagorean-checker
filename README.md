\# Pythagorean Theorem Checker 



Overview

This Python terminal application is designed to securely authenticate a user and then provide a robust, interactive tool for verifying Pythagorean triples. Built with a strong focus on \*\*Software Quality Assurance\*\*, the program features extensive input validation, security protocols, and dynamic formatting to handle unpredictable user inputs gracefully.



Key Features



1. Secure Authentication

Attempt Limiting: Users are restricted to a maximum of 3 login attempts to prevent brute-force attacks.

Input Validation: The username must be strictly 6 alphabetical characters, and the password must contain a specific substring.

Generic Error Handling: To prevent username enumeration, failed login attempts return a secure, generic "Invalid username or password" message rather than specifying which credential failed.


2. Pythagorean Checker

Dynamic Math Rendering: The system does not force the user to input the hypotenuse last. It actively scans the inputs, identifies the largest integer, and dynamically restructures the a²+ b² = c² ;formula to provide an accurate step-by-step mathematical printout.

Strict Data Types: The script safely catches `ValueError` exceptions if a user attempts to input strings, special characters, or floating-point decimals.

Geometric Validation: The program enforces positive integers (`> 0`), preventing mathematical false positives from negative numbers or zero.



