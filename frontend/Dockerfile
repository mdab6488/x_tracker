# Use Node.js 20 as the base image
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install --legacy-peer-deps

# Copy the rest of the application code
COPY . .

# Build the React app (for production)
# RUN npm run build

# Expose port 3000
EXPOSE 3000

# Start the development server
CMD ["npm", "start"]