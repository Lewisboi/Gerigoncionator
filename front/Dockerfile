FROM oven/bun:latest

WORKDIR /app

# Install dependencies
COPY  package.json /app/package.json

RUN bun install

# Copy source code
COPY . /app

# Expose port
EXPOSE 5173

# Start
CMD ["bun", "run", "dev"]