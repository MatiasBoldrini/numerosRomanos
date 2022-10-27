FROM python:3
RUN git clone https://github.com/MatiasBoldrini/numerosRomanos.git
WORKDIR /numerosRomanos
RUN pip install -r requirements.txt
CMD ["python3", "-m", "unittest"]
