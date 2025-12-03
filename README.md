# Python GitHub Actions Example

A minimal Python project to test GitHub Actions CI/CD.

## Project Structure

```
training/
├── .github/
│   └── workflows/
│       └── test.yml          # GitHub Actions workflow
├── calculator.py             # Simple calculator module
├── test_calculator.py        # Pytest test suite
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
```

## GitHub Actions

The workflow (`.github/workflows/test.yml`) will automatically:
- Run on every push to `main` or `master` branches
- Run on every pull request to `main` or `master` branches
- Test against Python 3.9, 3.10, and 3.11
- Install dependencies from `requirements.txt`
- Run all tests with pytest

## Next Steps

1. Commit and push this code to your GitHub repository:
   ```bash
   git add .
   git commit -m "Add minimal Python example with GitHub Actions"
   git push origin main
   ```

2. Go to your GitHub repository and click on the "Actions" tab to see the workflow run

3. The workflow will run automatically on each push and pull request

## What the Tests Cover

The calculator module includes basic arithmetic operations:
- Addition
- Subtraction
- Multiplication
- Division (with zero-division error handling)

Each operation has corresponding tests to ensure correctness.
