FROM python:3
WORKDIR /workdir
COPY . .
RUN pip install --upgrade pip && pip install \
    black \
    codecov \
    flake8 \
    geopandas \
    matplotlib \
    mutmut \
    mypy \
    pylint \
    pytest \
    pytest-cov \
    utm
