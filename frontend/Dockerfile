# Use Node.js image as base
FROM node:18.21.0

# Set working directory inside container
WORKDIR /app

# Copy package.json and package-lock.json to container
COPY package.json package-lock.json /app/

ENV NODE_OPTIONS=--openssl-legacy-provider

# Install dependencies
RUN npm install

# Copy all the files into the container
COPY . /app/

# Expose the port for React
EXPOSE 3000

# Run React app
CMD ["npm", "start"]
