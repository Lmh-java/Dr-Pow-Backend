import logging
from uuid import uuid1

import uvicorn
from fastapi import FastAPI, UploadFile
from starlette.responses import FileResponse

from service.ppt_gen import PPTGenerator

app = FastAPI()


@app.get("/test")
async def test():
    return {"message": "Congrats, tests passed"}


@app.post("/upload")
async def upload_file(file: UploadFile, prompt: str = '', template: str = '', file_type: str = ''):
    generator = PPTGenerator(file, prompt, template, file_type)
    generator.generate()
    return {"filename": file.filename, 'upload_id': uuid1()}


@app.post("/download")
async def download_file(upload_id: str) -> FileResponse:
    return FileResponse('./tests/test_pptx.pptx', media_type='application/octet-stream', filename='test_pptx.pptx')


if __name__ == '__main__':
    from util.config import Config

    logging.basicConfig(level=logging.DEBUG)

    logging.debug(f"Config loaded: openai_key -> {Config.OPEN_AI_API_KEY}, unsplash_key -> {Config.UNSPLASH_API_KEY}")
    uvicorn.run(app, host="127.0.0.1", port=4000)
