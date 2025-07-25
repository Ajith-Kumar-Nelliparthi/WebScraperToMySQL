# BookScraper
BookScraper is a Python-based web scraping application that extracts book details (titles, prices, and descriptions) from [books.toscrape.com](https://books.toscrape.com/) and stores them in a MySQL database. The project is containerized using Docker for portability and reproducibility, with a modular design for easy maintenance and scalability.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup Instructions] (#setup-instructions)
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