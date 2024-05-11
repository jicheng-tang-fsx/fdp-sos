uvicorn api:app --reload --host 0.0.0.0

docker build -t sos . && docker kill fdp-sos && docker rm fdp-sos && docker run -d --network host --name fdp-sos -v ./config.toml:/app/config.toml -v ./logs:/app/logs sos