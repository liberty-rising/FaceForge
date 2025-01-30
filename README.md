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

## Technical Implementation Details

### Architecture Choices

1. **FastAPI Framework**
   - Chosen for its async support and WebSocket capabilities
   - High performance and modern Python features
   - Built-in OpenAPI documentation
   - Built in swagger for API testing.

2. **Face Detection Implementation**
   ```python:app/face_detector.py
   startLine: 6
   endLine: 42
   ```
   - Uses OpenCV's Haar Cascade Classifier for face detection
   - Advantages:
     - Fast processing speed
     - Low computational requirements
     - Good for real-time applications
   - Limitations:
     - May miss faces at extreme angles
     - Less accurate than deep learning models
     - Sensitive to lighting conditions

3. **WebSocket Implementation**
   ```python:app/main.py
   startLine: 50
   endLine: 66
   ```
   - Maintains active connections in memory
   - Broadcasts results to all connected clients
   - Handles disconnections gracefully

### Potential Improvements

1. **Face Detection Enhancements**
   - Replace Haar Cascade with deep learning models:
     - MTCNN (Multi-task Cascaded Convolutional Networks)
     - RetinaFace
     - YOLOv5-face
   - These would provide:
     - Higher accuracy
     - Better handling of varied poses
     - Facial landmark detection
     - Face recognition capabilities

2. **Image Processing**
   - Add image preprocessing:
     - Automatic brightness adjustment
     - Contrast enhancement
     - Image scaling optimization
   - Implement face alignment
   - Add face attribute detection (age, gender, emotions)

3. **Performance Optimizations**
   - Add image caching
   - Implement batch processing
   - Add GPU support for faster processing
   - Optimize image storage and cleanup

4. **Security Enhancements**
   - Add authentication for WebSocket connections
   - Implement rate limiting
   - Add image validation
   - Secure file storage

5. **Scalability Improvements**
   - Implement connection pooling
   - Add load balancing
   - Use external storage (S3, Azure Blob) for images
   - Add database for tracking processed images

### Configuration Options

The current implementation allows for several adjustments in the face detection parameters:
```python:app/face_detector.py
startLine: 22
endLine: 27

Key parameters that can be tuned:
- `scaleFactor`: Affects detection accuracy vs speed (current: 1.1)
- `minNeighbors`: Controls false positive rate (current: 5)
- `minSize`: Minimum face size to detect (current: 30x30)

These parameters can be adjusted based on the specific use case:
- Lower `scaleFactor` (e.g., 1.05) for higher accuracy
- Higher `minNeighbors` (e.g., 6-8) for fewer false positives
- Adjust `minSize` based on expected face sizes in your images
```