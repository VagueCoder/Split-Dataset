""" Module to split the dataset into 2 sub datasets: Train & Test """
import os
import sys
import random
import pandas as pd

def export_csv(filename, dataframe):
    """ For Exporting the Dataframe to CSV File """
    dataframe.to_csv(filename, index=False)
    print(f"Exported {filename}\n")

def split_dataset(dataset, filename):
    """ For Splitting the Original Dataset to Training and Testing Datasets """
    count = len(dataset.values)
    test_count = int((0.2 * count) // 1)

    header = dataset.columns.tolist()
    test_dataset = []
    for index in random.sample(range(count), test_count):
        test_dataset.append(dataset.loc[index].tolist())
        dataset.drop(index, axis=0, inplace=True)

    test_dataframe = pd.DataFrame(test_dataset, columns = header)
    train_dataset = dataset.reset_index(drop=True)

    name, extension = os.path.splitext(filename)

    return {f"{name}_Train{extension}":train_dataset,
            f"{name}_Test{extension}":test_dataframe,}

def get_dataset(path):
    """ Function to get data from file. Returns DataFrame """
    dataframe = pd.read_csv(path).fillna(value="UNKNOWN")
    return dataframe

def get_path():
    """ Checks the Command-Line-Arguments or Interacts with User for Fullpath (Path + Filename). Returns Fullpath """
    flag = False
    def inner_check_path(arg):
        path, filename, fullpath = '', '', ''
        try:
            if not os.path.isabs(arg):
                if os.path.isabs(os.path.join(os.getcwd(), arg)):
                    path = str(input("File Name Found. Please enter the path:\t"))
                    fullpath = os.path.join(path, arg)
                else:
                    fullpath = str(input("Can't find the file specified. Enter the Full Path (Path + Filename):\t"))
            else:
                if os.path.isfile(arg):
                    fullpath = str(arg)
                else:
                    filename = str(input("Path Found. Please enter the file name alone:\t"))
                    fullpath = os.path.join(arg, filename)
            if not os.path.isfile(fullpath):
                raise Exception
        except Exception as exception_desc:
            print(f"Exception:\n{exception_desc}")
            return False
        return fullpath
        
    if len(sys.argv) > 1:
        fullpath = inner_check_path(sys.argv[1])
        if fullpath:
            flag = True
    if flag == False:
        while True:
            string = str(input("\nEnter the Full Path (Path + Filename):\t"))
            fullpath = inner_check_path(string)
            if fullpath:
                flag = True
                break
    return fullpath

def main():
    """ Main Function to Collaborate """
    fullpath = get_path()
    path, filename = os.path.split(fullpath)

    dataframe = get_dataset(fullpath)
    datasets = split_dataset(dataframe, filename)
    
    print("This can take a while depending upon the size of your dataset.\n")
    for file in datasets:
        filepath = os.path.join(path, file)
        export_csv(filepath, datasets[file])

if __name__ == "__main__":
    main()