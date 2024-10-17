class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension
        
    def resize(self, res):
        self.resolution = res
        

image_test_1 = Image('1920x1080', 'Test', '.HEIC')
image_test_1.resize('900x700')
print(image_test_1.resolution)

image_test_2 = Image('1920x1080', 'Test', '.HEIC')
image_test_2.resize('680x700')
print(image_test_2.resolution)

image_test_3 = Image('1920x1080', 'Test', '.HEIC')
image_test_3.resize('480x200')
print(image_test_3.resolution)