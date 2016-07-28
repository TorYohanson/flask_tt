import json
import pymongo
import app.settings as settings
import urllib.request

from pymongo import MongoClient
from bson.json_util import dumps


class Catalog():
    def __init__(self, **kwargs):
        db_location = settings.MONGO_LOCATION
        db_user = settings.MONGO_USER
        db_pass = settings.MONGO_PASS
        db_port = settings.MONGO_PORT
        db_name = settings.MONGO_DB
        db_collection = settings.MONGO_COLLECTION
        'mongodb://<dbuser>:<dbpassword>@ds029665.mlab.com:29665/t_task_cities'
        db_connection = 'mongodb://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_location, db_port, db_name)
        client = MongoClient(db_connection)
        d_base = client[db_name]

        self.collection = d_base[db_collection]
        self.dump_url = kwargs.get('filename', 'http://media.mongodb.org/zips.json')

    def load_collection(self):
        self.collection.drop()
        with urllib.request.urlopen(self.dump_url) as response:
            raw_dump = '[' + '}, '.join(response.read().decode('utf-8').split('}')).strip()[:-1] + ']'
            dump = json.loads(raw_dump)
        result = self.collection.insert_many(dump)
        print("{} records inserted into '{}' collection.".format(len(result.inserted_ids), self.collection.name))

    def get_most_populated(self, city_limit=20):
        city_list = self.collection.find(projection={'_id': False, 'loc': False}, limit=city_limit).sort([
            ('pop', pymongo.DESCENDING)])
        result = dumps([c for c in city_list], ensure_ascii=False)
        return result


def main():
    cat = Catalog()
    cat.load_collection()
    a = cat.get_most_populated()
    c = {'key': 'Cities by population', "color": "#4f99b4"}
    c['values'] = [{'label': '{} ({})'.format(row['city'].capitalize(), row['state']), 'value': row['pop']}
                   for row in json.loads(a)]
    c = json.dumps(c)
    print(c)

if __name__ == '__main__':
    main()
