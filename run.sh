uvicorn api:app --reload --host 0.0.0.0

docker kill fdp-sos && docker rm fdp-sos && docker run -d --network host --name fdp-sos -v ./logs:/app/logs sos