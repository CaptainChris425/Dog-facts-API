from functools import lru_cache

import uvicorn

from src.config import Settings


@lru_cache()
def settings():
    return Settings()


config = settings()


if __name__ == "__main__":
    uvicorn.run(
        "src.server:app",
        host=config.HOST,
        port=config.PORT,
        reload=config.RELOAD,
        debug=config.DEBUG,
        workers=config.WORKERS,
    )
