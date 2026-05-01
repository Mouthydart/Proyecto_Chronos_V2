from pymongo import MongoClient
from dotenv import load_dotenv #cargar las variables de entorno 
import os

load_dotenv()

class MongoDB:
    def __init__(self):
        self.client = None
        self.db = None
        
    def connect(self):
        try:
            self.client = MongoClient(os.getenv("MONGODB_URI"))
            self.db = self.client.chronos_db
            print("✅ Conectado a MongoDB")
            return True
        except Exception as e:
            print(f"❌ Error conectando a MongoDB: {e}")
            return False
    
    def disconnect(self):
        if self.client:
            self.client.close()
            print("🔌 Desconectado de MongoDB")
    
    def get_database(self):
        return self.db
    
    def get_collection(self, collection_name):
        return self.db[collection_name]

mongodb = MongoDB()
