from pathlib import Path

# Project Root
ROOT = Path.cwd()

# ----------------------------
# Folders to Create
# ----------------------------
folders = [
    "app",
    "app/api",
    "app/core",
    "app/database",
    "app/middleware",
    "app/models",
    "app/schemas",
    "app/services",
    "app/utils",
    "docs",
    "tests",
    ".github",
    ".github/workflows",
]

# ----------------------------
# Files to Create
# ----------------------------
files = [
    # App
    "app/__init__.py",
    "app/main.py",

    # API
    "app/api/__init__.py",
    "app/api/routes.py",

    # Core
    "app/core/__init__.py",
    "app/core/config.py",
    "app/core/logger.py",

    # Database
    "app/database/__init__.py",
    "app/database/connection.py",
    "app/database/session.py",

    # Middleware
    "app/middleware/__init__.py",
    "app/middleware/request_id.py",

    # Models
    "app/models/__init__.py",
    "app/models/url.py",

    # Schemas
    "app/schemas/__init__.py",
    "app/schemas/url.py",

    # Services
    "app/services/__init__.py",
    "app/services/shortener.py",
    "app/services/url_service.py",

    # Utils
    "app/utils/__init__.py",
    "app/utils/helpers.py",

    # Docs
    "docs/architecture.md",
    "docs/database.md",
    "docs/deployment.md",
    "docs/api.md",

    # Tests
    "tests/__init__.py",
    "tests/test_api.py",

    # GitHub Actions
    ".github/workflows/ci.yml",

    # Root Files
    ".env",
    ".env.example",
    ".gitignore",
    "Dockerfile",
    "docker-compose.yml",
    "pytest.ini",
    "README.md",
    "requirements.txt",
]

# ----------------------------
# Create Folders
# ----------------------------
for folder in folders:
    (ROOT / folder).mkdir(parents=True, exist_ok=True)

# ----------------------------
# Create Files
# ----------------------------
for file in files:
    path = ROOT / file
    path.touch(exist_ok=True)

print("\n✅ Project structure created successfully!\n")

print(ROOT)