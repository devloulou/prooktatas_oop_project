# fel kell olvasni az mkv file-okat a mappából / mappákból
# kiírni a szöveges metaadatot
# ki kell írni a képeket - itt oldjuk meg, vagy a lekérés osztályánál
# törölni a képeket
# törölni a metaadatot
import os
import json


class FileHandler:
    folder_path = r"C:\WORK\Prooktatás\oop_project\movies"
    #def __init__(self, folder_path: str):
    def __init__(self):
        pass
        #self.folder_path = folder_path

    def delete_file(self, file_path):
        try:
            os.remove(file_path)
        except FileNotFoundError:        
            return False, 'File nem található!'
        except Exception as e:
            return False, str(e)

        return True

    def write_file(self, file_path, data):
        if data:
            # a data-t át tudjuk e alakítani json-é           
            try: 
                json.dumps(dict(data))
            except TypeError:
                return False, 'Nem jó adattípust adtál meg.'
            except Exception as e:
                return False, str(e)

            if isinstance(file_path, str):        
                with open(file_path, 'w', encoding='utf-8') as json_file:
                    json.dump(data, json_file)
            else:
                return False, 'Nem string'
        else:
            return False, 'Nem adtál meg adatokat a kiíráshoz'

        return True

    def get_list(self):
        if not os.path.exists(self.folder_path):
            return False, "The given path is not exists"
        
        return [file for file in os.listdir(self.folder_path) if file[-3:] in ('mkv')]



class FileHandler2(FileHandler):
    def __init__(self):
        super().__init__()

    def write_file(self, file_path, data):
        with open(file_path, 'w') as file:
            file.write(data)
        return True

    @classmethod
    def first_cls(cls):
        return cls()

    @staticmethod
    def first_static(number):
        return number ** 2



if __name__ == '__main__':
    folder_path = r"C:\WORK\Prooktatás\oop_project\movies"
    # handler = FileHandler()

    # print(handler.get_list())

    # handler.write_file("test.json", {"kulcs": "érték"})
    # handler.delete_file("test.json")

    handler_2 = FileHandler2()
    print(handler_2.get_list())

    handler_2.write_file("test.txt", "Nagyon jó ez az oop")

    print(FileHandler2().first_cls())

    print(FileHandler2().first_static(5))