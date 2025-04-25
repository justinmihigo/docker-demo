# Project 

This project is a Python(Flask) application that can be containerized and run using Docker.

## Prerequisites

Before you can build and run this Docker container, ensure you have the following installed:

- **Docker**: You can download Docker from [here](https://www.docker.com/get-started).
- Your project should include a properly configured `requirements.txt` file with all necessary Python dependencies.

## Building the Docker Image

To build the Docker image for this project, follow these steps:

1. Clone or download the project to your local machine.
2. Open a terminal in the root directory of the project (where the `Dockerfile` is located).
3. Run the following command to build the Docker image:

    ```bash
    docker build -t your-image-name .
    ```

   Replace `your-image-name` with a name you want to assign to the Docker image. This will read the `Dockerfile`, install dependencies listed in `requirements.txt`, and prepare the application to run.

## Running the Docker Container

Once the image is built, you can run the Docker container. To do so:

1. In the same terminal, run the following command:

    ```bash
    docker run -p 5000:5000 your-image-name
    ```

   - `-p 5000:5000` maps port 5000 of your container to port 5000 on your local machine. This is important because the application is set to expose port 5000.
   - Replace `your-image-name` with the name you used when building the image.

2. The application will be running and accessible at `http://localhost:5000` in your browser.

## Dockerfile Explanation

- **FROM python:3.12-slim**: Uses a minimal Python 3.12 image as the base.
- **WORKDIR /app**: Sets the working directory inside the container to `/app`.
- **COPY requirements.txt .**: Copies the `requirements.txt` file into the container.
- **RUN pip install -r requirements.txt**: Installs the Python dependencies listed in `requirements.txt`.
- **COPY . .**: Copies the rest of the application files into the container.
- **EXPOSE 5000**: Exposes port 5000 so the app can be accessed externally.
- **CMD ["python3", "app.py"]**: Runs the Python application using `python3`.

## Notes

- Ensure that `requirements.txt` includes all necessary Python packages to avoid missing dependencies during the build process.
- If you need to run the container in the background, use the `-d` flag with `docker run`:

    ```bash
    docker run -d -p 5000:5000 your-image-name
    ```

This setup will allow you to containerize and run the Python application efficiently using Docker!

