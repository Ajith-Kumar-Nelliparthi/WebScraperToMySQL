# BookScraper
BookScraper is a Python-based web scraping application that extracts book details (titles, prices, and descriptions) from [books.toscrape.com](https://books.toscrape.com/) and stores them in a MySQL database. The project is containerized using Docker for portability and reproducibility, with a modular design for easy maintenance and scalability.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
    - [Local Setup](#local-setup)
    - [Docker Setup](#docker-setup)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Contributing](#contributing)

## Features
Scrapes book data (title, price, description) from books.toscrape.com.
Stores data in a MySQL database for persistent storage.
Modular code structure with separate modules for scraping, database operations, and configuration.
Dockerized setup for consistent deployment across environments.
Logging for debugging and monitoring.
Environment variable management using .env for secure configuration.
Optional data analysis and export using pandas.

## Project Structure
```
    BookScraper/
    ├── config/
    │   └── config.py           # Configuration and environment variable loading
    ├── src/
    │   ├── scraper.py          # Web scraping logic
    │   ├── database.py         # MySQL connection and queries
    │   └── models.py           # Data models (e.g., Product class)
    ├── logs/
    │   └── scraper.log         # Log file for debugging
    ├── scripts/
    │   ├── main.py             # Entry point to run the scraper
    │   ├── display_data.py     # Script to view scraped data
    │   └── analyze_data.py     # Script for data analysis with pandas
    ├── .env                    # Environment variables (not committed)
    ├── Dockerfile              # Docker configuration
    ├── docker-compose.yml      # Docker Compose for scraper and MySQL
    ├── requirements.txt        # Python dependencies
    ├── README.md               # Project documentation
    └── .gitignore              # Git ignore file
```
## Prerequisites
- Python: 3.12 or higher
- MySQL: 8.0 or higher (if not using Docker)
- Docker: Docker and Docker Compose (for containerized setup)
- Git: For cloning the repository
- pip: For installing Python dependencies

## Setup Instructions

### Local Setup
- #### Clone the Repository:
    ```bash
    git clone https://github.com/Ajith-Kumar-Nelliparthi/WebScraperToMySQL.git
    cd BookScraper
- #### Set Up a Virtual Environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

- #### Install Dependencies:
    ```bash
    pip install -r requirements.txt

- #### Configure MySQL:
- Ensure a MySQL server is running locally or remotely.
- Create a database:
    ```sql
    CREATE DATABASE web_scraper_db;
- Grant permissions to your MySQL user:
    ```sql
    GRANT ALL PRIVILEGES ON web_scraper_db.* TO 'your_username'@'localhost' IDENTIFIED BY 'your_password';
- ##### Set Up Environment Variables:
- Create a .env file in the project root:
    ```sh
    DB_HOST=localhost
    DB_USER=your_username
    DB_PASSWORD=your_password
    DB_NAME=web_scraper_db
    TARGET_URL=http://books.toscrape.com








