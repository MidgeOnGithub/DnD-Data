# Opting to separately declare and append values to data like a dict
# over initializing the whole object in one long super-brace
data = {}

data['Aasimar'] = {
    'base_ab_mod': {
        'Charisma': 2
    },
    'lifespan': '160',
    'size': {
        'tier': 'Medium',
        'height': (56, '2d10'),
        'weight': (110, '2d4')
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
        'height': (72, '2d12'),
        'weight': (200, '2d6')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    }
}

data['Dragonborn'] = {
    'base_ab_mod': {
        'Strength': 2,
        'Charisma': 1
    },
    'lifespan': '80',
    'size': {
        'tier': 'Medium',
        'height': (66, '2d8'),
        'weight': (175, '2d6')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    }
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
                'height': (48, '2d6'),   # Fabricated, PHB says 'between' 4-5
                'weight': (140, '2d10')  # Fabricated, PHB says 'around' 150
            }
        },
        'Hill': {
            'ab_mod': {
                'Wisdom': 1
            },
            'size': {
                'height': (44, '2d4'),
                'weight': (115, '2d6')
            }
        },
        'Mountain': {
            'ab_mod': {
                'Strength': 2
            },
            'size': {
                'height': (48, '2d4'),
                'weight': (130, '2d6')
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
        'tier': 'Medium'
    },
    'subrace': {
        'Drow': {
            'ab_mod': {
                'Charisma': 1
            },
            'size': {
                'height': (53, '2d6'),
                'weight': (75, '1d6')
            }
        },
        'Eladrin': {
            'ab_mod': {
                'Charisma': 1
            },
            'size': {
                'height': (54, '2d12'),
                'weight': (90, '1d4')
            }
        },
        'High': {
            'ab_mod': {
                'Intelligence': 1
            },
            'size': {
                'height': (54, '2d10'),
                'weight': (90, '1d4')
            }
        },
        'Sea': {
            'ab_mod': {
                'Constitution': 1
            },
            'size': {
                'height': (54, '2d8'),
                'weight': (90, '1d4')
            },
            'speed': {
                'swimming': 30
            }
        },
        'Shadar-Kai': {
            'ab_mod': {
                'Constitution': 1
            },
            'size': {
                'height': (56, '2d8'),
                'weight': (90, '1d4')
            }
        },
        'Wood': {
            'ab_mod': {
                'Wisdom': 1
            },
            'size': {
                'height': (56, '2d8'),
                'weight': (90, '1d4')
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
        'height': (74, '2d12'),
        'weight': (175, '2d6')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    }
}

data['Genasi'] = {
    'base_ab_mod': {
        'Constitution': 2
    },
    'lifespan': '120',
    'size': {
        'tier': 'Medium',
        'height': (56, '2d10'),
        'weight': (110, '2d4')
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
                'height': (60, '2d12'),
                'weight': (100, '2d4')
            }
        },
        'Githzerai': {
            'ab_mod': {
                'Wisdom': 2
            },
            'size': {
                'height': (59, '2d12'),
                'weight': (90, '1d4')
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
        'height': (35, '2d4'),
        'weight': (35, None)
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

data['Goblin'] = {
    'base_ab_mod': {
        'Dexterity': 2,
        'Constitution': 1
    },
    'lifespan': 60,
    'size': {
        'tier': 'Small',
        'height': (41, '2d4'),
        'weight': (35, None)
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    }
}

data['Half-Elf'] = {
    'base_ab_mod': {
        'Charisma': 2,
        'Choice1': 1,
        'Choice2': 1
    },
    'lifespan': 180,
    'size': {
        'tier': 'Medium',
        'height': (56, '2d10'),
        'weight': (110, '2d4')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
    'variant': {
        'Aquatic Elf Heritage': {
            'speed': {
                'swimming': 30
            }
        },
        'Drow Heritage': {
        },
        'High Elf Heritage': {
        },
        'Wood Elf Heritage': {
        }
    }
}

data['Half-Orc'] = {
    'base_ab_mod': {
        'Strength': 2,
        'Constitution': 1
    },
    'lifespan': 75,
    'size': {
        'tier': 'Medium',
        'height': (58, '2d10'),
        'weight': (140, '2d6')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
    'variant': {
        'Aquatic Elf Heritage': {
            'speed': {
                'swimming': 30
            }
        },
        'Drow Heritage': {
        },
        'High Elf Heritage': {
        },
        'Wood Elf Heritage': {
        }
    }
}

data['Halfling'] = {
    'base_ab_mod': {
        'Dexterity': 2
    },
    'lifespan': '150',
    'size': {
        'tier': 'Small',
        'height': (31, '2d4'),
        'weight': (35, None)
    },
    'speed': {
        'standard': 25,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
    'subrace': {
        'Ghostwise': {
            'ab_mod': {
                'Wisdom': 1
            }
        },
        'Lightfoot': {
            'ab_mod': {
                'Charisma': 1
            }
        },
        'Stout': {
            'ab_mod': {
                'Constitution': 1
            }
        }
    }
}

data['Hobgoblin'] = {
    'base_ab_mod': {
        'Constitution': 2,
        'Intelligence': 1
    },
    'lifespan': 100,
    'size': {
        'tier': 'Medium',
        'height': (56, '2d10'),
        'weight': (110, '2d4')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    }
}

data['Human'] = {
    'base_ab_mod': {
        'Strength': 1,
        'Dexterity': 1,
        'Constitution': 1,
        'Intelligence': 1,
        'Wisdom': 1,
        'Charisma': 1
    },
    'lifespan': 100,
    'size': {
        'tier': 'Medium',
        'height': (56, '2d10'),
        'weight': (110, '2d4')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
    'variant': {
        'Variant': {
            'ab_mod': {
                'Choice1': 1,
                'Choice2': 1
            }
        }
    }
}

data['Kenku'] = {
    'base_ab_mod': {
        'Dexterity': 2,
        'Wisdom': 1
    },
    'lifespan': 60,
    'size': {
        'tier': 'Medium',
        'height': (52, '2d8'),
        'weight': (50, '1d6')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    }
}

data['Kobold'] = {
    'base_ab_mod': {
        'Strength': 2,
        'Dexterity': 2
    },
    'lifespan': 120,
    'size': {
        'tier': 'Small',
        'height': (25, '2d4'),
        'weight': (25, None)
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
}

data['Lizardfolk'] = {
    'base_ab_mod': {
        'Constitution': 2,
        'Wisdom': 1
    },
    'lifespan': 60,
    'size': {
        'tier': 'Medium',
        'height': (57, '2d10'),
        'weight': (120, '2d6')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': 30
    },
}

data['Orc'] = {
    'base_ab_mod': {
        'Strength': 2,
        'Constitution': 1,
        'Intelligence': 2
    },
    'lifespan': 50,
    'size': {
        'tier': 'Medium',
        'height': (52, '2d8'),
        'weight': (175, '2d6')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
}

data['Tabaxi'] = {
    'base_ab_mod': {
        'Dexterity': 2,
        'Charisma': 1
    },
    'lifespan': 100,
    'size': {
        'tier': 'Medium',
        'height': (58, '2d10'),
        'weight': (90, '2d4')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
}

data['Tiefling'] = {
    'base_ab_mod': {},
    'lifespan': 105,  # Fabricated, PHB says 'human-like... few [more]'
    'size': {
        'tier': 'Medium',
        'height': (56, '2d10'),
        'weight': (110, '2d4')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
    'subrace': {
        'Asmodeus': {
            'ab_mod': {
                'Intelligence': 1,
                'Charisma': 2
            }
        },
        'Baalzebul': {
            'ab_mod': {
                'Intelligence': 1,
                'Charisma': 2
            }
        },
        'Dispater': {
            'ab_mod': {
                'Dexterity': 1,
                'Charisma': 2
            }
        },
        'Fierna': {
            'ab_mod': {
                'Wisdom': 1,
                'Charisma': 2
            }
        },
        'Glasya': {
            'ab_mod': {
                'Dexterity': 1,
                'Charisma': 2
            }
        },
        'Levistus': {
            'ab_mod': {
                'Constitution': 1,
                'Charisma': 2
            }
        },
        'Mammon': {
            'ab_mod': {
                'Intelligence': 1,
                'Charisma': 2
            }
        },
        'Mephistopheles': {
            'ab_mod': {
                'Intelligence': 1,
                'Charisma': 2
            }
        },
        'Zariel': {
            'ab_mod': {
                'Strength': 1,
                'Charisma': 2
            }
        },
    },
    'variant1': {
        'Feral': {
            'ab_mod': {
                'Dexterity': 2,
                'Intelligence': 1
            }
        }
    },
    'variant2': {
        'Winged': {
            'speed': {
                'flying': 30
            }
        }
    }
}

data['Tortle'] = {
    'base_ab_mod': {
        'Strength': 2,
        'Wisdom': 1
    },
    'lifespan': 50,
    'size': {
        'tier': 'Medium',
        'height': (60, '2d6'),   # Fabricated, ToA says '5 to 6'
        'weight': (430, '2d20')  # Fabricated, ToA says 'average 450'
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
}

data['Triton'] = {
    'base_ab_mod': {
        'Strength': 1,
        'Constitution': 1,
        'Charisma': 1
    },
    'lifespan': 200,
    'size': {
        'tier': 'Medium',
        'height': (54, '2d10'),
        'weight': (90, '2d4')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': 30
    },
}

data['Yuan-Ti Pureblood'] = {
    'base_ab_mod': {
        'Intelligence': 1,
        'Charisma': 2
    },
    'lifespan': 100,
    'size': {
        'tier': 'Medium',
        'height': (56, '2d10'),
        'weight': (110, '2d4')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': 30
    },
}
