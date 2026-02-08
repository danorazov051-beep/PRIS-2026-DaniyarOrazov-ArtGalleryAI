import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULES_PATH = os.path.join(BASE_DIR, "data", "raw", "rules.json")


def load_rules():
    with open(RULES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def check_rules(artwork):
    rules = load_rules()

    
    if rules["critical_rules"]["must_be_authentic"] and not artwork["is_authentic"]:
        return "⛔ Критическая ошибка: произведение не является подлинным"

   
    if artwork["price"] < rules["thresholds"]["min_price"]:
        return "❌ Отказ: цена слишком низкая"

    if artwork["price"] > rules["thresholds"]["max_price"]:
        return "❌ Отказ: цена слишком высокая"

    
    for tag in artwork["tags"]:
        if tag in rules["lists"]["forbidden_tags"]:
            return f"⚠️ Найден запрещённый тег: {tag}"

    return f"✅ Успех: произведение соответствует сценарию «{rules['scenario_name']}»"
