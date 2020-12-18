import json


class JsonDB():
    def __init__(self, path):
        self.path = path

        with open(self.path, 'w') as file:
            file.write("[]")

    def _read_db(self):
        with open(self.path, 'r') as file:
            return json.loads(file)

    def _write_db(self, context):
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

    def update(self, id, data):
        objects = self._read_db()


    def delete(self, id):
        pass
