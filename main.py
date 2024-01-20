import logging
from io import BytesIO
from uuid import uuid1

import uvicorn
from fastapi import FastAPI, UploadFile
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse, StreamingResponse

from service.ppt_gen import PPTGenerator

app = FastAPI()
# {upload_id: PresentationFile}
app.cache_storage = dict()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/test")
async def test():
    return {"message": "Congrats, tests passed"}


@app.post("/upload")
async def upload_file(file: UploadFile, prompt: str = '', template: str = '', file_type: str = ''):
    generator = PPTGenerator(file, prompt, template, file_type)
    upload_id = str(uuid1())
    pre_file = generator.generate()
    app.cache_storage[upload_id] = pre_file
    return {"filename": file.filename, 'upload_id': upload_id}


@app.post("/download")
async def download_file(upload_id: str) -> StreamingResponse:
    output = BytesIO()
    app.cache_storage[upload_id].save(output)
    output.seek(0)

    # app.cache_storage.pop(upload_id)
    return StreamingResponse(output, media_type='application/octet-stream')


if __name__ == '__main__':
    from util.config import Config

    logging.basicConfig(level=logging.DEBUG)

    logging.debug(f"Config loaded: openai_key -> {Config.OPEN_AI_API_KEY}, unsplash_key -> {Config.UNSPLASH_API_KEY}")
    uvicorn.run(app, host="127.0.0.1", port=4000)
