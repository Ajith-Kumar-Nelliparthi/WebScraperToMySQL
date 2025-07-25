# BookScraper
BookScraper is a Python-based web scraping application that extracts book details (titles, prices, and descriptions) from [books.toscrape.com](https://books.toscrape.com/) and stores them in a MySQL database. The project is containerized using Docker for portability and reproducibility, with a modular design for easy maintenance and scalability.

## Table of Contents
- [Features](features)
- Project Structure (#project-structure)
- Prerequisites (#prerequisites)
- Setup Instructions (#setup-instructions)
    - Local Setup (#local-setup)
    - Docker Setup (#docker-setup)
- Usage (#usage)
- Database Schema (#database-schema)
- Viewing Scraped Data (#viewing-scraped-data)
- Contributing (#contributing)

### Features
Scrapes book data (title, price, description) from books.toscrape.com.
Stores data in a MySQL database for persistent storage.
Modular code structure with separate modules for scraping, database operations, and configuration.
Dockerized setup for consistent deployment across environments.
Logging for debugging and monitoring.
Environment variable management using .env for secure configuration.
Optional data analysis and export using pandas.

Project Structure

