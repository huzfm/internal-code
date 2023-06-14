class Papa():
    def show(self):
        print('parent')
class Beta(Papa):
    def show(self):
        super().show()
        print("Son")
obj=Beta()
obj.show()        