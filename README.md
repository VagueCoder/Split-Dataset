# Split-Dataset
For the purpose of Machine Learning, the dataset needs to be split into Train &amp; Test data (manually at times). The repository has a small code snippet (in both Python &amp; Golang) that splits it automatically in the ratio 80% to 20%.

### Usage :+1:
#### In Python
```
python split_dataset.py "Full/Path/To/CSV-File/Here"
```

#### In Go
```
go run split_dataset.go "Full/Path/To/CSV-File/Here"
```

### Suggestion & Warning :warning:
The approach was focused on **Ease-of-development** to **Speed of Execution**. Hence the program was created in Python using DataFrame where the dataset can be considered as plain text, and so the execution is too `slow` (above 30 mins for the dataset in this repo).

However, in Golang, the execution is `superfast` (about 5 seconds for the dataset in this repo) and also the build can directly be used instead of running the the go file manually. Following is the Syntax,
```
split_dataset.exe "Full/Path/To/CSV-File/Here"
```

## Happy Coding! :metal: :metal:
