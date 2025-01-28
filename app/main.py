import os
import uuid
from fastapi import FastAPI, UploadFile, WebSocket, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import asyncio
from typing import Set, Dict
from .face_detector import FaceDetector
from .utils import save_image

app = FastAPI()

# Mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize face detector
face_detector = FaceDetector()

# Store active websocket connections
active_connections: Set[WebSocket] = set()

@app.post("/image")
async def upload_image(file: UploadFile):
    try:
        # Read image file
        image_bytes = await file.read()
        
        # Process image and detect faces
        processed_image, face_count = face_detector.detect_faces(image_bytes)
        
        # Generate unique filename
        filename = f"{uuid.uuid4()}.jpg"
        image_path = save_image(processed_image, filename)
        
        # Generate URL for the processed image
        image_url = f"/static/images/{filename}"
        
        # Notify all connected clients
        message = {
            "url": image_url,
            "face_count": face_count
        }
        await notify_clients(message)
        
        return {"url": image_url, "face_count": face_count}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.websocket("/faces")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.add(websocket)
    try:
        while True:
            # Keep connection alive
            await websocket.receive_text()
    except:
        active_connections.remove(websocket)

async def notify_clients(message: Dict):
    for connection in active_connections:
        try:
            await connection.send_json(message)
        except:
            active_connections.remove(connection)