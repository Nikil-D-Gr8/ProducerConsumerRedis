## This is the version 1 of Producer and Consumer modules 

### Files 
    - producer.py : This file is the consumer which uses subprocess to call random_log, random_message and custom_input.It captures the stdout and stderr and sends to the redis stream mentioned using the flag.
    - consumer.py : Listens to a specifc stream mentioned using the flag either from the beginning or continue.
    - random_log : Produces random logs for n seconds and sends to the stderr.
    - random_message : Produces random messages for n seconds and sends to stdout.
    - custom_input : Waits for input from the user and sends it to stdout till you type exit
