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

get_quiz_items = {
    200: {
        "description": "Successful response",
        "content": {
            "application/json": {
                "example": [
                    {
                        "id": 50,
                        "question": "This mounted figure appears on Ralph Lauren products",
                        "answer": "a polo player",
                        "created_at": "2022-07-27T00:24:02.273000+00:00"
                    },
                    {
                        "id": 55,
                        "question": "He sought & taught Nirvana in India 500 years before Christ",
                        "answer": "Buddha (SiddhÄrtha Gautama)",
                        "created_at": "2022-07-27T00:24:02.301000+00:00"
                    },
                    {
                        "id": 198568,
                        "question": "Not just about tulips, in 2017 this European country had 50% of the world's exports of cut flowers",
                        "answer": "the Netherlands",
                        "created_at": "2022-07-27T02:32:56.014000+00:00"
                    }
                ]
            }
        }
    },
    204: {
        "description": "Empty quiz item table"
    },
    422: {
        "description": "Validation Error",
        "content": {
            "application/json": {
                "examples": {
                    "limit < 1": {
                        "summary": "limit < 1",
                        "value": {
                            "detail": [
                                {
                                    "loc": [
                                        "query",
                                        "limit"
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
                    "limit > 1000": {
                        "summary": "limit > 1000",
                        "value": {
                            "detail": [
                                {
                                    "loc": [
                                        "query",
                                        "limit"
                                    ],
                                    "msg": "ensure this value is less than or equal to 1000",
                                    "type": "value_error.number.not_le",
                                    "ctx": {
                                        "limit_value": 1000
                                    }
                                }
                            ]
                        }
                    },
                    "invalid limit": {
                        "summary": "invalid limit",
                        "value": {
                            "detail": [
                                {
                                    "loc": [
                                        "query",
                                        "limit"
                                    ],
                                    "msg": "value is not a valid integer",
                                    "type": "type_error.integer"
                                }
                            ]
                        }
                    },
                    "invalid order_by": {
                        "summary": "invalid order_by",
                        "value": {
                            "detail": [
                                {
                                    "loc": [
                                        "query",
                                        "order_by"
                                    ],
                                    "msg": "unexpected value; permitted: 'id', 'question', 'answer', 'created_at'",
                                    "type": "value_error.const",
                                    "ctx": {
                                        "given": "some_unexistent_field",
                                        "permitted": [
                                            "id",
                                            "question",
                                            "answer",
                                            "created_at"
                                        ]
                                    }
                                }
                            ]
                        }
                    },
                    "invalid order type": {
                        "summary": "invalid order type",
                        "value": {
                            "detail": [
                                {
                                    "loc": [
                                        "query",
                                        "order"
                                    ],
                                    "msg": "unexpected value; permitted: 'asc', 'desc'",
                                    "type": "value_error.const",
                                    "ctx": {
                                        "given": "lorem_ipsum",
                                        "permitted": [
                                            "asc",
                                            "desc"
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                }
            }
        }
    }
}

get_items_count = {
    200: {
        "description": "Successful response",
        "content": {
            "application/json": {
                "example": {
                    "count": 4200
                }
            }
        }
    }
}
