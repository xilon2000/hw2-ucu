# Hello App

## Project Overview

Hello App is a client-server applaiction.
- hello_server is a REST service. It defines ednpoint GET / that returns "hello world" as response.
- hello_client is a CLI utility and a REST client to hello_server. You can use hello_client to sent requests to hello_server.

---

## Contents

* [Setup the application](#setup-the-application)
* [Run the application](#run-the-application)
* [Cleanup the application](#cleanup-the-application)

---

## Setup the application

1. Build an image for hello_server.

![](screenshots/01.%20docker%20build%20server.jpg)

2. Build an image for hello_client.

![](screenshots/02.%20docker%20build%20client.jpg)

3. Create hello_network.

![](screenshots/03.%20docker%20network%20create.jpg)

## Run the application

1. Run hello_server in hello_network. 

![](screenshots/04.%20docker%20run%20hello_server.jpg)

2. Run hello_client in hello_network to call endpoint GET / on hello_server.

![](screenshots/05.%20docker%20run%20client.jpg)

## Cleanup

1. Stop hello_server. hello_server container is removed because it was created by `docker run --rm ...`.

![](screenshots/06.%20docker%20stop%20hello_server.jpg)

2. Remove images hello_server and hello_client.

![](screenshots/07.%20docker%20remove%20images.jpg)

3. Remove hello_network.

![](screenshots/08.%20docker%20remove%20network.jpg)

