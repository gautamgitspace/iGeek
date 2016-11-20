package main

import (
    "fmt"
    "bufio"
    "os"
    "strings"
    "strconv"
    "sort"
)

func main() {
    file, err := os.Open("/Users/Gautam/Desktop/phones.txt")
    if err != nil {
        fmt.Print(err)
    }
    defer file.Close()
    container := ""
    var tokens []string
    phoneMap := make(map[int]string)

    scanner := bufio.NewScanner(file)
    for scanner.Scan(){
      container = scanner.Text()
      tokens = strings.Split(container, ",")
      phoneCount, _ := strconv.Atoi(strings.TrimSpace(tokens[2]))
      phoneMap[phoneCount] = tokens[3]
    }
    var keys []int
    for k := range phoneMap{
      keys = append(keys, k)
    }
    sort.Ints(keys)
    fmt.Println("ASC ORDER:")
    for _, k := range keys {
      fmt.Println("Key:", k, "Value:", phoneMap[k])
    }
    fmt.Println("DESC ORDER:")
    sort.Sort(sort.Reverse(sort.IntSlice(keys)))
    for _, k := range keys {
      fmt.Println("Key:", k, "Value:", phoneMap[k])
    }
}
