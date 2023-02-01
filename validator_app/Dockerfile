FROM python:3.11.0

# Update default packages
RUN apt-get update

# Get Ubuntu packages
RUN apt-get install -y \
    build-essential \
    curl

# Update new packages
RUN apt-get update

# Get Rust
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y

RUN echo 'source $HOME/.cargo/env' >> $HOME/.bashrc

WORKDIR /usr/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY ./requirements.txt /usr/validator_app/requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade -r /usr/validator_app/requirements.txt

COPY . /usr/validator_app/