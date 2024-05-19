# Use the official Node.js image as the base image
FROM node:lts-alpine as build-stage

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json into the container at /app
COPY kazirestaurant_vue/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code into the container at /app
COPY kazirestaurant_vue/ .

# Build the Vue.js application
RUN npm run build

# Production stage
FROM nginx:stable-alpine as production-stage

# Copy the build output to Nginx's HTML directory
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Expose port 8080
EXPOSE 80

# Command to run the application
CMD ["nginx", "-g", "daemon off;"]
