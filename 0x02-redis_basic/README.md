Redis Basic

This repository contains the code for a short specialization course on Redis basics. The course covers the following topics:

Installing Redis on Ubuntu 18.04
Using Redis commands with Python
Working with different data types in Redis (strings, lists)
Caching with Redis
Learning Objectives

By the end of this course, i am able to:

Use Redis for basic operations
Use Redis as a simple cache
Write Python code to interact with Redis
Requirements

Ubuntu 18.04 LTS
Python 3.7
pip
Getting Started

Clone this repository:
Bash
git clone https://github.com/your-username/alx-backend-storage.git
Use code with caution.
content_copy
Navigate to the project directory:
Bash
cd alx-backend-storage/0x02-redis_basic
Use code with caution.
content_copy
Install the required Python library:
Bash
pip3 install redis
Use code with caution.
content_copy
Running the Tests

There are no automated tests included in this repository. However, you can manually test your code by running the provided Python scripts.

Code Structure

The code for this course is located in the exercise.py file. This file contains several classes and functions that demonstrate how to use Redis with Python.

Exercises

The course is divided into several exercises that cover different aspects of Redis. Each exercise includes instructions and code examples.

Writing strings to Redis: This exercise covers how to create a Cache class that can store strings in Redis.
Reading from Redis and recovering original type: This exercise demonstrates how to retrieve data from Redis and convert it back to its original data type.
Incrementing values: This exercise shows how to use the INCR command to increment values stored in Redis.
Storing lists: This exercise covers how to store and retrieve lists in Redis using commands like RPUSH and LRANGE.
Retrieving lists: This exercise demonstrates how to display the history of calls to a function that stores data in a Redis list.
Contribution

This repository is currently not intended for external contributions.

License

This repository is licensed under the MIT License. Please refer to the LICENSE file for more details.

Additional Resources

Redis Documentation: https://redis.io/docs/latest/
Redis Python Client: https://redis.io/docs/latest/develop/connect/clients/python/
