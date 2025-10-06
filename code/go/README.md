
# 🐹 Go Learning & Experiments

### *"It's time to go!"*

Welcome to my personal Go (Golang) repository!  
This is where I document my journey learning Go — exploring syntax, tools, and concepts through practical experiments and small projects.
New to Go, but excited to explore what makes it so powerful, simple, and efficient.

---

## 🎯 Purpose

The goal of this repository is to:

- Learn and understand Go fundamentals  
- Experiment with idiomatic Go patterns and tools  
- Build small, self-contained projects and examples  
- Keep notes, resources, and essential commands handy  
- Gradually develop a deeper understanding of Go’s philosophy and ecosystem

---

## 🧭 Repository Structure

```

.
├── examples/          # Small standalone Go examples
├── projects/          # Larger experiments or mini-projects
├── snippets/          # Reusable snippets and code templates
├── notes/             # Learning notes, links, and documentation
└── README.md

````

---

## ⚙️ Setup

### 1. Install Go

Follow the official installation guide:  
👉 [https://go.dev/doc/install](https://go.dev/doc/install)

Verify installation:
```bash
go version
````

### 2. Create a new module

```bash
mkdir myproject
cd myproject
go mod init github.com/yourusername/myproject
```

### 3. Run Go files

```bash
go run main.go
```

### 4. Build an executable

```bash
go build -o app main.go
./app
```

### 5. Run tests

```bash
go test ./...
```

### 6. Format and tidy code

```bash
go fmt ./...
go mod tidy
```

---

## 💡 Essential Go Commands

| Command                | Description                      |
| ---------------------- | -------------------------------- |
| `go version`           | Check Go version                 |
| `go env`               | Show Go environment variables    |
| `go mod init <module>` | Initialize a new module          |
| `go get <pkg>`         | Add a new dependency             |
| `go build`             | Compile code to binary           |
| `go run`               | Run code directly                |
| `go test`              | Run tests                        |
| `go fmt`               | Auto-format Go code              |
| `go mod tidy`          | Clean and organize dependencies  |
| `go doc <pkg>`         | Show documentation for a package |

---

## 🎓 Learning Goals

* [ ] Understand Go syntax and data types
* [ ] Work with packages and modules
* [ ] Learn about interfaces and structs
* [ ] Explore concurrency with goroutines and channels
* [ ] Learn error handling and logging best practices
* [ ] Build small CLI tools
* [ ] Create REST APIs using `net/http`
* [ ] Write unit tests and benchmarks
* [ ] Use Go’s standard library effectively
* [ ] Contribute to open-source Go projects

---

## 📚 Resources

### Official

* [Go.dev – Official Website](https://go.dev)
* [Tour of Go](https://go.dev/tour/)
* [Effective Go](https://go.dev/doc/effective_go)
* [Go Standard Library](https://pkg.go.dev/std)

### Tutorials & References

* [Go by Example](https://gobyexample.com/)
* [Learn Go with Tests](https://quii.gitbook.io/learn-go-with-tests/)
* [Gophercises](https://gophercises.com/)
* [JustForFunc YouTube Series](https://www.youtube.com/c/JustForFunc)

### Tools

* [Go Playground](https://go.dev/play/)
* [Golangci-lint](https://golangci-lint.run/)
* [Air (live reload for Go)](https://github.com/air-verse/air)

---

## 🧠 Notes

This repository will grow over time as I:

* Experiment with different Go features
* Add code examples and notes
* Refactor as I learn idiomatic Go practices

It’s not meant to be perfect — it’s a living notebook of progress and curiosity.

---