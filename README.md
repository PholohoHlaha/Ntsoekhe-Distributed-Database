# Ntsoekhe Distributed Database project Phase II.

# The basic Aim of Ntsoere is to Implement a Scalable and fault-tolerant Distributed Database System: Healthcare systems generate massive amounts of data, including patient records, diagnostic reports, medical images, and sensor data from different levels of hospitality, being the primary stage(Clinics), secondary stage(Medium hospitals) and Tertiary stage(Large technological hospitals)-Tsepong and Queen II in cases of Lesotho.


# Written using Django and little of html and bootstrap to render the front page forms, and Postgesql instances as database management Systems. Docker is used to containerize this platform, but mainly, Docker is used to host multiple databases that are used within the platform. The databases run on different ports. From port 5431 to port 5434, as specified by the docker-compose.yml file.

# There are 5 different databases used within this platform.
#       1. Primary_Health_Center Database
#       2. Hospital_Health_Center Databae
#       3. Tertiary_Health_Center Database
#       4. Patient_Records Database

# All the databases allow CRUD(create, Read, Update and Delete). We have allowed db_router.py, our essential router file that allows the operations on the databases from the front end to allow all its operations to be done that is: 'db_for_read', 'db_for_write', 'allow_relation', 'allow_migrate'.

# In our Django application, there are four application that map to our databases using a one to one relation, that is, every application-(hospital_center, Northern records, Tertiary_center) within the umbrella of our platform(distributedddms). There is transparency.

# Project Setup Guide

This guide provides step-by-step instructions for setting up your development environment for a Django project using Docker, Python, PostgreSQL, and pgAdmin.

## Prerequisites

- Docker: Ensure Docker is installed on your system. Visit [Docker's official website](https://www.docker.com/) for installation instructions.
- Python: Install Python on your system. Visit [Python's official website](https://www.python.org/) for installation instructions.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/PholohoHlaha/Ntsoekhe-Distributed-Database.git
    ```

2. Navigate to the project directory:

    ```bash
    cd distributeddms
    ```

3. Set up the Docker environment:

    ```bash
    docker-compose up -d
    ```

4. Install Django and other dependencies using pip:

    ```bash

    pip install -r requirements.txt
    ```

5. Apply migrations to set up the database:

    ```bash
    python3 manage.py migrate
    python3 manage.py migrate --database=Primary_Health_CenterDB
    ```

    ```bash
    python3 manage.py migrate
    python3 manage.py migrate --database=Hospital_CenterDB
    ```

    ```bash
    python3 manage.py migrate
    python3 manage.py migrate --database=Hospital_CenterDBTertiary_CenterDB
    ```
    ```bash
    python3 manage.py migrate
    python3 manage.py migrate --database=Northern_PatientsRecordDB
    ```


6. Create a superuser for accessing the Django admin interface:

    ```bash
    python3 manage.py createsuperuser
    ```

7. Access the Django development server:

    Visit `http://localhost:8000` in your web browser.

8. Access pgAdmin:

    - URL: `http://localhost:5050`
    - Username: `admin@example.com`
    - Password: `admin`

9. Access SQlite3 for users of the application:
   Hosted locally
    - For manual installation on Windows: Download and install DB Browser for SQLite from https://sqlitebrowser.org/dl/
    - For manual installation on macOS: Download and install DB Browser for SQLite from https://sqlitebrowser.org/dl/
    - For manual installation on Linux: Install DB Browser for SQLite using your package manager or download it from https://   sqlitebrowser.org/dl/
    
## Additional Notes

- Modify the settings in `docker-compose.yml` and `settings.py` as per requirements.
- Ensure Docker Desktop is running before executing Docker commands.
- For more information on Docker commands and usage, refer to the [Docker documentation](https://docs.docker.com/).






