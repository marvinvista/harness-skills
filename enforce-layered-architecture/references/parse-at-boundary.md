# Parse At Boundary

Prefer validating external or loosely typed data where it enters the system:

- API handlers
- queue consumers
- file readers
- third-party integrations

Do not let guessed shapes leak inward and become internal assumptions.
