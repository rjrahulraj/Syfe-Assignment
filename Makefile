

.PHONY: all build run test clean

all: build

build:
	go build -o my-go-project ./cmd/server

run: build
	./my-go-project

test:
	go test ./...

clean:
	go clean
	rm -f my-go-project