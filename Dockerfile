FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
ENV MINICONDA_VERSION=py312_24.3.0-0-Linux-x86_64
ENV INSTALL_PATH=/miniconda3
RUN apt-get update && apt-get install -y wget vim

WORKDIR /tmp
RUN wget -O miniconda.sh "https://repo.anaconda.com/miniconda/Miniconda3-${MINICONDA_VERSION}.sh" \
    && chmod +x miniconda.sh \
    && ./miniconda.sh -b -p $INSTALL_PATH \
    && rm miniconda.sh
ENV PATH="${INSTALL_PATH}/bin:${PATH}"
RUN echo "miniconda installed"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./*.py ./

CMD exec uvicorn api:app --host 0.0.0.0 --port 8000 >> /app/logs/fdp_sos_$(date +%Y%m%d).log 2>&1
