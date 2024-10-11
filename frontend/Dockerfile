# Use Node.js as base image
FROM node:16

# Set the working directory
WORKDIR /app

# Install dependencies
COPY package.json .
RUN npm install

# Copy the application code
COPY . .

# Build the React app
RUN npm run build

# Serve the static files with a simple server
RUN npm install -g serve
CMD ["serve", "-s", "build", "-l", "3000"]
