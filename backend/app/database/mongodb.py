from pymongo import MongoClient
from dotenv import load_dotenv #cargar las variables de entorno 
import os

load_dotenv()

class MongoDB:
    def __init__(self):
        self.client = None
        self.db = None
        self._mock_db = MockDatabase()  # Base de datos en memoria para pruebas
        
    def connect(self):
        try:
            self.client = MongoClient(os.getenv("MONGODB_URI"), serverSelectionTimeoutMS=5000)
            # Probar conexión
            self.client.admin.command('ping')
            self.db = self.client.chronos_db
            print("✅ Conectado a MongoDB")
            return True
        except Exception as e:
            print(f"❌ Error conectando a MongoDB: {e}")
            print("🔄 Usando base de datos en memoria para pruebas")
            self.db = self._mock_db
            return False
    
    def disconnect(self):
        if self.client:
            self.client.close()
            print("🔌 Desconectado de MongoDB")
    
    def get_database(self):
        return self.db
    
    def get_collection(self, collection_name):
        return self.db[collection_name]

class MockDatabase:
    def __init__(self):
        self._collections = {}
    
    def __getitem__(self, collection_name):
        if collection_name not in self._collections:
            self._collections[collection_name] = MockCollection()
        return self._collections[collection_name]
    
    def __getattr__(self, collection_name):
        if collection_name not in self._collections:
            self._collections[collection_name] = MockCollection()
        return self._collections[collection_name]

class MockCollection:
    def __init__(self, data=None):
        self.data = data if data is not None else []
    
    def find_one(self, query):
        for item in self.data:
            match = True
            for key, value in query.items():
                if key not in item or item[key] != value:
                    match = False
                    break
            if match:
                return item
        return None
    
    def find(self, query=None):
        if query is None:
            return self.data
        results = []
        for item in self.data:
            match = True
            for key, value in query.items():
                if key not in item or item[key] != value:
                    match = False
                    break
            if match:
                results.append(item)
        return results
    
    def insert_one(self, document):
        document['_id'] = str(len(self.data) + 1)
        self.data.append(document)
        return type('obj', (object,), {'inserted_id': document['_id']})
    
    def update_one(self, query, update):
        for i, item in enumerate(self.data):
            match = True
            for key, value in query.items():
                if key not in item or item[key] != value:
                    match = False
                    break
            if match:
                if '$set' in update:
                    for key, value in update['$set'].items():
                        self.data[i][key] = value
                return type('obj', (object,), {'modified_count': 1})
        return type('obj', (object,), {'modified_count': 0})
    
    def delete_one(self, query):
        for i, item in enumerate(self.data):
            match = True
            for key, value in query.items():
                if key not in item or item[key] != value:
                    match = False
                    break
            if match:
                del self.data[i]
                return type('obj', (object,), {'deleted_count': 1})
        return type('obj', (object,), {'deleted_count': 0})

mongodb = MongoDB()
