call_for_quiz_items = """
# Request insertion of `count` items from jservice.io

- Schedules jservice.io call for `count` items as starlette.BackgroundTasks
- Returns last inserted row

## Request body

### Required fields:

- `count`: int, in range 1-100
"""

get_quiz_items = """
# Select inserted quiz items

## Query parameters

### Optional:

- `limit`: int, in range 1-1000, defaults to 10
- `order_by`: str, in ['id', 'question', 'answer', 'created_at'], defaults to 'id'
- `order`: str, in ['asc', 'desc'], defaults to 'asc'
"""

get_items_count = """
# Get the number of quiz items in db
"""
