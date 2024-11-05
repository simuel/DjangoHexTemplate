# DjangoHexTemplate

**DjangoHexTemplate** is a robust and scalable template for building Django applications using **Hexagonal Architecture** or **Clean Architecture** principles. This project structure encourages a separation of concerns, keeping your business logic independent from the framework and infrastructure details, thus promoting maintainability, testability, and the ability to adapt to change over time.

## Features

**Domain-Driven Design:** Clear separation of business logic from infrastructure.
Hexagonal/Clean Architecture: Organized into domain, application, infrastructure, and presentation layers.

**Testability:** Easy to write unit and integration tests for each layer.

**Extensibility:** Can be easily extended to fit various use cases and business requirements.

**Django REST Framework Integration:** Preconfigured serializers for API development.


## Project Structure
Here's a breakdown of the project's main directories and their purpose:

``` DjangoHexTemplate/
|-- app_name/                   # Main directory for the application
|   |-- domain/                 # Core business logic and entities
|   |-- application/            # Use cases and application logic
|   |-- infrastructure/         # Infrastructure details (DB, serializers)
|   |-- presentation/           # User interface and API endpoints
|   |-- tests/                  # Unit and integration tests
|-- manage.py                   # Django's management script
|-- requirements.txt            # Project dependencies
|-- README.md                   # Project documentation
```

How to Set Up and Migrate the Application
Follow these steps to get your application running:

## Prerequisites
Django 4.0+: The project is built on Django 4.0 or later.

