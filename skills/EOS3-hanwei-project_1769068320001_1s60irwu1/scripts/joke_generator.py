#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import random

def generate_joke(joke_type='random', theme='general', language='zh'):
    jokes_db = {
        'cold': [
            {'zh': '为什么企鹅的肚子是白的？因为它手太短，洗澡只能洗到肚子。', 'en': 'Why is the penguin belly white? Because its arms are too short to wash its back.'},
            {'zh': '为什么海鸥不住海边？因为住海边就成海（害）鸥了。', 'en': 'Why do seagulls not live by the sea? Because then they would be bay-gulls (bagels).'},
        ],
        'riddle': [
            {'zh': '什么东西越洗越脏？答案：水', 'en': 'What gets dirtier the more you wash it? Answer: Water'},
            {'zh': '什么门永远关不上？答案：球门', 'en': 'What door can never be closed? Answer: A goalpost'},
        ],
        'tech': [
            {'zh': '为什么程序员总是分不清万圣节和圣诞节？因为 Oct 31 = Dec 25', 'en': 'Why do programmers confuse Halloween and Christmas? Because Oct 31 = Dec 25'},
            {'zh': '程序员的三大谎言：1.明天就能修好 2.一定写注释 3.不用测试', 'en': 'Three programmer lies: 1. Will fix tomorrow 2. Will write comments 3. No need to test'},
        ]
    }
    
    if joke_type == 'random':
        joke_type = random.choice(list(jokes_db.keys()))
    
    jokes = jokes_db.get(joke_type, jokes_db['cold'])
    selected_joke = random.choice(jokes)
    
    result = {
        'type': joke_type,
        'theme': theme,
        'joke': selected_joke.get(language, selected_joke['zh']),
        'language': language
    }
    
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result

if __name__ == '__main__':
    joke_type = sys.argv[1] if len(sys.argv) > 1 else 'random'
    theme = sys.argv[2] if len(sys.argv) > 2 else 'general'
    language = sys.argv[3] if len(sys.argv) > 3 else 'zh'
    
    generate_joke(joke_type, theme, language)