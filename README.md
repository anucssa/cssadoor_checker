cssadoor_checker
================

Checks to see if the door is open and updates the space api.

The script runs in an infinite loop
If a change is detected on pin 3 (second from the top on the left),
it will try to send off a request to the space api.  If that fails,
it will retry a few times before giving up and returning to the main
waiting loop.
