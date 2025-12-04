# Python GitHub Actions Example with Docker

A minimal Python project to demonstrate GitHub Actions CI/CD with automated Docker image builds.

## Project Structure

```
training/
├── .github/
│   └── workflows/
│       └── test.yml          # GitHub Actions workflow
├── calculator.py             # Simple calculator module
├── test_calculator.py        # Pytest test suite
├── main.py                   # Demo script (Docker entry point)
├── Dockerfile                # Docker image definition
├── .dockerignore             # Docker build exclusions
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Local Testing

To run the tests locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
pytest -v test_calculator.py

# Run the demo script
python main.py
```

## Code Quality

This project uses automated code quality tools to ensure consistent, high-quality code.

### Linting

Check code for issues using ruff:

```bash
# Check for linting errors
ruff check .

# Auto-fix linting issues where possible
ruff check . --fix
```

### Formatting

Ensure consistent code formatting:

```bash
# Check if code is properly formatted
ruff format --check .

# Auto-format all code
ruff format .
```

### Code Coverage

Run tests with coverage reporting:

```bash
# Run tests with coverage (must be ≥80%)
pytest --cov --cov-report=term-missing

# Generate HTML coverage report
pytest --cov --cov-report=html
# Then open htmlcov/index.html in your browser
```

### Run All Quality Checks

Run all quality checks locally before pushing:

```bash
# Install dependencies
pip install -r requirements.txt

# Run linting
ruff check .

# Run formatting check
ruff format --check .

# Run tests with coverage
pytest --cov --cov-report=term-missing --cov-fail-under=80
```
## Docker Usage

### Build Docker Image Locally

```bash
docker build -t calculator .
```

### Run the Docker Container

```bash
docker run calculator
```

This will execute the demo script that showcases all calculator functions.

### Pull from GitHub Container Registry

After pushing to GitHub, the image will be automatically built and published. You can pull and run it:

```bash
# Pull the latest version
docker pull ghcr.io/mbanf/training:latest

# Run the pulled image
docker run ghcr.io/mbanf/training:latest

# Pull a specific version (by commit SHA)
docker pull ghcr.io/mbanf/training:<commit-sha>
```

## GitHub Actions

The workflow (`.github/workflows/test.yml`) will automatically:

### Code Quality (on every push and PR)
- Run **ruff** linting to check code quality
- Verify code formatting standards
- Run tests with **coverage reporting** (minimum 80% required)
- All quality checks must pass before tests run

### Testing (on every push and PR)
- Run on every push to `main` or `master` branches
- Run on every pull request to `main` or `master` branches
- Test against Python 3.9, 3.10, and 3.11
- Install dependencies from `requirements.txt`
- Run all tests with pytest

### Docker Build (on push to main only)
- Build Docker image after all tests pass
- Push to GitHub Container Registry (ghcr.io)
- Tag with:
  - `latest` for the most recent build on main branch
  - Git commit SHA for version tracking

## Deployment

1. Commit and push your code:
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin main
   ```

2. GitHub Actions will automatically:
   - Run all tests
   - Build the Docker image
   - Push to ghcr.io/mbanf/training

3. Monitor the workflow at: https://github.com/mbanf/training/actions

4. View published packages at: https://github.com/mbanf?tab=packages

## What the Calculator Does

The calculator module includes basic arithmetic operations:
- Addition
- Subtraction
- Multiplication
- Division (with zero-division error handling)
- Hello World function

Each operation has corresponding tests to ensure correctness.
