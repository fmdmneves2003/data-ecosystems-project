from pymongo import MongoClient

# 1. Connect to your MongoDB (adjust connection string if needed)
client = MongoClient("mongodb://localhost:27017/")
db = client["novacred_db"]

# 2. Define your automated Governance Validation Schema
governance_rules = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["_id", "applicant_info", "financials", "spending_behavior", "decision"],
        "properties": {
            "_id": {
                "bsonType": "string",
                "description": "Application ID must be a string"
            },
            "applicant_info": {
                "bsonType": "object",
                "required": ["full_name", "email", "ssn", "ip_address", "date_of_birth"],
                "properties": {
                    "full_name": {"bsonType": "string"},
                    "email": {
                        "bsonType": "string",
                        "pattern": "^.+@.+\\..+$", 
                        "description": "Must be a valid email format"
                    },
                    "ssn": {
                        "bsonType": "string",
                        "description": "SSN must be a string for strict PII tracking"
                    },
                    "ip_address": {"bsonType": "string"},
                    "date_of_birth": {"bsonType": "string"},
                    "gender": {"bsonType": "string"},
                    "zip_code": {"bsonType": "string"}
                }
            },
            # Acknowledging the rest of the dataset structure to allow insertion
            "financials": {"bsonType": "object"},
            "spending_behavior": {"bsonType": "array"},
            "decision": {"bsonType": "object"}
        }
    }
}

# 3. Apply the rules to the collection
try:
    db.create_collection("credit_applications", validator=governance_rules)
    print("Governance Gatekeeper activated: Collection created with strict PII validation.")
except Exception as e:
    db.command("collMod", "credit_applications", validator=governance_rules)
    print("Governance Gatekeeper updated: Validation rules applied to existing collection.")