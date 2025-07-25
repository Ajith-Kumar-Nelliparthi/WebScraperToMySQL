import mysql.connector
from config.config import Config
import logging

# set up logging
logging.basicConfig(filename='logs/scraper.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Database:
    """Database connection class."""
    def __init__(self):
        self.config = Config.DB_CONFIG
        self.connection = None
        self.cursor = None
    
    def connect(self):
        """Connect to the MySQL database."""
        try:
            self.connection = mysql.connector.connect(**self.config)
            self.cursor = self.connection.cursor()
            logging.info("Database connection established.")
        except mysql.connector.Error as err:
            logging.error(f"Error connecting to database: {err}")
            raise
    
    def create_table(self):
        """Create the products table if it does not exist."""
        try:
            query = """
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                price DECIMAL(10, 2),
                description TEXT
            )
            """
            self.cursor.execute(query)
            self.connection.commit()
            logging.info("Products table created or already exists.")
        except mysql.connector.Error as err:
            logging.error(f"Error creating table: {err}")
            raise

    def insert_product(self, product):
        """Insert a product into the database."""
        try:
            query = """
            INSERT INTO products (name, price, description)
            VALUES (%s, %s, %s)
            """
            values = (product.name, product.price, product.description)
            self.cursor.execute(query, values)
            self.connection.commit()
            logging.info(f"Inserted product: {product.name}")
        except mysql.connector.Error as err:
            logging.error(f"Failed to insert product: {err}")
            raise

    def close(self):
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            logging.info("Database connection closed.") 