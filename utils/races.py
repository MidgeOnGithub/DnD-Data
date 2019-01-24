# Opting to separately declare and append values to data like a list
# instead of initializing the whole object in one confusing super-brace
data = []

data.append({
    'race': 'Aarakocra',
    'source': 'EE',
    'adventure_league': False,
    'base_ability_modifier': {
        'Dexterity': 2,
        'Wisdom': 1
    },
    'lifespan': '30',
    'size': {
        'tier': 'Medium',
        'height': (57, '2d2'),  # Fabricated, EE: 'about 5 feet'
        'weight': (76, '2d3')   # Fabricated, EE: 'between 80 and 100'
    },
    'speed': {
        'standard': 25,
        'climbing': None,
        'flying': 50,
        'swimming': None
    }
})

data.append({
    'race': 'Aasimar',
    'source': 'VOLO',
    'adventure_league': True,
    'base_ability_modifier': {
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
            'ability_modifier': {
                'Strength': 1
            }
        },
        'Protector': {
            'ability_modifier': {
                'Wisdom': 1
            }
        },
        'Scourge': {
            'ability_modifier': {
                'Constitution': 1
            }
        },
    }
})

data.append({
    'race': 'Bugbear',
    'source': 'VOLO',
    'adventure_league': True,
    'base_ability_modifier': {
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
})

data.append({
    'race': 'Dragonborn',
    'source': 'PHB',
    'adventure_league': True,
    'base_ability_modifier': {
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
})

data.append({
    'race': 'Dwarf',
    'source': 'PHB',
    'adventure_league': True,
    'base_ability_modifier': {
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
            'source': 'SCAG',
            'ability_modifier': {
                'Strength': 1
            },
            'size': {
                'height': (48, '2d6'),   # Fabricated, PHB: 'between' 4-5
                'weight': (140, '2d4')   # Fabricated, PHB: 'around' 150
            }
        },
        'Hill': {
            'ability_modifier': {
                'Wisdom': 1
            },
            'size': {
                'height': (44, '2d4'),
                'weight': (115, '2d6')
            }
        },
        'Mountain': {
            'ability_modifier': {
                'Strength': 2
            },
            'size': {
                'height': (48, '2d4'),
                'weight': (130, '2d6')
            }
        }
    }
})

data.append({
    'race': 'Elf',
    'source': 'PHB',
    'adventure_league': True,
    'base_ability_modifier': {
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
            'ability_modifier': {
                'Charisma': 1
            },
            'size': {
                'height': (53, '2d6'),
                'weight': (75, '1d6')
            }
        },
        'Eladrin': {
            'source': 'MTOF',
            'ability_modifier': {
                'Charisma': 1
            },
            'size': {
                'height': (54, '2d12'),
                'weight': (90, '1d4')
            }
        },
        'High': {
            'ability_modifier': {
                'Intelligence': 1
            },
            'size': {
                'height': (54, '2d10'),
                'weight': (90, '1d4')
            }
        },
        'Sea': {
            'source': 'MTOF',
            'ability_modifier': {
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
            'source': 'MTOF',
            'ability_modifier': {
                'Constitution': 1
            },
            'size': {
                'height': (56, '2d8'),
                'weight': (90, '1d4')
            }
        },
        'Wood': {
            'ability_modifier': {
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
})

data.append({
    'race': 'Firbolg',
    'source': 'VOLO',
    'adventure_league': True,
    'base_ability_modifier': {
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
})

data.append({
    'race': 'Genasi',
    'source': 'EE',
    'adventure_league': True,
    'base_ability_modifier': {
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
            'ability_modifier': {
                'Dexterity': 1
            }
        },
        'Earth': {
            'ability_modifier': {
                'Strength': 1
            }
        },
        'Fire': {
            'ability_modifier': {
                'Intelligence': 1
            }
        },
        'Water': {
            'ability_modifier': {
                'Wisdom': 1
            },
            'speed': {
                'swimming': 30
            }
        }
    }
})

data.append({
    'race': 'Gith',
    'source': 'MToF',
    'adventure_league': True,
    'base_ability_modifier': {
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
            'ability_modifier': {
                'Strength': 2
            },
            'size': {
                'height': (60, '2d12'),
                'weight': (100, '2d4')
            }
        },
        'Githzerai': {
            'ability_modifier': {
                'Wisdom': 2
            },
            'size': {
                'height': (59, '2d12'),
                'weight': (90, '1d4')
            }
        }
    }
})

data.append({
    'race': 'Gnome',
    'source': 'PHB',
    'adventure_league': True,
    'base_ability_modifier': {
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
        'Svirfneblin': {
            'source': 'EE',
            'ability_modifier': {
                'Dexterity': 1
            },
            'lifespan': '200:250',
            'size': {
                'tier': 'Small',
                'height': (35, '2d2'),  # Fabricated, EE: 'about 3 to 3 1/2 feet'
                'weight': (82, '1d8')   # Fabricated, EE: 'about 80 to 120'
            },
        },
        'Forest': {
            'ability_modifier': {
                'Dexterity': 1
            }
        },
        'Rock': {
            'ability_modifier': {
                'Constitution': 1
            }
        }
    }
})

data.append({
    'race': 'Goblin',
    'source': 'VOLO',
    'adventure_league': True,
    'base_ability_modifier': {
        'Dexterity': 2,
        'Constitution': 1
    },
    'lifespan': '60',
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
})

data.append({
    'race': 'Goliath',
    'source': 'VOLO',
    'adventure_league': True,
    'base_ability_modifier': {
        'Strength': 2,
        'Constitution': 1
    },
    'lifespan': '100',
    'size': {
        'tier': 'Medium',
        'height': (74, '2d10'),
        'weight': (200, '2d6')
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    }
})

data.append({
    'race': 'Half-Elf',
        'source': 'PHB',
    'adventure_league': True,
    'base_ability_modifier': {
        'Charisma': 2,
        'Choice1': 1,
        'Choice2': 1
    },
    'lifespan': '180',
    'size': {
        'tier': 'Medium',
        'height': (57, '2d8'),
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
            'source': 'SCAG',
            'speed': {
                'swimming': 30
            }
        },
        'Drow Heritage': {
            'source': 'SCAG'
        },
        'High Elf Heritage': {
            'source': 'SCAG'
        },
        'Wood Elf Heritage': {
            'source': 'SCAG'
        }
    }
})

data.append({
    'race': 'Half-Orc',
    'source': 'PHB',
    'adventure_league': True,
    'base_ability_modifier': {
        'Strength': 2,
        'Constitution': 1
    },
    'lifespan': '75',
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
})

data.append({
    'race': 'Halfling',
    'source': 'PHB',
    'adventure_league': True,
    'base_ability_modifier': {
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
            'source': 'SCAG',
            'ability_modifier': {
                'Wisdom': 1
            }
        },
        'Lightfoot': {
            'ability_modifier': {
                'Charisma': 1
            }
        },
        'Stout': {
            'ability_modifier': {
                'Constitution': 1
            }
        }
    }
})

data.append({
    'race': 'Hobgoblin',
    'source': 'VOLO',
    'adventure_league': True,
    'base_ability_modifier': {
        'Constitution': 2,
        'Intelligence': 1
    },
    'lifespan': '100',
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
})

data.append({
    'race': 'Human',
    'source': 'PHB',
    'adventure_league': True,
    'base_ability_modifier': {
        'Strength': 1,
        'Dexterity': 1,
        'Constitution': 1,
        'Intelligence': 1,
        'Wisdom': 1,
        'Charisma': 1
    },
    'lifespan': '100',
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
            'ability_modifier': {
                'Choice1': 1,
                'Choice2': 1
            }
        }
    }
})

