package main

import (
	"fmt"
	"encoding/csv"
	"log"
	"os"
	"math/rand"
	"time"
	"path/filepath"
	"strings"
)

func main()  {
	fullpath := os.Args[1]
	path, filename := filepath.Split(fullpath)
	
	rows := read_csv(filename)
	test_count := len(rows) / 5

	random_nums := random_numbers(1, len(rows), test_count)

	test, train := split_dataset(rows, random_nums)

	extension := filepath.Ext(filename)
	just_filename := strings.Replace(filename, extension, "", -1)
	train_filename := just_filename + "_Train" + extension
	test_filename := just_filename + "_Test" + extension
	train_filepath := filepath.Join(path, train_filename)
	test_filepath := filepath.Join(path, test_filename)
	
	write_csv(train, train_filepath)
	fmt.Printf("\nTraining Dataset:\t%s", train_filepath)
	write_csv(test,test_filepath)
	fmt.Printf("\nTesting Dataset:\t%s", test_filepath)

}

func random_numbers(min, max, count int) []int {
	arr := make([]int, max-min)
	for i:=min; i<max; i++{
		arr[i-min] = i
	}
	rand.Seed(time.Now().UnixNano())
	rand.Shuffle(len(arr), func(i, j int) {arr[i], arr[j] = arr[j], arr[i]})
	return arr[0:count]
}

func read_csv(filename string) [][]string {
	f, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}

	rows, err := csv.NewReader(f).ReadAll()
	f.Close()
	if err != nil {
		log.Fatal(err)
	}

	return rows

}

func write_csv(rows [][]string, filename string) {
	csvFile, err := os.Create(filename)
	if err != nil {
		log.Fatal(err)
	}

	csvWriter := csv.NewWriter(csvFile)

	for _, row := range rows {
		_ = csvWriter.Write(row)
	}

	csvWriter.Flush()
	csvFile.Close()
}

func split_dataset(dataset [][]string, selective_row_nums []int) ([][]string, [][]string) {
	in_dataset := make([][]string, len(selective_row_nums) +1)
	out_dataset := make([][]string, len(dataset) - len(selective_row_nums))

	in_dataset[0] = dataset[0]
	out_dataset[0] = dataset[0]

	id, od := 1, 1

	for i:= 1; i< len(dataset); i++ {
		if isin(i, selective_row_nums) {
			in_dataset[id] = dataset[i]
			id++
		} else {
			out_dataset[od] = dataset[i]
			od++
		}
	}
	return in_dataset, out_dataset
}

func isin(val int, list []int) bool {
	for _, i := range list {
		if i == val {
			return true
		}
	}
	return false
}