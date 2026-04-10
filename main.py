from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.proxy_headers import ProxyHeadersMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

app = FastAPI()

# 👇 CLAVE
app.add_middleware(ProxyHeadersMiddleware)

# 👇 opcional pero recomendado
app.add_middleware(HTTPSRedirectMiddleware)

# 👇 tu CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)