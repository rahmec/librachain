# node:alpine will be our base image to create this image
FROM node:alpine

# Set the /app directory as working directory
WORKDIR /app

# Install ganache-cli globally
RUN npm install -g ganache-cli

# Set the default command for the image
CMD ["ganache-cli", "-h", "0.0.0.0", "-d", "Software Secutirity 1", "-p", "8550", "--gasLimit", "1000000000000000000000"]