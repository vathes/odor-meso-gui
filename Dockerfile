FROM continuumio/miniconda3
COPY . /src/gui
RUN pip install -e /src/gui
