# Name: Joseph Tastet
# Date: 4/6/2023
# Module 4 milestone

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:48357/AAC' % (username, password))
        # where xxxx is your unique port number
        self.database = self.client['AAC']
        print("Connection Successful")

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            insert_result = self.database.animals.insert(data)  # data should be dictionary    
            if insert_result != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    #Read method to implement the R in CRUD
    def read(self, query=None):
        if query is not None:
            #Equivalent to Mongo find({query}) command
            data = self.database.animals.find(query,{"_id": False})
            
                
        else:
            data = self.database.animals.find({},{"_id": False})
            
        return data
    
    #Update method to implement the U in CRUD
    def update(self, query, change, count):
        if query is not None:
            #use count to determine if using one or many
            if count == 1:
                try: 
                    #Mongodb equivalent of updateOne({query}, {$set: {change}})
                    update_result = self.database.animals.update_one(query, change)
                    if update_result.modified_count == 1:
                        print("The update was successful")
                        print(update_result)
                        return True
                    else:
                        print("Something went wrong")
                        return False
                except Exception as e:
                    print("Error message: ", e)
                    return False
            elif count <= 2:
                try:
                    #Mongodb equivalent of update({query}, {$set: {change}})
                    update_result = self.database.animals.update_many(query, change)
                    if update_result.modified_count == update_result.matched_count:
                        print("The update was successful")
                        print(update_result)
                        return True
                    else:
                        print("Something went wrong")
                        return False
                except Exception as e:
                    print("Error message: ", e)
                    return False
            else:
                print("Invalid count")
                return False
        else:
            raise Exception("Query is empty")
            return False
        
    #Delete method implementing the D in CRUD
    def delete(self, query, count):
        if query is not None:
            #use count to determine one or many
            if count == 1:
                try:
                    #Mongodb equivalent of deleteOne({query})
                    delete_result = self.database.animals.delete_one(query)
                    if delete_result.deleted_count == 1:
                        print("The delete was successful")
                        print(delete_result)
                        return True
                    else:
                        print("Something went wrong")
                        return False
                except Exception as e:
                    print("Error message: ", e)
                    return False
            elif count <= 2:
                try:
                    #Mongodb equivalent of delete({query})
                    delete_result = self.database.animals.delete_many(query)
                    if delete_result.deleted_count > 0:
                        print("The delete was successful")
                        print(delete_result)
                        return True
                    else:
                        print("Something went wrong")
                        return False
                except Exception as e:
                    print("Error message: ", e)
                    return False
            else:
                print("Invalid count")
                return False
        else:
            raise Exception("Query is empty")
            return False