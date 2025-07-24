# Build stage
FROM golang:1.22.2-alpine AS builder

WORKDIR /app
COPY main.go .
COPY go.mod .

# Build the Go binary
RUN go build -o server .

# Final stage
FROM alpine:latest

WORKDIR /app
COPY --from=builder /app/server .

EXPOSE 8080

CMD ["./server"]
