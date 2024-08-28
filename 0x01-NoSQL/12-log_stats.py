#!/usr/bin/env python3
'''Task 12's module.
'''
from pymongo import MongoClient

def print_nginx_request_logs(nginx_collection):
    '''Prints stats about Nginx request logs.'''
    # Count the total number of documents
    log_count = nginx_collection.count_documents({})
    print(f"{log_count} logs")

    # Methods count
    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        count = nginx_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")

    # GET requests to /status
    status_check_count = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status_check_count} status check")

def run():
    '''Provides some stats about Nginx logs stored in MongoDB.'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print_nginx_request_logs(nginx_collection)

if __name__ == '__main__':
    run()
