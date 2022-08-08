call_for_quiz_items = {
    200: {
        "description": "Successful response",
        "content": {
            "application/json": {
                "examples": {
                    "success": {
                        "summary": "success",
                        "value": {
                            "id": 198568,
                            "question": "Not just about tulips, in 2017 this European country had 50% of the world's exports of cut flowers",
                            "answer": "the Netherlands",
                            "created_at": "2022-07-27T02:32:56.014000+00:00"
                        }
                    },
                    "empty": {
                        "summary": "empty",
                        "value": []
                    }
                }
            }
        }
    },
    422: {
        "description": "Validation Error",
        "content": {
            "application/json": {
                "examples": {
                    "count > 100": {
                        "summary": "count > 100",
                        "value": {
                            "detail": [
                                {
                                    "loc": [
                                        "body",
                                        "count"
                                    ],
                                    "msg": "ensure this value is less than or equal to 100",
                                    "type": "value_error.number.not_le",
                                    "ctx": {
                                        "limit_value": 100
                                    }
                                }
                            ]
                        }
                    },
                    "count < 1": {
                        "summary": "count < 1",
                        "value": {
                            "detail": [
                                {
                                    "loc": [
                                        "body",
                                        "count"
                                    ],
                                    "msg": "ensure this value is greater than 0",
                                    "type": "value_error.number.not_gt",
                                    "ctx": {
                                        "limit_value": 0
                                    }
                                }
                            ]
                        }
                    },
                    "no count": {
                        "summary": "no count",
                        "value": {
                            "detail": [
                                {
                                    "loc": [
                                        "body",
                                        "count"
                                    ],
                                    "msg": "none is not an allowed value",
                                    "type": "type_error.none.not_allowed"
                                }
                            ]
                        }
                    },
                    "empty request body": {
                        "summary": "empty request body",
                        "value": {
                            "detail": [
                                {
                                    "loc": [
                                        "body",
                                        "count"
                                    ],
                                    "msg": "field required",
                                    "type": "value_error.missing"
                                }
                            ]
                        }
                    }
                }
            }
        }
    }
}
