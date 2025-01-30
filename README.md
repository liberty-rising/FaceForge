# Face Detection WebSocket Server

This application is a FastAPI-based server that performs face detection on uploaded images and broadcasts the results via WebSocket. It receives images through a POST endpoint, processes them to detect faces, and sends the results to all connected WebSocket clients.

## Features

- Face detection in uploaded images
- Real-time WebSocket notifications
- Docker containerization
- Static file serving for processed images

## Prerequisites

- Docker installed on your system
- Web browser for testing

## Installation & Running

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Build and run with Docker**
   ```bash
   docker build -t face-detection-app .
   docker run -p 8282:8282 face-detection-app
   ```

   The server will be available at `http://localhost:8282`

## Testing the Application

1. **Open the test HTML file**
   Within the root of the repository is a file named `test.html`. Open this file with your browser to initialise the websocket connection and visualise the results.

2. **Open the WebSocket client**
   - Open the `test.html` file in your web browser
   - Check the browser's console (F12) to confirm WebSocket connection

3. **Send an image for processing**
   - Go to `http://localhost:8282/docs`
   - Send a post request to the `/image` endpoint.

4. **View results**
   The processed image with detected faces will appear automatically in your browser through the WebSocket connection.

## API Endpoints

- `POST /image`: Upload an image for face detection
- `WS /faces`: WebSocket endpoint for real-time updates
- `GET /static/images/{filename}`: Access processed images

## Error Handling

The server includes error handling for:
- Invalid image uploads
- Processing errors
- WebSocket connection issues

## Notes

- The server runs on port 8282
- Processed images are stored in the `static/images` directory
- Each processed image gets a unique filename

## Troubleshooting

If you encounter any issues:
1. Ensure Docker is running
2. Check that port 8282 is not in use
3. Verify that your image file is valid
4. Check the browser console for WebSocket connection errors