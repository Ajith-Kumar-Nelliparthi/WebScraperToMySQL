import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#from src.scraper import Scraper

from src.scraper import Scraper
from src.database import Database
import logging
import time

def main():
    # Initialize logging
    logging.basicConfig(filename='logs/scraper.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    try:
        # Initialize scraper and database
        scraper = Scraper()
        db = Database()
        db.connect()
        db.create_table()

        # Scrape and store data
        products = scraper.scrape()
        for product in products:
            db.insert_product(product)
        
        logging.info("Scraping and storage completed successfully")

    except Exception as err:
        logging.error(f"Error in main: {err}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    main()