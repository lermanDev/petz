## About Poetry

This project is powered by [Poetry](https://python-poetry.org/), a modern Python dependency management and packaging tool that simplifies the management of project dependencies and enhances the development workflow.

[Poetry](https://python-poetry.org/) is designed to make managing Python projects and their dependencies more straightforward and efficient. It provides a user-friendly and intuitive way to specify and install dependencies, create virtual environments, and ensure reproducible builds.

Poetry is particularly well-suited for Python projects of all sizes, making it easier to keep your project organized and maintainable.

## Dependency Management

With Poetry, managing dependencies for this project is a breeze. The `pyproject.toml` file contains a clear and concise list of project dependencies along with their versions.

Poetry automatically creates a virtual environment and installs these dependencies when you run:

    poetry install

## Adding Dependencies

Adding new dependencies to your project is as simple as running the poetry add command, which updates the pyproject.toml file and lock file for you. For example:

    poetry add package-name

Poetry will automatically handle version resolution and package installation.

## Running Your Django Application
To run your Django application, you can use Poetry's poetry run command. For instance, to start the development server, use the following command:

    poetry run python manage.py runserver

Poetry ensures that your application runs within the correct virtual environment with all the required dependencies.

## Running Tests

Running tests for your Django application is straightforward with Poetry. You can execute tests using the poetry run command as well:

    poetry run pytest

This command runs your unit tests, helping you maintain code quality and reliability throughout your development process.

## Conclusion

Poetry is a powerful tool that enhances the development experience by simplifying dependency management, ensuring package compatibility, and providing a smooth workflow for Python projects like this one.
