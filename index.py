import bottle
from bottle import route, run, template
from concurrent.futures import ThreadPoolExecutor
import image

def call_service():
    directoryName = 'photos'
    # Using a thread pool to process images concurrently
    with ThreadPoolExecutor() as executor:
        executor.submit(image.process, directoryName)

@route('/')
def index():
    """Home page"""
    title = "Image Processor App"
    call_service()
    return template('index.tpl', data="Request completed!", title=title)

if __name__ == '__main__':
    run(host='0.0.0.0', port=8000, debug=False, reloader=True)
