FROM ubuntu:latest
RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip install pandas numpy seaborn matplotlib scikit-learn scipy
RUN mkdir -p home/doc-bd-a1
COPY dataset.csv .
COPY load.py .
COPY dpre.py .
CMD ["bash"]

