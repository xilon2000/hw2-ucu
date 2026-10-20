# Project Overview

This project demonstrates how to use a multi-stage build to create a lightweight Go image based on scratch.

# How to Build and Run

1. Build an image.

```bash
docker build -t task8_image . 
```

2. Run a container from the image.

```bash
docker run --rm task8_image
```

3. Remove the image.

```bash
docker rmi task8_image
```