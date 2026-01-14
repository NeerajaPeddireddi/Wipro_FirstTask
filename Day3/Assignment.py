def write_num_file(filename):
    try:
        with open(filename,"w") as file:
            for i in range(1,101):
                file.write(str(i)+"\n")
        print("File written")
    except FileNotFoundError:
        print("File not exist")
    except PermissionError:
        print("Permission denied")
    except Exception as e:
        print(e)
write_num_file("Assignment_File.txt")