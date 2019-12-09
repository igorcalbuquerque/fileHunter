import os

print('Put the file place: (Example: C:\)')
searchFile = input()
print('Put the name or a part of name (or extension) of the file:')
searchBy = input()

def sizeFormat(size):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if size < kilo:
        text = 'b'
    elif size < mega:
        size /= kilo
        text = 'Kb'
    elif size < giga:
        size /= mega
        text = 'Mb'
    elif size < tera:
        size /= giga
        text = 'Gb'
    elif size < peta:
        size /= tera
        text = 'Tb'
    else:
        size /= peta
        text = 'P'
    size = round(size, 2)
    return f'{size}{text}'

for root, directories, files in os.walk(searchFile):
    for file in files:
        if searchBy in file:
            try:
                complete_way = os.path.join(root, file)
                archive_name, archive_ext = os.path.splitext(file)
                archive_size = os.path.getsize(complete_way)

                print()
                print('Archive Found!')
                print('Archive: ', file)
                print('Place: ', complete_way)
                print('Ext: ', archive_ext)
                print('Archive size: ', sizeFormat(archive_size))
            except PermissionError as e:
                print('Permission Denied!!!')
            except FileNotFoundError as e:
                print("File Not Found")
            except Exception as e:
                print("ERROR!", e)
