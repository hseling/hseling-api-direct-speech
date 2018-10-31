FROM hseling/hseling-api-base:python3.6-alpine3.7

LABEL maintainer="Sergey Sobko <ssobko@hse.ru>"

COPY ./app /app
COPY ./hseling_api_direct_speech /app/hseling_api_direct_speech
