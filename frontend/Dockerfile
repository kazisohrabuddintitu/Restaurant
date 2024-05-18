# Use the official Node.js image as the base image
FROM node:latest

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json into the container at /app
COPY kazirestaurant_vue/package*.json ./


RUN npm install -g @vue/cli
# Install dependencies
RUN npm install

# Install Vite globally
# RUN npm install -g vite

# Copy the rest of the application code into the container at /app
COPY kazirestaurant_vue/ .

# Expose port 8080 to the outside world
EXPOSE 8080

# Command to run the application
CMD ["npm", "run", "build"]
