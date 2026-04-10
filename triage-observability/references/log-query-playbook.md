# Log Query Playbook

To reduce noisy logs:

- filter by level first
- then by service or component
- then by one error string, request ID, or user journey marker
- stop when you can explain one concrete failure path

If structured logs are missing the fields you need, treat that as a tooling gap worth fixing.
