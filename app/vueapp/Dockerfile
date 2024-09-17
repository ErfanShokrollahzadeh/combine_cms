# Use the official Node.js image as the base image
FROM node:14

# Set the working directory to /app
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the Vue.js project files to the container
COPY . .

# Expose port 8080
EXPOSE 8080

# Run the Vue.js development server
CMD ["npm", "run", "serve"]