data.append({
    'race': 'Kenku',
    'source': 'VOLO',
    'adventure_league': True,
    'base_ability_modifier': {
        'Dexterity': 2,
        'Wisdom': 1
    },
    'lifespan': '60',
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
})

data.append({
    'race': 'Kobold',
    'source': 'VOLO',
    'adventure_league': True,
    'base_ability_modifier': {
        'Strength': 2,
        'Dexterity': 2
    },
    'lifespan': '120',
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
})

data.append({
    'race': 'Lizardfolk',
    'source': 'VOLO',
    'adventure_league': True,
    'base_ability_modifier': {
        'Constitution': 2,
        'Wisdom': 1
    },
    'lifespan': '60',
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
})

data.append({
    'race': 'Orc',
    'source': 'VOLO',
    'adventure_league': True,
    'base_ability_modifier': {
        'Strength': 2,
        'Constitution': 1,
        'Intelligence': 2
    },
    'lifespan': '50',
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
})

data.append({
    'race': 'Tabaxi',
    'source': 'VOLO',
    'adventure_league': True,
    'base_ability_modifier': {
        'Dexterity': 2,
        'Charisma': 1
    },
    'lifespan': '100',
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
})

data.append({
    'race': 'Tiefling',
    'source': 'PHB',
    'adventure_league': True,
    'base_ability_modifier': {},
    'lifespan': '105',  # Fabricated, PHB: 'human-like... few [more]'
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
            'ability_modifier': {
                'Intelligence': 1,
                'Charisma': 2
            }
        },
        'Baalzebul': {
            'source': 'MToF',
            'ability_modifier': {
                'Intelligence': 1,
                'Charisma': 2
            }
        },
        'Dispater': {
            'source': 'MToF',
            'ability_modifier': {
                'Dexterity': 1,
                'Charisma': 2
            }
        },
        'Fierna': {
            'source': 'MToF',
            'ability_modifier': {
                'Wisdom': 1,
                'Charisma': 2
            }
        },
        'Glasya': {
            'source': 'MToF',
            'ability_modifier': {
                'Dexterity': 1,
                'Charisma': 2
            }
        },
        'Levistus': {
            'source': 'MToF',
            'ability_modifier': {
                'Constitution': 1,
                'Charisma': 2
            }
        },
        'Mammon': {
            'source': 'MToF',
            'ability_modifier': {
                'Intelligence': 1,
                'Charisma': 2
            }
        },
        'Mephistopheles': {
            'source': 'MToF',
            'ability_modifier': {
                'Intelligence': 1,
                'Charisma': 2
            }
        },
        'Zariel': {
            'source': 'MToF',
            'ability_modifier': {
                'Strength': 1,
                'Charisma': 2
            }
        },
    },
    'variant1': {
        'Feral': {
            'source': 'SCAG',
            'ability_modifier': {
                'Dexterity': 2,
                'Intelligence': 1
            }
        }
    },
    'variant2': {
        'Winged': {
            'source': 'SCAG',
            'adventure_league': False,
            'speed': {
                'flying': 30
            }
        }
    }
})

data.append({
    'race': 'Tortle',
    'source': 'MToF+',
    'adventure_league': True,
    'adventure_league_source': 'XGE',
    'base_ability_modifier': {
        'Strength': 2,
        'Wisdom': 1
    },
    'lifespan': 50,
    'size': {
        'tier': 'Medium',
        'height': (60, '2d6'),   # Fabricated, ToA: '5 to 6'
        'weight': (400, '2d8')   # Fabricated, ToA: 'average 450'
    },
    'speed': {
        'standard': 30,
        'climbing': None,
        'flying': None,
        'swimming': None
    },
})

data.append({
    'race': 'Triton',
    'source': 'VOLO',
    'adventure_league': True,
    'base_ability_modifier': {
        'Strength': 1,
        'Constitution': 1,
        'Charisma': 1
    },
    'lifespan': '200',
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
})

data.append({
    'race': 'Yuan-Ti Pureblood',
    'source': 'VOLO',
    'adventure_league': True,
    'base_ability_modifier': {
        'Intelligence': 1,
        'Charisma': 2
    },
    'lifespan': '100',
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
})
