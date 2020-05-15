import shelve
import uuid


class Person:
    def __init__(self):
        self.data = shelve.open('mydata.dat')
    def create_data(self,nama_file=None,byte_data=None):
        if (nama_file is None):
            return False

        """File disimpan di server"""
        FileTerima = open('server/'+nama_file, 'wb+')
        FileTerima.write(byte_data)
        FileTerima.close()
        """======================"""

        """File disimpan di database"""
        id=str(uuid.uuid4())
        data = dict(id=id,nama_file=nama_file,byte_data=byte_data)
        self.data[id]=data
        """========================="""    
        return True
        
    def get_data(self,nama=None):
        print('ini p1')
        for i in self.data.keys():
            if (self.data[i]['nama_file'].lower() == nama.lower()):
                return self.data[i]
        return False

    def list_data(self):
        k = [dict(nama_file=self.data[i]['nama_file']) for i in self.data.keys()]
        return k

if __name__=='__main__':
    p = Person()
    # p.create_data("vanBasten","621234")
    # p.create_data("vanPersie","621235")
    # p.create_data("vanNistelroy","621236")
    # p.create_data("vanDerVaart","621237")
    # print(p.list_data())
    # print(p.get_data('vanbasten'))
