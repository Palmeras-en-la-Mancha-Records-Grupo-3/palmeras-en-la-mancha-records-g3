import os
from dotenv import load_dotenv


load_dotenv()


APP_TITLE: str = os.getenv(
    "APP_TITLE",
    "Palmeras en la Mancha Records API"
)

APP_VERSION: str = os.getenv(
    "APP_VERSION",
    "1.0.0"
)

APP_DESCRIPTION: str = os.getenv(
    "APP_DESCRIPTION",
    "REST API for managing the Palmeras en la Mancha Records catalog."
)


DATABASE_NAME: str = os.getenv(
    "DATABASE_NAME",
    "palmeras_records.db"
)

DATABASE_URL: str = os.getenv(
    "DATABASE_URL",
    f"sqlite:///./{DATABASE_NAME}"
)

CLOUDINARY_CLOUD_NAME: str = os.getenv(
    "CLOUDINARY_CLOUD_NAME"
)

CLOUDINARY_API_KEY: str = os.getenv(
    "CLOUDINARY_API_KEY"
)

CLOUDINARY_API_SECRET: str = os.getenv(
    "CLOUDINARY_API_SECRET"
)