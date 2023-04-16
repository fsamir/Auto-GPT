#FROM node:16
#
#RUN apt-get update \
# && apt-get install -y chromium \
#    fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf libxss1
##    \
##    --no-install-recommends

## non-root user that comes with `node` images.
#USER node
##RUN mkdir -p /home/node

ARG base_image=base_image=seleniarm/standalone-chromium:103.0
FROM $base_image

ENV CHROMEDRIVER_PORT 4444
ENV CHROMEDRIVER_WHITELISTED_IPS "127.0.0.1"
ENV CHROMEDRIVER_URL_BASE ''
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
ENV PUPPETEER_PRODUCT=chrome
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium

#Force all commans to use bash - nedded for nvm
SHELL ["/bin/bash", "-i", "-c"]

#Default user from selenoum image
USER seluser

ENV NODE_VERSION=16.13.0
ENV NVM_DIR=/home/seluser/.nvm
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
RUN . "$NVM_DIR/nvm.sh" && nvm install ${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm use v${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm alias default v${NODE_VERSION}
ENV PATH="/home/seluser/.nvm/versions/node/v${NODE_VERSION}/bin/:${PATH}"


WORKDIR /app

RUN npm install -g puppeteer@^19.8.5 mocha@10.2.0 should@13.2.3

COPY --chown=seluser ./bash-exec.sh /opt/
RUN chmod +x /opt/bash-exec.sh
ENTRYPOINT ["/opt/bash-exec.sh"]

COPY --chown=seluser package.json .
#COPY --chown=seluser package-lock.json .
RUN npm install

COPY --chown=seluser src/ src/

