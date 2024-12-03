from flask import Flask
from flask_pymongo import PyMongo
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from routes import register_routes

# Initialize the Flask application
app = Flask(__name__)

# MongoDB connection details
app.config["MONGO_URI"] = "mongodb+srv://bka2bg:QcqSyZpNSyiH52cU@crisismanagement.vypxy.mongodb.net/Crisis_Management"
mongo = PyMongo(app)

# Initialize the transformer pipeline
# Register routes
register_routes(app, mongo)

# Run the Flask app on EC2 and make it accessible to the public IP (0.0.0.0)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
