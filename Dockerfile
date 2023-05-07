FROM python:3.9-slim-buster AS compile-image
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

COPY requirements.txt .
RUN pip install --user -r requirements.txt

COPY setup.py .
COPY myapp/ .
RUN pip install --user .

FROM python:3.9-slim-buster AS build-image
COPY --from=compile-image /root/.local /root/.local

# Make sure scripts in .local are usable:
ENV PATH=/root/.local/bin:$PATH
CMD ['myapp']

