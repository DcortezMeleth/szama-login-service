FROM python:3-onbuild
COPY . /usr/src/app
CMD ["python", "sample.py"]
