# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_find_last_5 1'] = {
    'data': {
        'me': {
            'email': 'user-0@graphene-is-awesome.com',
            'firstName': 'user-0',
            'friends': {
                'edges': [
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzA0',
                        'node': {
                            'friendSince': '2021-03-04T00:00:00',
                            'profile': {
                                'email': 'user-4@graphene-is-awesome.com',
                                'firstName': 'user-4',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMDQ='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzAz',
                        'node': {
                            'friendSince': '2021-03-03T00:00:00',
                            'profile': {
                                'email': 'user-3@graphene-is-awesome.com',
                                'firstName': 'user-3',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMDM='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzAy',
                        'node': {
                            'friendSince': '2021-03-02T00:00:00',
                            'profile': {
                                'email': 'user-2@graphene-is-awesome.com',
                                'firstName': 'user-2',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMDI='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzAx',
                        'node': {
                            'friendSince': '2021-03-01T00:00:00',
                            'profile': {
                                'email': 'user-1@graphene-is-awesome.com',
                                'firstName': 'user-1',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMDE='
                            }
                        }
                    }
                ],
                'pageInfo': {
                    'endCursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzAx',
                    'hasNextPage': True,
                    'hasPreviousPage': False,
                    'startCursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzA0'
                }
            },
            'id': 'TWU6NjBmMDE1M2M0OWM1MTIzNjYyNzRlYzAw'
        }
    }
}

snapshots['test_friends_query_display_page_info 1'] = {
    'data': {
        'me': {
            'email': 'user-0@graphene-is-awesome.com',
            'firstName': 'user-0',
            'friends': {
                'edges': [
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzA2',
                        'node': {
                            'friendSince': '2021-03-06T00:00:00',
                            'profile': {
                                'email': 'user-6@graphene-is-awesome.com',
                                'firstName': 'user-6',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMDY='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzA3',
                        'node': {
                            'friendSince': '2021-03-07T00:00:00',
                            'profile': {
                                'email': 'user-7@graphene-is-awesome.com',
                                'firstName': 'user-7',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMDc='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzA4',
                        'node': {
                            'friendSince': '2021-03-08T00:00:00',
                            'profile': {
                                'email': 'user-8@graphene-is-awesome.com',
                                'firstName': 'user-8',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMDg='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzA5',
                        'node': {
                            'friendSince': '2021-03-09T00:00:00',
                            'profile': {
                                'email': 'user-9@graphene-is-awesome.com',
                                'firstName': 'user-9',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMDk='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzBh',
                        'node': {
                            'friendSince': '2021-03-10T00:00:00',
                            'profile': {
                                'email': 'user-10@graphene-is-awesome.com',
                                'firstName': 'user-10',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMGE='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzBi',
                        'node': {
                            'friendSince': '2021-03-11T00:00:00',
                            'profile': {
                                'email': 'user-11@graphene-is-awesome.com',
                                'firstName': 'user-11',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMGI='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzBj',
                        'node': {
                            'friendSince': '2021-03-12T00:00:00',
                            'profile': {
                                'email': 'user-12@graphene-is-awesome.com',
                                'firstName': 'user-12',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMGM='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzBk',
                        'node': {
                            'friendSince': '2021-03-13T00:00:00',
                            'profile': {
                                'email': 'user-13@graphene-is-awesome.com',
                                'firstName': 'user-13',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMGQ='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzBl',
                        'node': {
                            'friendSince': '2021-03-14T00:00:00',
                            'profile': {
                                'email': 'user-14@graphene-is-awesome.com',
                                'firstName': 'user-14',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMGU='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzBm',
                        'node': {
                            'friendSince': '2021-03-15T00:00:00',
                            'profile': {
                                'email': 'user-15@graphene-is-awesome.com',
                                'firstName': 'user-15',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMGY='
                            }
                        }
                    }
                ],
                'pageInfo': {
                    'endCursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzBm',
                    'hasNextPage': True,
                    'hasPreviousPage': True,
                    'startCursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzA2'
                }
            },
            'id': 'TWU6NjBmMDE1M2M0OWM1MTIzNjYyNzRlYzAw'
        }
    }
}

snapshots['test_friends_query_retrieves_first_10_results 1'] = {
    'data': {
        'me': {
            'email': 'user-0@graphene-is-awesome.com',
            'firstName': 'user-0',
            'friends': {
                'edges': [
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzAx',
                        'node': {
                            'friendSince': '2021-03-01T00:00:00',
                            'profile': {
                                'email': 'user-1@graphene-is-awesome.com',
                                'firstName': 'user-1',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMDE='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzAy',
                        'node': {
                            'friendSince': '2021-03-02T00:00:00',
                            'profile': {
                                'email': 'user-2@graphene-is-awesome.com',
                                'firstName': 'user-2',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMDI='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzAz',
                        'node': {
                            'friendSince': '2021-03-03T00:00:00',
                            'profile': {
                                'email': 'user-3@graphene-is-awesome.com',
                                'firstName': 'user-3',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMDM='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzA0',
                        'node': {
                            'friendSince': '2021-03-04T00:00:00',
                            'profile': {
                                'email': 'user-4@graphene-is-awesome.com',
                                'firstName': 'user-4',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMDQ='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzA1',
                        'node': {
                            'friendSince': '2021-03-05T00:00:00',
                            'profile': {
                                'email': 'user-5@graphene-is-awesome.com',
                                'firstName': 'user-5',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMDU='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzA2',
                        'node': {
                            'friendSince': '2021-03-06T00:00:00',
                            'profile': {
                                'email': 'user-6@graphene-is-awesome.com',
                                'firstName': 'user-6',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMDY='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzA3',
                        'node': {
                            'friendSince': '2021-03-07T00:00:00',
                            'profile': {
                                'email': 'user-7@graphene-is-awesome.com',
                                'firstName': 'user-7',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMDc='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzA4',
                        'node': {
                            'friendSince': '2021-03-08T00:00:00',
                            'profile': {
                                'email': 'user-8@graphene-is-awesome.com',
                                'firstName': 'user-8',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMDg='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzA5',
                        'node': {
                            'friendSince': '2021-03-09T00:00:00',
                            'profile': {
                                'email': 'user-9@graphene-is-awesome.com',
                                'firstName': 'user-9',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMDk='
                            }
                        }
                    },
                    {
                        'cursor': 'b2JqZWN0SWQ6NjBmMDFhMGI0OWM1MTIzNjYyNzRlYzBh',
                        'node': {
                            'friendSince': '2021-03-10T00:00:00',
                            'profile': {
                                'email': 'user-10@graphene-is-awesome.com',
                                'firstName': 'user-10',
                                'id': 'UHJvZmlsZTo2MGYwMTUzYzQ5YzUxMjM2NjI3NGVjMGE='
                            }
                        }
                    }
                ]
            },
            'id': 'TWU6NjBmMDE1M2M0OWM1MTIzNjYyNzRlYzAw'
        }
    }
}
