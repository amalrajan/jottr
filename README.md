<h1 align="center">Jottr</h1>

<p align="center">
  Jottr is a super simple and user-friendly API for building note-taking applications.
</p>

## Table of Contents

- [Flow Diagram](#flow-diagram)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)


## Flow Diagram
![Flow Diagram](https://ik.imagekit.io/5jrct2yttdr/jottr_DugS-ZkBe.png?updatedAt=1691181293179)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/amalrajan/jottr.git
   cd jottr
   ```

2. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```


## Usage

1. Running the Server: 

    Before using the API, you need to run the server locally. In the terminal, navigate to the project directory and execute the following command:

    ```bash
    python app.py
    ```
    The server will start running on http://localhost:5000.

2. Authentication

    Jottr uses JWT (JSON Web Token) authentication to secure the API endpoints. To access protected routes (e.g., creating, updating, or deleting notes), you need to include a valid JWT token in the request header.

    To obtain a JWT token, first, sign up for an account by making a POST request to /api/register with your choice of username and password. You will receive a response with a success message.

    Next, log in to your account by making a POST request to /api/login with your credentials. The response will include a JWT token. Copy this token for future requests.

3. Database

    First, open a terminal or command prompt and run the following command to pull the official PostgreSQL Docker image from Docker Hub:

    ```bash
    docker pull postgres:latest
    ```

    It is a good practice to create a dedicated Docker network for your PostgreSQL container. This allows you to easily connect other containers to the database without exposing it directly to the host machine.

    ```bash
    docker network create my_postgres_network
    ```

    Now, start a new PostgreSQL container using the docker run command. Make sure to set the required environment variables and mount a volume to persist the database data.


    ```bash
    docker run -d \
        --name my_postgres \
        --network my_postgres_network \
        -e POSTGRES_PASSWORD=mysecretpassword \
        -e POSTGRES_USER=myuser \
        -e POSTGRES_DB=mydatabase \
        -v /path/on/host:/var/lib/postgresql/data \
        -p 5432:5432 \
        postgres:latest
    ```


## API Endpoints

1. User Registration

    **Endpoint:** `POST /api/register`

    Allows users to create an account by providing a unique username and password.

    **Request:**
    ```json
    {
        "username": "user123",
        "password": "secretpassword"
    }
    ```

2. Notes creation
    
    **Endpoint:** `POST /api/notes`

    Allows users to create a new note by providing a title and content.

    **Request:**
    ```json
    {
        "title": "My first note",
        "content": "This is the content of my first note."
    }
    ```

    **Authorization**
    Bearer your.jwt.token

And other endpoints...


## License
The MIT License