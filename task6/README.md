# Shared Storage Streamlit App

## Project Overview

A multi-instance Streamlit web application that enables users \
to upload CSV files to a shared volume through any active instance \
and instantly inspect, browse, and analyze the uploaded dataset across \
all running instances.

---

## Contents

* [Setup the application](#setup-the-application)
* [Run the application](#run-the-application)
* [Work with the application](#work-with-the-application)
* [Cleanup the application](#cleanup-the-application)

---

## Setup the application

1. Create a named volume.

![](./screenshots/01.%20docker%20volume%20create.jpg)

2. Check that the volume has been created.

![](./screenshots/02.%20docker%20volume%20ls.jpg)

3. Build an image.

![](./screenshots/03.%20docker%20build.jpg)

4. Check that the image has been built.

![](./screenshots/04.%20docker%20image%20ls.jpg)

## Run the application

1. Run two instances of the application that have access to the same volume.

![](./screenshots/05.%20docker%20run.jpg)

2. Check that the two instances are running.

![](./screenshots/06.%20docker%20ps.jpg)

## Work with the application

1. Open the main web page of the first instance of the application.

![](./screenshots/07.%20task6_instance1_web_page.jpg)

2. Open the main web page of the second instance of the application.

![](./screenshots/07.%20task6_instance2_web_page.jpg)

3. Upload file ./data/taxi_zone_lookup.csv to the second instance and save it on the volume.

![](./screenshots/08.%20upload_file_to_task6_instance2.jpg)

4. Refresh the main web page of the first instance to see the uploaded file.

![](./screenshots/09.%20refresh_task6_instance1_wep_page.jpg)

## Cleanup

1. Remove the application instances.

![](./screenshots/10.%20docker_rm__task6_instance1__task6_instance2.jpg)

2. Remove the image

![](./screenshots/11.%20docker_rmi__task6_image.jpg)

3. Remove the volume.

![](./screenshots/12.%20docker_volume_rm__task6_volume.jpg)

