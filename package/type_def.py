class parameter:
    def __init__(self, entries="NULL"):
        if entries!="NULL":
            try:
                parameter.threshold    = float(entries[0].get())
                parameter.filterRadius = int(entries[1].get())
                parameter.crop         = int(entries[2].get())
                parameter.resize       = int(entries[3].get())
                parameter.openDir      = str(entries[4].get())
                parameter.fileType     = str(entries[5].get())
                parameter.saveDir      = str(entries[6].get())
            except ValueError:
                print("Invalid input parameter!!!")
        else:
            parameter.threshold = 0.2  # Sun detection threshold
            parameter.filterRadius = 5  # Remove small objects fewer pixel than P
            parameter.crop = 2500  # Crop size
            parameter.resize = 500  # Resize to
            parameter.openDir = './input'  # Image folder
            parameter.fileType = '*.JPG'  # Image file type, supports jpg/bmp/png/tif
            parameter.saveDir = './output/'  # Save folder

fields = ('threshold', 'filterRadius', 'crop', 'resize', 'input directory', 'fileType', 'output directory')
default_val = ('0.2', '5', '2500', '500', './small_input', 'JPG', './output/')