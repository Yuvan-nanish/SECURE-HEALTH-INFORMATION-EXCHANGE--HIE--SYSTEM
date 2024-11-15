from app.input_form import get_ehr_data
from app.encrypt_and_store import encrypt_and_store_ehr
from db.database import init_db

def main():
    # Initialize MongoDB connection
    db, collection = init_db()
    
    if collection is not None:  # Check if collection is not None
        # Get EHR data (simulate form input)
        ehr_data = get_ehr_data()

        # Encrypt and store EHR data in MongoDB
        encrypt_and_store_ehr(ehr_data, collection)
    else:
        print("Failed to connect to the collection.")

if __name__ == "__main__":
    main()
