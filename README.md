## This is the version 1 of Producer and Consumer modules 

### Files 
    - producer.py : This file is the consumer which uses subprocess to call random_log, random_message and custom_input.It captures the stdout and stderr and sends to the redis stream mentioned using the flag.
    - consumer.py : Listens to a specifc stream mentioned using the flag either from the beginning or continue.
    - random_log : Produces random logs for n seconds and sends to the stderr.
    - random_message : Produces random messages for n seconds and sends to stdout.
    - custom_input : Waits for input from the user and sends it to stdout till you type exit

### Usage 
    - Please use the producer to stream the outputs to Redis along with helper modules.
    - You can connect multiple consumers to the producer, make sure that you pass the stream id when you do.

### Design choices 
    - The consumer was designed in mind that the redis server might be running in places other than default, so flags were provided to take that as an input, coming to stream_id and starting point, both were made to give the user ability to view the stream from where they want and which stream they want. Connection Pool was added becauses why not?
    - The producer was construted to mainly take and run python scripts and capture both its stderr and stdout, to showcase it capturing stderr we can run random_log and for stdout we can use random message. To add the capablity of sending user text to the stream, custom_input was made.

### Good to have features which are absent 
    - The producer having the ability to run any UNIX command as a subprocess.
    - ~~Maybe check if they work in Windows??~~ Not touching windows unless I am paid to do so.

### v2? 
    - To familiarize with Web sockets, the plan is essentialy to create a server which gets the data stream through sockets, the server puts it into the Redis stream and later when any user wants to view the streams, they can get it via sockets.
