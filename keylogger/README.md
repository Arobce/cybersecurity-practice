# Keylogger

Keylogger that has two reporting mechanism. Files based and email based.

## Basic Algorithm

- Get keyboard entry from a `keyboard` library
- Store locally
- On a fixed interval
    - If file reporting
        - Save to log
    - If email reporting
        - Send email to the specified email

