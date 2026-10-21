# Scipt Overview

main.py script reads and outputs the content of text files passed as arguments:

```bash
python3 -m main file1 file2 ...
```

Dockerfile_cmd and Dockerfile_entrypoint build identical images, differing only in their default execution directives:

```Dockerfile
CMD ["python3", "-m", "main"] 

versus 

ENTRYPOINT ["python3", "-m", "main"].
```

---

## Case 1. Dockerfile_entrypoint

```bash
docker build -t task5_image -f Dockerfile_entrypoint .
```

**Run the script in the container. No parameters are passed in.**

```bash
docker run -it --rm --name task5_c task5_image

No file names were passed.
```

**Run the script in the container with file that doesn't exist in the container.**

```bash
docker run -it --rm --name task5_c task5_image ./data/report1.csv

Error reading file ./data/report1.csv:
[Errno 2] No such file or directory: './data/report1.csv'
```

```text
Explanation:
    The script exits with error because /app/data/report1.csv doesn't exist in the container.
```

**Run the script in the container with file that exists on the host.**

```bash
docker run -it --rm --name task5_c -v ./data/report1.csv:/app/data/report1.csv task5_image ./data/report1.csv

File: ./data/report1.csv
Content:
Month,Portfolio_Value_USD,Tech_Index_Points
2026-01,10000,3100
2026-02,10250,3150
2026-03,10100,3080
```

```text
Explanation: 
    1) The file ./data/report1.csv on the host is bound to the path /app/data/report1.csv in the container.
    2) The final command that runs in the container is python3 -m main /app/data/report1.csv
```

---

## Case 2. Dockerfile_cmd

```bash
docker build -t task5_image -f Dockerfile_cmd .
```

**Run the script in the container. No parameters are passed in.**

```bash
docker run -it --rm --name task5_c task5_image

No file names were passed.
```

**Run the script in the container with file that doesn't exist in the container.**

```bash
docker run -it --rm --name task5_c task5_image ./data/report1.csv

docker: 
    Error response from daemon: failed to create task for container: ...
    exec: "./data/report1.csv": stat ./data/report1.csv: no such file or directory
```

```text
Explanation: 
    The parameter ./data/report1.csv is treated as a command for two reasons:
        - The image has no ENTRYPOINT.
        - The CMD instruction is overridden by the passed argument.
    The error indicates that ./data/report1.csv does not exist inside the container.
```

**Run the script in the container with file that exists on the host.**

```bash
docker run -it --rm --name task5_c -v ./data/report1.csv:/app/data/report1.csv task5_image ./data/report1.csv

exec ./data/report1.csv: exec format error
```

```text
Explanation: 
    The -v flag mounts ./data/report1.csv inside the container. 
    However, the error still occurs because Docker treats ./data/report1.csv as an executable command
    for these reasons:
        - The image has no ENTRYPOINT.
        - The CMD instruction is overridden by the passed argument.
```

**As before, but adding the --entrypoint flag.**

```bash
docker run -it --rm --name task5_c -v ./data/report1.csv:/app/data/report1.csv --entrypoint 'python3' task5_image -m main ./data/report1.csv

File: ./data/report1.csv
Content:
Month,Portfolio_Value_USD,Tech_Index_Points
2026-01,10000,3100
2026-02,10250,3150
2026-03,10100,3080
```

```text
Explanation: 
    The --entrypoint flag sets python3 as the executable, the CMD instruction is overriden.
    The final command that runs in the container is python3 -m main /app/data/report1.csv.
    The /app/data/report1.csv is bound to ./data/report1.csv on the host.
```

**Same as before, but overriding the CMD instruction.**

```bash
docker run -it --rm --name task5_c -v ./data/report1.csv:/app/data/report1.csv task5_image python3 -m main ./data/report1.csv

File: ./data/report1.csv
Content:
Month,Portfolio_Value_USD,Tech_Index_Points
2026-01,10000,3100
2026-02,10250,3150
2026-03,10100,3080
```

```text
Explanation: 
    The CMD instruction is overriden by the input parameters of docker run command.
    The final command that runs in the container is python3 -m main /app/data/report1.csv.
    The /app/data/report1.csv is bound to ./data/report1.csv on the host.
```
