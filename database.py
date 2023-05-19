import json

class DataBase:
    def load(self, filename):
        with open(filename, 'r') as f:
            return json.load(f)

    def save(self,obct, filename):
        with open(filename, 'w') as f:
            json.dump(obct,f, indent=4)

