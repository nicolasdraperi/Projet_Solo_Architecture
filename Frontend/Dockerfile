# Builder
FROM node:20-alpine as builder
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

# Serveur Nginx
FROM nginx:alpine
COPY --from=builder /app/build /usr/share/nginx/html
