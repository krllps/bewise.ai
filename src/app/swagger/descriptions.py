call_for_quiz_items = """
# Request insertion of `count` items from jservice.io

- Schedules jservice.io call for `count` items as starlette.BackgroundTasks
- Returns last inserted row

## Request body

### Required fields:

- `count`: int, in range 1-100
"""
