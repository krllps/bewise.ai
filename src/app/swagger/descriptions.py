quizAPI = """
# Tasks:

#### 1. Implement `POST` endpoint that accepts requests with `JSON` request body of type {"questions_num": integer}
#### 2. After consuming `POST` request, an external API call has to be made with accepted request body parameters
#### 3. Fetch and insert into `PostgreSQL` db data with following fields: [`'id'`, `'question'`, `'answer'`, `'created_at'`] where `'id'` is unique
#### 4. The number of inserted rows has to be as specified in request body
#### 5. If a duplicate (or more) occured, make extra API calls up until the point when rows inserted in db = specified value
#### 6. Endpoint has to respond with the last inserted row
"""

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
