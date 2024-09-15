Document Retrieval System


Overview:

The Document Retrieval System is a backend application designed for efficiently retrieving documents to provide context for Large Language Models (LLMs). The system supports storing documents in a database, retrieving relevant results based on text queries, caching responses for improved performance, and rate-limiting to prevent abuse. Additionally, the system performs background scraping of news articles upon startup.

Features

Document Retrieval: Accepts text prompts and returns the top K results based on similarity scores.

Caching: Responses are cached for faster retrieval and optimized system performance.

Background Scraping: Scrapes news articles when the server starts in a separate thread.

Rate Limiting: Limits users to 5 API requests, after which they receive an HTTP 429 response.

API Logging: Logs inference times for each request.

Dockerized: The entire application is containerized using Docker for easy deployment.

Re-ranking and Fine-tuning (Bonus): The system includes re-ranking algorithms to enhance the accuracy of search results.


Installation:

Prerequisites:

Python 3.7+

Docker (for containerization)

Redis (for caching)

Sentence-Transformers


Caching Strategy:

The application uses Redis for caching to ensure fast retrieval of frequently requested results. 

This approach was chosen for its performance and scalability, making it suitable for handling concurrent API calls.

The reasoning behind selecting Redis for caching is explained in detail in the README.md, along with configuration details. Refer to the Caching section in the documentation for more insights.

Rate Limiting:

Each user is identified by a user_id, and the system restricts each user to a maximum of 5 requests. 

Once a user exceeds this limit, they will receive an HTTP 429 (Too Many Requests) response.

Logging and Monitoring:

The application logs all incoming requests, including:

Request URL

Response Time

Status Codes

Inference Time

These logs are essential for monitoring and debugging.


Background Scraping:

Upon startup, a separate thread starts scraping the latest news articles from various sources and stores them in the database.

This ensures that fresh and relevant content is available for document retrieval.


Technologies Used:

Flask: Web framework for building the backend API.

Redis: In-memory data structure store, used for caching.

Sentence-Transformers: For encoding and querying document embeddings.

Docker: Containerization for easier deployment.

Waitress: Production-ready WSGI server for serving the Flask app.

Project Structure


Document Retrieval System/
│
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
├── .gitignore           # Files to ignore in Git
├── README.md            # Project documentation
└── utils/               # Utility functions
    ├── cache.py         # Caching-related functions
    ├── db.py            # Database operations
    └── scrapers.py      # Web scraping logic



Contact(For only Trademarkia Recruiters):
For any inquiries, please reach out to Mallampati Bhavishya at mallampatibhavishyachowdary@gmail.com.

