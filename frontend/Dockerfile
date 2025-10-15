# Stage 1 - Build the React app
FROM node:20-alpine AS build

WORKDIR /app
COPY package*.json ./
RUN npm install --production
COPY . .
RUN npm run build

# Stage 2 - Serve static files with Nginx
FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
