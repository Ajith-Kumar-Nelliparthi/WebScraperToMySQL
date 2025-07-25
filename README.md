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

### Docker Setup
- #### Clone the Repository (if not already done):
    ```bash
    git clone https://github.com/Ajith-Kumar-Nelliparthi/WebScraperToMySQL.git
    cd BookScraper

- #### Set Up Environment Variables:
- Create a .env file:
    ```sh
    DB_HOST=db
    DB_USER=your_username
    DB_PASSWORD=your_password
    DB_NAME=web_scraper_db
    TARGET_URL=http://books.toscrape.com

- #### Build and Run with Docker Compose:
    ```bash
    docker-compose up --build
- This starts the scraper and a MySQL container, automatically creating the products table and scraping data.

- #### Stop the Containers:
    ```bash
    docker-compose down
- To remove the MySQL data volume (reset database):
    ```bash
    docker-compose down -v

### Usage
- #### Run the Scraper:
- Local:
    ```bash
    python scripts/main.py

- Docker:
    ```bash
    docker-compose up

- #### View Logs:
- Check logs/scraper.log for scraping and database activity.
- For Docker, view container logs:
    ```bash
    docker-compose logs scraper

### Database Schema
The scraped data is stored in the products table in the web_scraper_db database:
    ```sql
    CREATE TABLE products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price DECIMAL(10, 2),
        description TEXT
    );

### Contributing
Contributions are welcome! 
- Please follow these steps:Fork the repository.
- Create a feature branch (git checkout -b feature/your-feature).
- Commit changes (git commit -m "Add your feature").
- Push to the branch (git push origin feature/your-feature).
- Open a pull request.
Please ensure code follows PEP 8 style guidelines and includes appropriate logging.













