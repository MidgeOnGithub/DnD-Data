import json

data = {}
data['Aasimar'] = {
    'base_ab_mod': {
        'Charisma': 2
    },
    'lifespan': '160',
    'size': {
        'tier': 'Medium',
        'h': (56, '2d10'),
        'w': (110, '2d4')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
    'subrace': {
        'Fallen': {
            'ab_mod': {
                'Strength': 1
            }
        },
        'Protector': {
            'ab_mod': {
                'Wisdom': 1
            }
        },
        'Scourge': {
            'ab_mod': {
                'Constitution': 1
            }
        },
    }
}

data['Bugbear'] = {
    'base_ab_mod': {
        'Strength': 2,
        'Dexterity': 1
    },
    'lifespan': '80',
    'size': {
        'tier': 'Medium',
        'h': (72, '2d12'),
        'w': (200, '2d6')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
    'subrace': {}
}

data['Dragonborn'] = {
    'base_ab_mod': {
        'Strength': 2,
        'Charisma': 1
    },
    'lifespan': '80',
    'size': {
        'tier': 'Medium',
        'h': (66, '2d8'),
        'w': (175, '2d6')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
    'subrace': {}
}

data['Dwarf'] = {
    'base_ab_mod': {
        'Constitution': 2
    },
    'lifespan': '350',
    'speed': {
        'standard': 25,  # Not affected by heavy armor
        'climbing': None,
        'flying': None,
        'swimming': None
    },
    'size': {
        'tier': 'Medium'
    },
    'subrace': {
        'Duergar': {
            'ab_mod': {
                'Strength': 1
            },
            'size': {
                'h': (48, '2d6'),   # Fabricated, PHB says 'between' 4-5
                'w': (140, '2d10')  # Fabricated, PHB says 'around' 150
            }
        },
        'Hill': {
            'ab_mod': {
                'Wisdom': 1
            },
            'size': {
                'h': (44, '2d4'),
                'w': (115, '2d6')
            }
        },
        'Mountain': {
            'ab_mod': {
                'Strength': 2
            },
            'size': {
                'h': (48, '2d4'),
                'w': (130, '2d6')
            }
        }
    }
}

data['Elf'] = {
    'base_ab_mod': {
        'Dexterity': 2
    },
    'lifespan': '750',
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
    'size': {
        'tier:' 'Medium'
    },
    'subrace': {
        'Drow': {
            'ab_mod': {
                'Charisma': 1
            },
            'size': {
                'h': (53, '2d6'),
                'w': (75, '1d6')
            }
        },
        'Eladrin': {
            'ab_mod': {
                'Charisma': 1
            },
            'size': {
                'h': (54, '2d12'),
                'w': (90, '1d4')
            }
        },
        'High': {
            'ab_mod': {
                'Intelligence': 1
            },
            'size': {
                'h': (54, '2d10'),
                'w': (90, '1d4')
            }
        },
        'Sea': {
            'ab_mod': {
                'Constitution': 1
            },
            'size': {
                'h': (54, '2d8'),
                'w': (90, '1d4')
            },
            'speed': {
                'swimming': 30
            }
        },
        'Shadar-kai': {
            'ab_mod': {
                'Constitution': 1
            },
            'size': {
                'h': (56, '2d8'),
                'w': (90, '1d4')
            }
        },
        'Wood': {
            'ab_mod': {
                'Wisdom': 1
            },
            'size': {
                'h': (56, '2d8'),
                'w': (90, '1d4')
            },
            'speed': {
                'standard': 35
            }
        }
    }
}

data['Firbolg'] = {
    'base_ab_mod': {
        'Strength': 1,
        'Wisdom': 2
    },
    'lifespan': '500',
    'size': {
        'tier': 'Medium',
        'h': (74, '2d12'),
        'w': (175, '2d6')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
    'subrace': {}
}

data['Genasi'] = {
    'base_ab_mod': {
        'Constitution': 2
    },
    'lifespan': '120',
    'size': {
        'tier': 'Medium',
        'h': (56, '2d10'),
        'w': (110, '2d4')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
    'subrace': {
        'Air': {
            'ab_mod': {
                'Dexterity': 1
            }
        },
        'Earth': {
            'ab_mod': {
                'Strength': 1
            }
        },
        'Fire': {
            'ab_mod': {
                'Intelligence': 1
            }
        },
        'Water': {
            'ab_mod': {
                'Wisdom': 1
            },
            'speed': {
                'swimming': 30
            }
        }
    }
}

data['Gith'] = {
    'base_ab_mod': {
        'Intelligence': 1
    },
    'lifespan': '120',
    'size': {
        'tier': 'Medium',
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
    'subrace': {
        'Githyanki': {
            'ab_mod': {
                'Strength': 2
            },
            'size': {
                'h': (60, '2d12'),
                'w': (100, '2d4')
            }
        },
        'Githzerai': {
            'ab_mod': {
                'Wisdom': 2
            },
            'size': {
                'h': (59, '2d12'),
                'w': (90, '1d4')
            }
        }
    }
}

data['Gnome'] = {
    'base_ab_mod': {
        'Intelligence': 2
    },
    'lifespan': '350:500',
    'size': {
        'tier': 'Small',
        'h': (35, '2d4'),
        'w': (35, '1')
    },
    'speed': {
        'standard': 25,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
    'subrace': {
        'Deep': {
            'ab_mod': {
                'Dexterity': 1
            },
            'lifespan': '200:250'
        },
        'Forest': {
            'ab_mod': {
                'Dexterity': 1
            }
        },
        'Rock': {
            'ab_mod': {
                'Constitution': 1
            }
        }
    }
}

"""A template for new races
data['Name'] = {
    'base_ab_mod': {
        'Ab': 0
    },
    'lifespan': ,
    'size': {
        'tier': 'Medium',
        'h': (56, '2d10'),
        'w': (110, '2d4')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
    'subrace': {
        'Subrace': {
            'stuff': 'stuff'
        }
    }
}
"""
