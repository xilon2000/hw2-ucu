FROM golang:1.22-alpine AS builder

WORKDIR /app

COPY main.go .

RUN CGO_ENABLED=0 GOOS=linux GO111MODULE=off go build -ldflags="-s -w" -o /app/hello-world main.go

FROM scratch

COPY --from=builder /app/hello-world /hello-world

ENTRYPOINT ["/hello-world"]