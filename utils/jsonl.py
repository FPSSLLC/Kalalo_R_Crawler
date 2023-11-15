from dotenv import load_dotenv
import os
import psycopg2
import time
import json

class Output:
    def __init__(self, config):
        self.indent=False
        self.file_path = f"{config['dirname']}/output/{config['domain']}_{int(time.time())}.jsonl"
        self.file = open(self.file_path, 'w')

    def write_listing(self, data):
        for url in data:
            if self.indent:
                json.dump({"url":url}, self.file,indent=4)
            else:
                json.dump({"url":url}, self.file)
            self.file.write('\n')

    def write_products(self, data):
        if "product_url" in data:
            if self.indent:
                json.dump(data, self.file,indent=4)
            else:
                json.dump(data, self.file)
            self.file.write('\n')

    def close(self):
        self.file.close()
