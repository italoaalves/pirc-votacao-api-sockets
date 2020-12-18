import json
import threading


class JsonDB():
    def __init__(self, path):
        self.path = path
        self.lock = threading.Lock()

    def _read_db(self):
        with open(self.path, 'r') as file:
            return json.loads(file.read())

    def _write_db(self, context):
        with self.lock:
            with open(self.path, 'w') as file:
                objects = json.dumps(context)
                file.write(objects)

    def insert(self, data):
        objects = self._read_db()

        objects.append(data)

        self._write_db(objects)

    def find_all(self):
        return self._read_db()

    def find(self, id):
        objects = self._read_db()

        return objects[id]
