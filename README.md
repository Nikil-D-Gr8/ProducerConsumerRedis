## This is version 1 of the Producer and Consumer modules

### Files

* **producer.py**
  This file acts as the producer. It uses subprocess to call `random_log`, `random_message`, and `custom_input`. It captures both stdout and stderr and sends them to the Redis stream specified using a flag.

* **consumer.py**
  Listens to a specific stream mentioned via a flag, either from the beginning or from a given point.

  * **random_log**
    Produces random logs for *n* seconds and sends them to stderr.

  * **random_message**
    Produces random messages for *n* seconds and sends them to stdout.

  * **custom_input**
    Waits for user input and sends it to stdout until you type `exit`.


### Usage

* Use the producer to stream outputs to Redis along with the helper modules.
* You can connect multiple consumers to the producer. Make sure you pass the correct stream ID when doing so.


### Design Choices

* The consumer was designed with the assumption that the Redis server may run on non-default locations. Therefore, flags were added to configure this.
  Additionally, both `stream_id` and starting point options allow users to control which stream they want and from where they want to start reading.
  A connection pool was added—because why not?

* The producer was constructed to primarily run Python scripts as subprocesses and capture both stdout and stderr.
  To demonstrate stderr capture, `random_log` can be used, and for stdout, `random_message` works.
  To support user input streaming, `custom_input` was added.


### Good-to-have Features (Currently Missing)

* The producer should support running any UNIX command as a subprocess. ( adding shell=True will work, not verified)
* ~~Maybe check if it works on Windows?~~ Not touching Windows unless I’m paid to do so.

### v2?

* To get familiar with WebSockets, the plan is to create a server that receives the data stream via sockets from "workers".
* The server will push this data into a Redis stream.
* Later, users can view the streams via WebSockets as well.

